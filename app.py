import streamlit as st
import os
from typing import TypedDict, Annotated, List
from datetime import datetime, timedelta
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import json

# Load environment 
load_dotenv()

# Configure Streamlit page
st.set_page_config(
    page_title="SafarSathi - AI Travel Planner",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load external CSS
def load_css():
    """Load CSS from external file"""
    css_file = os.path.join(os.path.dirname(__file__), "static", "styles.css")
    try:
        with open(css_file) as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("⚠️ CSS file not found. Using default styling.")

# Load styles
load_css()

# Define PlannerState
class PlannerState(TypedDict):
    messages: Annotated[List[HumanMessage | AIMessage], "The messages in the conversation"]
    from_city: str
    city: str
    interests: List[str]
    itinerary: str
    start_date: str
    end_date: str
    num_travelers: int
    budget_per_person: float
    total_budget: float
    hotel_recommendations: str
    food_recommendations: str
    travel_style: str
    accommodation_type: str
    currency: str
    currency_symbol: str

# Initialize session state
if 'state' not in st.session_state:
    st.session_state.state = {
        "messages": [],
        "from_city": "",
        "city": "",
        "interests": [],
        "itinerary": "",
        "start_date": "",
        "end_date": "",
        "num_travelers": 2,
        "budget_per_person": 0.0,
        "total_budget": 0.0,
        "hotel_recommendations": "",
        "food_recommendations": "",
        "travel_style": "Balanced",
        "accommodation_type": "Hotel",
        "currency": "USD",
        "currency_symbol": "$"
    }

if 'history' not in st.session_state:
    st.session_state.history = []

@st.cache_resource
def get_llm():
    try:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key or api_key == "your_groq_api_key_here":
            st.error("❌ GROQ API Key not configured!")
            st.warning("""
            **To fix this:**
            1. Visit https://console.groq.com/keys
            2. Sign up or log in (it's free!)
            3. Create a new API key
            4. Update the `.env` file with your API key
            5. Restart the application
            """)
            return None
        
        return ChatGroq(
            temperature=0.7,
            groq_api_key=api_key,
            model_name="llama-3.3-70b-versatile"
        )
    except Exception as e:
        st.error(f"❌ Error initializing ChatGroq: {str(e)}")
        st.info("💡 Make sure your GROQ API key is valid and has proper permissions.")
        return None

# Enhanced itinerary prompt with real-world details
itinerary_prompt = ChatPromptTemplate.from_messages([
    ("system", """You are SafarSathi, an expert AI travel planner with extensive real-world knowledge of global destinations.
    Create a comprehensive, detailed travel itinerary from {from_city} to {city} with the following requirements:
    
    - Origin City: {from_city}
    - Destination City: {city}
    - Travel Style: {travel_style}
    - Interests: {interests}
    - Dates: {start_date} to {end_date} ({num_days} days)
    - Total Travelers: {total_travelers}
    - Budget: {currency_symbol}{total_budget} in {currency} ({currency_symbol}{budget_per_person} per person)
    - Accommodation Type: {accommodation_type}
    
    **IMPORTANT: All prices and costs MUST be in {currency} ({currency_symbol}). Convert all amounts to {currency}.**
    
    IMPORTANT: Provide REAL, SPECIFIC recommendations with actual names and details:
    
    1. **Flight & Rail Options from {from_city} to {city}**
       - Suggest specific airlines with real names and flight numbers if available (e.g., IndiGo 6E-123, Air India AI-456)
       - Provide approximate flight times and prices including departure and arrival times
       - **IMPORTANT: Recommend REAL train routes with COMPLETE TIMING DETAILS:**
         * For India: Use real train names like "Rajdhani Express 12951", "Shatabdi 12002", "Vande Bharat Express", "Duronto Express" with actual numbers
         * **Include DEPARTURE TIME, ARRIVAL TIME, and JOURNEY DURATION** (e.g., "Rajdhani Express 12951 - Departs: 4:55 PM, Arrives: 8:35 AM next day, Duration: 15h 40m")
         * For Japan: Use real Shinkansen services like "Nozomi", "Hikari", "Kodama" with timing
         * For Europe: Use actual train services like "Eurostar 9056", "TGV 6821", "ICE 71" with departure/arrival times
         * For USA: Use Amtrak services with real names like "Northeast Regional", "Acela Express" with schedule
         * Research and provide only trains that actually operate between these specific cities
         * Specify which days the train operates (daily, except Sundays, etc.)
       - Include booking platforms (Skyscanner, Google Flights, Make My Trip, Yatra, Cleartrip, IRCTC for India trains)
       - Mention best booking times for deals
       - Provide layover information if applicable
    
    2. **Day-by-Day Itinerary**
       - **CRITICAL: START Day 1 activities based on ACTUAL ARRIVAL TIME at {city}**
         * If arriving by train at 8:35 AM, start Day 1 activities from 9:00 AM or 10:00 AM
         * If arriving by flight at 2:00 PM, start Day 1 activities from 3:00 PM or 4:00 PM after airport transfer
         * Account for check-in time at hotel/accommodation
         * Be realistic about jet lag and travel fatigue for flight arrivals
       - **For LAST DAY: Schedule activities based on DEPARTURE TIME**
         * If train/flight departs at 5:00 PM, plan activities only until 1:00-2:00 PM
         * Include travel time to station/airport
         * Allow time for check-out and reaching departure point
       - Include specific attraction names, addresses, and neighborhoods
       - Provide realistic timings (e.g., "10:00 AM - Visit Eiffel Tower, Champ de Mars")
       - Mention actual landmarks, museums, parks, and locations
       - Include approximate costs for each activity
       - Consider realistic travel time between locations
    
    3. **Hotel Recommendations** (3-5 options)
       - Name actual hotels, hostels, or guesthouses with real names
       - Provide realistic price ranges (per night)
       - Mention specific neighborhoods/areas (e.g., "Marais District", "Shinjuku Area")
       - Include amenities and why each is recommended
       - Provide booking platform suggestions (Booking.com, Agoda, Airbnb, Hotels.com)
    
    4. **Food & Dining**
       - Recommend real restaurants, cafes, and street food spots with actual names
       - Include specific dishes to try (e.g., "Try the ramen at Ichiran Shibuya")
       - Mention average meal costs
       - Suggest breakfast, lunch, and dinner options for each day
       - Include popular food delivery apps if relevant
    
    5. **Transportation in {city}**
       - Recommend specific metro lines, bus routes, or taxi apps
       - Provide actual costs (e.g., "Paris Metro day pass: €7.50")
       - Mention if Uber/Grab/Ola/local alternatives work
       - Include airport transfer options with prices
       - Suggest car rental options if applicable
    
    6. **Budget Breakdown**
       - Flights/Trains from {from_city} to {city}: [estimated cost with booking tips]
       - Accommodation: [specific amount based on recommendations]
       - Food: [daily estimate with meal breakdown]
       - Activities/Entry fees: [list major costs]
       - Transportation: [local transport + any day trips]
       - Miscellaneous: [souvenirs, tips, etc.]
       - Total: [sum of all expenses]
    
    7. **Return Journey Options from {city} to {from_city}**
       - Suggest specific flights with airline names, flight numbers, and complete timing (departure, arrival, duration)
       - **IMPORTANT: Recommend REAL return train routes with COMPLETE TIMING DETAILS:**
         * Use only trains that actually operate between these specific cities
         * **Include DEPARTURE TIME, ARRIVAL TIME, and JOURNEY DURATION** (e.g., "Rajdhani Express 12952 - Departs: 5:15 PM, Arrives: 9:10 AM next day, Duration: 15h 55m")
         * Specify operating days (daily, specific days only, etc.)
       - Include approximate costs and booking tips
       - Mention best time to book for discounts
    
    8. **Local Tips**
       - Best times to visit popular attractions (avoid crowds)
       - Local customs and etiquette
       - Hidden gems and off-the-beaten-path recommendations
       - Useful phrases in local language
       - SIM card/WiFi options with provider names
    
    9. **Safety & Health**
       - Emergency numbers
       - Healthcare facilities nearby
       - Safe neighborhoods vs areas to avoid
       - Common scams to watch out for
    
    10. **Packing Suggestions**
       - Based on actual weather for those dates
       - Essential items for planned activities
       - Power adapter requirements
    
    Make recommendations PRACTICAL and ACTIONABLE with real place names, actual costs, and verifiable information. Be specific rather than generic. Use emojis to make it visually appealing. Ensure all hotels, restaurants, airlines, and attractions are REAL and can be verified."""),
    ("human", "Create my dream itinerary from {from_city} to {city} with real, specific recommendations including flights, trains, hotels, and return journey!"),
])

# Sample itinerary template for demonstration
SAMPLE_ITINERARY_TEMPLATE = """
# 🌏 Sample Travel Itinerary

## ⚠️ API Configuration Required

To generate personalized itineraries for **{city}**, please configure your GROQ API key.

**Quick Setup (5 minutes):**
1. Visit: https://console.groq.com/keys
2. Create a free account and generate an API key
3. Add your key to the `.env` file
4. Restart the application

---

## 📋 What You'll Get After Setup:

### ✨ Your Personalized Itinerary Will Include:

**🗓️ Day-by-Day Planning**
- Specific attractions with real names and locations
- Optimal timing for each activity
- Estimated costs for entries and activities

**🏨 Accommodation Recommendations**
- Real hotel/hostel names and locations
- Price ranges matching your ${budget_per_person:.0f}/person budget
- Best areas to stay in {city}

**🍽️ Food & Dining**
- Local restaurants and street food spots
- Must-try dishes and cuisines
- Budget-friendly to luxury options

**🚗 Transportation Guide**
- Airport transfers
- Local transport options (metro, bus, taxi)
- Day trip recommendations

**💰 Complete Budget Breakdown**
- Accommodation costs
- Daily food expenses
- Activity fees
- Transportation
- Emergency fund suggestions

**🎯 Personalized for Your Interests:**
{interests}

**👥 Optimized for {num_travelers} Travelers**

---

## 🚀 Get Started Now!

See [`API_KEY_SETUP.md`](API_KEY_SETUP.md) for detailed setup instructions.

Once configured, click **"Generate My Itinerary"** again to get your complete, personalized travel plan! ✈️
"""

def create_itinerary(state: PlannerState) -> str:
    try:
        llm = get_llm()
        if llm is None:
            return """❌ **Failed to Initialize AI Model**
            
Please configure your GROQ API key:
1. Visit: https://console.groq.com/keys
2. Sign up for a free account
3. Generate a new API key
4. Update the `.env` file with your key
5. Restart the application

The GROQ API is free and provides fast, high-quality AI responses for travel planning."""
        
        # Calculate number of days
        start = datetime.strptime(state["start_date"], "%Y-%m-%d")
        end = datetime.strptime(state["end_date"], "%Y-%m-%d")
        num_days = (end - start).days + 1
            
        response = llm.invoke(itinerary_prompt.format_messages(
            from_city=state["from_city"],
            city=state["city"],
            interests=", ".join(state["interests"]),
            start_date=state["start_date"],
            end_date=state["end_date"],
            num_days=num_days,
            total_travelers=state["num_travelers"],
            total_budget=state["total_budget"],
            budget_per_person=state["budget_per_person"],
            travel_style=state["travel_style"],
            accommodation_type=state["accommodation_type"],
            currency=state.get("currency", "USD"),
            currency_symbol=state.get("currency_symbol", "$")
        ))
        return response.content
    except Exception as e:
        error_msg = str(e).lower()
        if "api" in error_msg and ("key" in error_msg or "401" in error_msg or "invalid" in error_msg):
            return f"""⚠️ **API Key Error**

{str(e)}

**Solution:**
1. Visit: https://console.groq.com/keys
2. Create or copy your API key (should start with 'gsk_')
3. Open the `.env` file in this project
4. Replace `your_groq_api_key_here` with your actual key
5. Save the file and restart the application

**Note:** GROQ provides free API access for travel planning!"""
        else:
            return f"""⚠️ **An error occurred while generating the itinerary:**

{str(e)}

**Possible Solutions:**
- Check your internet connection
- Verify your GROQ API key is valid
- Try again in a moment
- If the problem persists, check https://status.groq.com/"""

def save_to_history(state):
    """Save trip to history"""
    trip_data = {
        "from_city": state.get("from_city", "N/A"),
        "city": state["city"],
        "dates": f"{state['start_date']} to {state['end_date']}",
        "travelers": state["num_travelers"],
        "budget": state["total_budget"],
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    st.session_state.history.append(trip_data)

def main():
    # Hero Header
    st.markdown("""
        <div class="title-container">
            <div class="title-text">✈️ SafarSathi</div>
            <div class="subtitle-text">Your AI-Powered Travel Companion</div>
        </div>
    """, unsafe_allow_html=True)
    
    # Sidebar for input
    with st.sidebar:
        st.markdown("### 🎯 Plan Your Perfect Trip")
        
        # Trip Details Section
        with st.expander("🗺️ Journey Details", expanded=True):
            from_city = st.text_input("🏠 From (Origin City)", placeholder="e.g., Mumbai, Delhi, New York", help="Enter your starting city")
            city = st.text_input("📍 To (Destination City)", placeholder="e.g., Paris, Tokyo, Dubai", help="Enter your destination city")
            
            col1, col2 = st.columns(2)
            with col1:
                start_date = st.date_input("🛫 Start Date", value=datetime.now() + timedelta(days=7))
            with col2:
                end_date = st.date_input("🛬 End Date", value=datetime.now() + timedelta(days=14))
            
            # Currency Selection
            st.markdown("---")
            currency_options = {
                "USD ($) - US Dollar": ("USD", "$"),
                "EUR (€) - Euro": ("EUR", "€"),
                "GBP (£) - British Pound": ("GBP", "£"),
                "INR (₹) - Indian Rupee": ("INR", "₹"),
                "JPY (¥) - Japanese Yen": ("JPY", "¥"),
                "AUD (A$) - Australian Dollar": ("AUD", "A$"),
                "CAD (C$) - Canadian Dollar": ("CAD", "C$"),
                "AED (د.إ) - UAE Dirham": ("AED", "د.إ"),
                "CNY (¥) - Chinese Yuan": ("CNY", "¥"),
                "SGD (S$) - Singapore Dollar": ("SGD", "S$")
            }
            
            selected_currency = st.selectbox(
                "💱 Preferred Currency",
                options=list(currency_options.keys()),
                index=0,
                help="Select your preferred currency for all costs and budgets"
            )
            currency, currency_symbol = currency_options[selected_currency]
        
        # Traveler Details
        with st.expander("👥 Travelers & Style", expanded=True):
            num_travelers = st.number_input("Number of Travelers", min_value=1, max_value=20, value=2)
            
            travel_style = st.selectbox(
                "🎨 Travel Style",
                ["Budget Backpacker", "Balanced Explorer", "Comfort Seeker", "Luxury Traveler", "Adventure Enthusiast", "Cultural Immersion"]
            )
            
            accommodation_type = st.selectbox(
                "🏨 Accommodation Preference",
                ["Hotel", "Hostel", "Airbnb", "Resort", "Boutique Hotel", "Mixed"]
            )
        
        # Interests
        with st.expander("💫 Interests & Activities", expanded=True):
            interests = st.multiselect(
                "What interests you?",
                ["Sightseeing", "Food & Dining", "Adventure Sports", "Shopping", "Nightlife", 
                 "Museums & Art", "Nature & Wildlife", "Photography", "History & Culture",
                 "Beach & Water Sports", "Mountain Trekking", "Local Experiences"],
                default=["Sightseeing", "Food & Dining"]
            )
            
            custom_interests = st.text_input("✨ Additional Interests (optional)", placeholder="e.g., wine tasting, scuba diving")
            if custom_interests:
                interests.extend([i.strip() for i in custom_interests.split(",")])
        
        # Budget
        with st.expander("💰 Budget Planning", expanded=True):
            budget_per_person = st.number_input(
                f"Budget per Person ({currency})",
                min_value=0.0,
                value=1000.0,
                step=100.0,
                help=f"Total budget for the entire trip per person in {currency}"
            )
           
            total_budget = num_travelers * budget_per_person
            st.markdown(f"**Total Trip Budget:** {currency_symbol}{total_budget:,.2f}")
        
        st.markdown("---")
        
        # Generate Button
        generate_btn = st.button("🚀 Generate My Itinerary", use_container_width=True)
        
        if generate_btn:
            if not from_city:
                st.error("⚠️ Please enter your origin city!")
            elif not city:
                st.error("⚠️ Please enter a destination city!")
            elif not interests:
                st.error("⚠️ Please select at least one interest!")
            elif start_date >= end_date:
                st.error("⚠️ End date must be after start date!")
            else:
                with st.spinner("✨ Creating your personalized itinerary... This may take a moment!"):
                    # Update state
                    st.session_state.state.update({
                        "from_city": from_city,
                        "city": city,
                        "interests": interests,
                        "start_date": start_date.strftime("%Y-%m-%d"),
                        "end_date": end_date.strftime("%Y-%m-%d"),
                        "num_travelers": num_travelers,
                        "budget_per_person": budget_per_person,
                        "total_budget": total_budget,
                        "travel_style": travel_style,
                        "accommodation_type": accommodation_type,
                        "currency": currency,
                        "currency_symbol": currency_symbol
                    })
                    
                    # Generate itinerary
                    itinerary = create_itinerary(st.session_state.state)
                    st.session_state.state["itinerary"] = itinerary
                    
                    # Save to history
                    save_to_history(st.session_state.state)
                    
                    st.success("✅ Itinerary created successfully!")
                    st.balloons()
        
        # Quick Stats
        if st.session_state.state["itinerary"]:
            st.markdown("---")
            st.markdown("### 📊 Trip Overview")
            
            start = datetime.strptime(st.session_state.state["start_date"], "%Y-%m-%d")
            end = datetime.strptime(st.session_state.state["end_date"], "%Y-%m-%d")
            num_days = (end - start).days + 1
            
            st.metric("Duration", f"{num_days} days")
            st.metric("Travelers", st.session_state.state["num_travelers"])
            currency_symbol_display = st.session_state.state.get("currency_symbol", "$")
            st.metric("Budget", f"{currency_symbol_display}{st.session_state.state['total_budget']:,.0f}")
    
    # Main content area
    if st.session_state.state["itinerary"]:
        # Tabs for better organization
        tab1, tab2, tab3 = st.tabs(["📋 Your Itinerary", "🗂️ Trip History", "💡 Travel Tips"])
        
        with tab1:
            # Key Metrics
            col1, col2, col3, col4 = st.columns(4)
            
            start = datetime.strptime(st.session_state.state["start_date"], "%Y-%m-%d")
            end = datetime.strptime(st.session_state.state["end_date"], "%Y-%m-%d")
            num_days = (end - start).days + 1
            daily_budget = st.session_state.state["budget_per_person"] / num_days
            
            with col1:
                st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-value">{st.session_state.state.get("from_city", "N/A")} → {st.session_state.state["city"]}</div>
                        <div class="metric-label">Journey</div>
                    </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-value">{num_days}</div>
                        <div class="metric-label">Days</div>
                    </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-value">{st.session_state.state["num_travelers"]}</div>
                        <div class="metric-label">Travelers</div>
                    </div>
                """, unsafe_allow_html=True)
            
            with col4:
                currency_symbol_display = st.session_state.state.get("currency_symbol", "$")
                st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-value">{currency_symbol_display}{daily_budget:.0f}</div>
                        <div class="metric-label">Per Day/Person</div>
                    </div>
                """, unsafe_allow_html=True)
            
            # Itinerary Display
            st.markdown('<div class="itinerary-container">', unsafe_allow_html=True)
            st.markdown(st.session_state.state["itinerary"])
            st.markdown('</div>', unsafe_allow_html=True)
            
            # Action Buttons
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.download_button(
                    label="📥 Download as Text",
                    data=st.session_state.state["itinerary"],
                    file_name=f"safarsathi_{st.session_state.state['city'].lower().replace(' ', '_')}_itinerary.txt",
                    mime="text/plain",
                    use_container_width=True
                )
            
            with col2:
                # Create markdown version
                md_content = f"""# {st.session_state.state.get('from_city', 'N/A')} → {st.session_state.state['city']} Trip Itinerary

**Generated by SafarSathi**

## Trip Details
- **From:** {st.session_state.state.get('from_city', 'N/A')}
- **To:** {st.session_state.state['city']}
- **Dates:** {st.session_state.state['start_date']} to {st.session_state.state['end_date']}
- **Travelers:** {st.session_state.state['num_travelers']}
- **Budget:** ${st.session_state.state['total_budget']:,.2f}

---

{st.session_state.state['itinerary']}
"""
                st.download_button(
                    label="📄 Download as Markdown",
                    data=md_content,
                    file_name=f"safarsathi_{st.session_state.state['city'].lower().replace(' ', '_')}_itinerary.md",
                    mime="text/markdown",
                    use_container_width=True
                )
            
            with col3:
                # Create JSON export
                json_data = {
                    "from_city": st.session_state.state.get('from_city', 'N/A'),
                    "destination": st.session_state.state['city'],
                    "start_date": st.session_state.state['start_date'],
                    "end_date": st.session_state.state['end_date'],
                    "travelers": st.session_state.state['num_travelers'],
                    "budget": st.session_state.state['total_budget'],
                    "interests": st.session_state.state['interests'],
                    "travel_style": st.session_state.state['travel_style'],
                    "itinerary": st.session_state.state['itinerary']
                }
                st.download_button(
                    label="💾 Export as JSON",
                    data=json.dumps(json_data, indent=2),
                    file_name=f"safarsathi_{st.session_state.state['city'].lower().replace(' ', '_')}_data.json",
                    mime="application/json",
                    use_container_width=True
                )
        
        with tab2:
            st.markdown("### 🗂️ Your Trip History")
            
            if st.session_state.history:
                for idx, trip in enumerate(reversed(st.session_state.history), 1):
                    journey_label = f"{trip.get('from_city', 'N/A')} → {trip['city']}"
                    with st.expander(f"Trip #{idx}: {journey_label} - {trip['dates']}"):
                        col1, col2 = st.columns(2)
                        with col1:
                            st.write(f"**From:** {trip.get('from_city', 'N/A')}")
                            st.write(f"**To:** {trip['city']}")
                            st.write(f"**Travelers:** {trip['travelers']}")
                        with col2:
                            st.write(f"**Budget:** ${trip['budget']:,.2f}")
                            st.write(f"**Planned on:** {trip['timestamp']}")
            else:
                st.info("📝 No trip history yet. Start planning your first trip!")
        
        with tab3:
            st.markdown("### 💡 Essential Travel Tips")
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                <div class="info-card">
                    <h4>✅ Before You Go</h4>
                    <ul>
                        <li>Check passport validity (6+ months)</li>
                        <li>Research visa requirements</li>
                        <li>Get travel insurance</li>
                        <li>Notify your bank about travel</li>
                        <li>Make copies of important documents</li>
                        <li>Research local customs and laws</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("""
                <div class="info-card">
                    <h4>💰 Money Matters</h4>
                    <ul>
                        <li>Carry mix of cash and cards</li>
                        <li>Research currency exchange rates</li>
                        <li>Keep emergency cash separate</li>
                        <li>Use local ATMs for better rates</li>
                        <li>Inform bank of travel dates</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                <div class="info-card">
                    <h4>🎒 Packing Essentials</h4>
                    <ul>
                        <li>Universal power adapter</li>
                        <li>Portable charger</li>
                        <li>First-aid kit</li>
                        <li>Comfortable walking shoes</li>
                        <li>Weather-appropriate clothing</li>
                        <li>Reusable water bottle</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown("""
                <div class="info-card">
                    <h4>📱 Stay Connected</h4>
                    <ul>
                        <li>Download offline maps</li>
                        <li>Get local SIM or eSIM</li>
                        <li>Save important numbers offline</li>
                        <li>Share itinerary with family</li>
                        <li>Download translation apps</li>
                    </ul>
                </div>
                """, unsafe_allow_html=True)
    
    else:
        # Welcome screen with features
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("""
                <div class="info-card">
                    <h2>🌟 Why Choose SafarSathi?</h2>
                    <p>Your AI-powered travel companion that creates personalized itineraries in seconds!</p>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
                <div class="info-card">
                    <h3>✨ Smart Features</h3>
                    <span class="feature-badge">AI-Powered Planning</span>
                    <span class="feature-badge">Budget Optimization</span>
                    <span class="feature-badge">Local Insights</span>
                    <span class="feature-badge">Day-by-Day Breakdown</span>
                    <span class="feature-badge">Hotel Recommendations</span>
                    <span class="feature-badge">Food Suggestions</span>
                    <span class="feature-badge">Safety Tips</span>
                    <span class="feature-badge">Multiple Export Formats</span>
                </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
                <div class="info-card">
                    <h3>🚀 How It Works</h3>
                    <ol>
                        <li><strong>Choose Your Destination</strong> - Tell us where you want to go</li>
                        <li><strong>Set Your Preferences</strong> - Budget, dates, interests, and travel style</li>
                        <li><strong>Get Your Itinerary</strong> - AI generates a detailed, personalized plan</li>
                        <li><strong>Download & Go</strong> - Export in multiple formats and start your adventure!</li>
                    </ol>
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("""
                <div class="info-card">
                    <h3>🎯 Perfect For</h3>
                    <ul>
                        <li>🏝️ Weekend Getaways</li>
                        <li>🌍 International Adventures</li>
                        <li>👨‍👩‍👧‍👦 Family Vacations</li>
                        <li>💑 Romantic Escapes</li>
                        <li>🎒 Solo Travel</li>
                        <li>👥 Group Trips</li>
                    </ul>
                </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("""
            <div style="text-align: center; padding: 2rem; color: white;">
                <h3>👈 Start planning your dream trip by filling out the form in the sidebar!</h3>
                <p>SafarSathi makes travel planning effortless, intelligent, and fun.</p>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
