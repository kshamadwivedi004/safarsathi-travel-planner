# ✈️ SafarSathi - AI-Powered Travel Planner

Your complete AI travel planning companion with personalized itineraries, premium UI, and intelligent recommendations.

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Configure API key in .env file
GROQ_API_KEY=your_key_here

# 3. Run the application
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## 📁 Project Structure

```
SafarSathi/
├── app.py                  # Main Streamlit application (All-in-one)
├── streamlit_custom.css    # Premium styling and animations
├── requirements.txt        # Python dependencies
├── .env                    # API key configuration
├── .streamlit/             # Streamlit configuration
│   ├── config.toml        # Theme and settings
│   └── secrets.toml       # Cloud deployment secrets
└── Documentation/          # Setup guides
    ├── API_KEY_SETUP.md
    ├── QUICK_START_DOCS.md
    └── PROJECT_STRUCTURE.md
```

## ✨ Features

### 🎯 Smart AI Planning
- **Personalized Itineraries** - Day-by-day detailed plans based on your preferences
- **Real Recommendations** - Actual hotels, restaurants, attractions with names and prices
- **Transport Options** - Complete flight and train details with timings and booking platforms
- **Budget Breakdown** - Detailed cost analysis for accommodation, food, activities, and transport
- **Multi-Currency Support** - 10+ currencies including USD, EUR, GBP, INR, JPY, AUD, etc.

### 🎨 Premium User Interface
- **Animated Header** - Floating logo with scrolling feature highlights
- **Gradient Design** - Beautiful purple-pink backgrounds with black sidebar
- **Organized Layout** - Clean sections with expandable forms
- **Responsive Design** - Works perfectly on desktop and mobile

### 📊 Travel Management
- **Trip History** - Track all your planned trips
- **Multiple Exports** - Download as TXT, Markdown, or JSON
- **Travel Tips** - Essential packing, safety, and money advice
- **Session Persistence** - Your data stays during the session

### 🌍 Comprehensive Planning
- **Flight Recommendations** - Real airlines with flight numbers and timings
- **Train Options** - Actual train services with complete schedules (India, Europe, Japan, USA)
- **Accommodation** - 3-5 hotel options with pricing and locations
- **Food & Dining** - Restaurant recommendations with specific dishes
- **Local Transport** - Metro, taxi, and ride-sharing app details
- **Safety Tips** - Emergency numbers, health advice, and local customs
- **Packing Guide** - Weather-based suggestions and essential items

## 🛠️ Setup Guide

### 1. Prerequisites
- Python 3.8 or higher
- pip package manager
- Internet connection for AI API

### 2. Installation

```bash
# Clone or download the project
cd SafarSathi-main

# Install required packages
pip install -r requirements.txt
```

### 3. Configure API Key

**Option A - Local Development:**
1. Visit https://console.groq.com/keys
2. Create a free account (no credit card required)
3. Generate a new API key
4. Open `.env` file and add:
   ```env
   GROQ_API_KEY=your_actual_key_here
   ```

**Option B - Streamlit Cloud Deployment:**
1. Go to your app settings in Streamlit Cloud
2. Click "Secrets" in sidebar
3. Add:
   ```toml
   GROQ_API_KEY = "your_actual_key_here"
   ```

### 4. Run Application

```bash
streamlit run app.py
```

Visit `http://localhost:8501` in your browser.

## 🎯 Technology Stack

- **Framework**: Streamlit - Fast web app framework
- **AI Model**: GROQ API with LLaMA 3.3 70B Versatile
- **AI Framework**: LangChain for prompt management
- **Language**: Python 3.8+
- **Styling**: Custom CSS with animations

## 💡 How to Use

