# SafarSathi ✈️ - AI-Powered Travel Planner

SafarSathi is an intelligent travel planning application that leverages AI to create personalized, detailed travel itineraries based on your preferences, budget, and interests.

![SafarSathi Banner](https://img.shields.io/badge/SafarSathi-Travel%20Planner-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-green?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

## 🌟 Features

- **AI-Powered Itineraries**: Generates comprehensive travel plans using LLM technology
- **Personalized Journey**: From origin to destination with complete travel details
- **Smart Budget Planning**: Optimized recommendations based on your budget
- **Multi-Currency Support**: Plan in USD, EUR, GBP, INR, JPY, and more
- **Real Recommendations**: 
  - Actual flight options with airlines and timings
  - Real train routes with complete schedules
  - Genuine hotel recommendations with pricing
  - Authentic restaurant and food suggestions
- **Day-by-Day Breakdown**: Detailed daily schedules with timing and costs
- **Travel Styles**: Choose from budget backpacker to luxury traveler
- **Multiple Export Formats**: Download as Text, Markdown, or JSON
- **Trip History**: Keep track of all your planned adventures
- **Safety & Tips**: Essential travel advice and local insights

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- GROQ API key (free from [console.groq.com](https://console.groq.com/keys))

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/kshamadwivedi004/safarsathi-travel-planner.git
   cd safarsathi-travel-planner
   ```

2. **Install dependencies**:
   ```bash
   pip install streamlit langchain-groq langchain-core python-dotenv
   ```

3. **Set up your API key**:
   - Visit [console.groq.com/keys](https://console.groq.com/keys)
   - Sign up for a free account
   - Generate a new API key
   - Create a `.env` file in the project root:
     ```
     GROQ_API_KEY=your_api_key_here
     ```

4. **Run the application**:
   ```bash
   streamlit run app.py
   ```

5. **Open your browser** and navigate to `http://localhost:8501`

## 📋 Usage

### Planning Your Trip

1. **Journey Details**:
   - Enter your origin city
   - Enter your destination city
   - Select start and end dates
   - Choose your preferred currency

2. **Traveler Preferences**:
   - Number of travelers
   - Travel style (Budget, Balanced, Luxury, etc.)
   - Accommodation type (Hotel, Hostel, Airbnb, etc.)

3. **Interests & Activities**:
   - Select from pre-defined interests
   - Add custom interests

4. **Budget Planning**:
   - Set budget per person
   - View total trip budget

5. **Generate**: Click "Generate My Itinerary" and let AI work its magic!

### Your Itinerary Includes

- **Flight & Rail Options**: Real airlines, trains with timings
- **Day-by-Day Schedule**: Complete itinerary with attractions and timing
- **Hotel Recommendations**: 3-5 actual hotels with pricing
- **Food & Dining**: Real restaurants and local cuisine suggestions
- **Local Transportation**: Metro, bus, taxi options with costs
- **Budget Breakdown**: Detailed expense categories
- **Return Journey**: Flight and train options back home
- **Local Tips**: Best times to visit, customs, hidden gems
- **Safety Information**: Emergency numbers, healthcare, scams to avoid
- **Packing Suggestions**: Weather-based recommendations

## 🛠️ Technical Stack

- **Frontend**: Streamlit
- **AI Model**: Llama 3.3 70B (via GROQ)
- **LLM Framework**: LangChain
- **Language**: Python 3.8+

## 📦 Dependencies

```python
streamlit
langchain-groq
langchain-core
python-dotenv
```

## 🎨 Customization

The application includes custom CSS styling in `streamlit_custom.css` for an enhanced user experience. You can modify this file to customize the appearance.

## 🔐 Environment Variables

Create a `.env` file with:

```env
GROQ_API_KEY=your_groq_api_key_here
```

For Streamlit Cloud deployment, add this key in the app's Secrets section.

## 🌍 Supported Currencies

- USD ($) - US Dollar
- EUR (€) - Euro
- GBP (£) - British Pound
- INR (₹) - Indian Rupee
- JPY (¥) - Japanese Yen
- AUD (A$) - Australian Dollar
- CAD (C$) - Canadian Dollar
- AED (د.إ) - UAE Dirham
- CNY (¥) - Chinese Yuan
- SGD (S$) - Singapore Dollar

## 📱 Export Options

Download your itinerary in multiple formats:
- **Plain Text** (.txt)
- **Markdown** (.md)
- **JSON** (.json)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Uses [GROQ](https://groq.com/) for fast AI inference
- Built with [Streamlit](https://streamlit.io/)
- Powered by [LangChain](https://langchain.com/)

## 📞 Contact

For questions or feedback, please open an issue on GitHub.

---

**Happy Travels with SafarSathi! ✈️🌍**