1. **Enter Journey Details**
   - Origin city (where you're traveling from)
   - Destination city (where you want to go)
   - Travel dates (start and end)
   - Preferred currency

2. **Customize Your Trip**
   - Number of travelers
   - Travel style (Budget Backpacker to Luxury Traveler)
   - Accommodation preference (Hotel, Hostel, Airbnb, etc.)

3. **Select Interests**
   - Choose from 12+ categories
   - Add custom interests
   - Multiple selections allowed

4. **Set Your Budget**
   - Budget per person in your chosen currency
   - Automatic total calculation

5. **Generate Itinerary**
   - Click "Generate My Itinerary"
   - Wait for AI to create your personalized plan
   - Review detailed recommendations

6. **Download & Share**
   - Export as Text, Markdown, or JSON
   - Save trip to history
   - Access travel tips

## 🌟 Key Highlights

### Intelligent AI Generation
- Real train names with actual schedules (Rajdhani, Shatabdi, Eurostar, Shinkansen, Amtrak)
- Specific flight options with airline names and numbers
- Actual hotel names with locations and pricing
- Real restaurant recommendations with signature dishes
- Verified information that can be looked up online

### Comprehensive Itineraries Include
- Transportation from origin to destination (flights + trains)
- Day-by-day activity schedule with timings
- Hotel recommendations (3-5 options)
- Food suggestions (breakfast, lunch, dinner)
- Local transportation guide
- Complete budget breakdown
- Return journey options
- Local tips and hidden gems
- Safety and health information
- Packing suggestions

## 🎨 Customization

### Change Theme Colors

Edit `streamlit_custom.css`:
```css
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #your-color-1, #your-color-2);
}
```

### Modify AI Behavior

Edit prompts in `app.py` (lines 130-240):
```python
itinerary_prompt = ChatPromptTemplate.from_messages([
    ("system", "Your custom instructions here..."),
    ("human", "Your custom request here...")
])
```

### Adjust Currency Options

Edit currency list in `app.py` (lines 406-417):
```python
currency_options = {
    "Your Currency": ("CODE", "Symbol"),
    # Add more currencies
}
```

## 📖 Documentation

- **[API_KEY_SETUP.md](API_KEY_SETUP.md)** - Detailed API key setup guide
- **[QUICK_START_DOCS.md](QUICK_START_DOCS.md)** - Getting started quickly
- **[PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md)** - Code organization guide

## 🚀 Deployment

### Deploy to Streamlit Cloud (Free)

1. Push code to GitHub
2. Visit https://share.streamlit.io/
3. Connect your repository
4. Add GROQ_API_KEY in Secrets
5. Deploy!

### Deploy to Other Platforms

The app can also be deployed to:
- Heroku
- Railway
- AWS/GCP/Azure
- Any platform supporting Python and Streamlit

## 🔧 Troubleshooting

### API Key Issues
- Ensure key starts with `gsk_`
- Check `.env` file has no extra spaces
- Verify key is active at https://console.groq.com/

### Import Errors
```bash
pip install --upgrade streamlit langchain langchain-groq
```

### CSS Not Loading
- Check `streamlit_custom.css` exists in project root
- Restart Streamlit app after CSS changes

## 📝 Code Organization

The [`app.py`](app.py:1) is organized into clear sections:
- **IMPORTS** - All required libraries
- **CONFIGURATION** - Page setup and environment
- **DATA STRUCTURES** - Type definitions
- **SESSION STATE** - State management
- **STYLING** - CSS loading functions
- **AI INITIALIZATION** - LLM setup
- **PROMPT TEMPLATE** - AI instructions
- **CORE FUNCTIONS** - Business logic
- **MAIN APPLICATION** - UI and interaction
- **ENTRY POINT** - Startup code

## 🙏 Credits

Built with:
- [Streamlit](https://streamlit.io/) - Web framework
- [LangChain](https://www.langchain.com/) - AI framework
- [GROQ](https://groq.com/) - Fast AI inference
- [LLaMA 3.3](https://ai.meta.com/llama/) - Language model

## 📄 License

© 2026 SafarSathi. All rights reserved.

## 🤝 Support

For issues or questions:
1. Check documentation files
2. Verify API key setup
3. Check https://status.groq.com/ for service status

---

**Start planning your perfect trip today!** ✈️🗺️

Made with ❤️ for travelers around the world 🌍
