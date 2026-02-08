# SafarSathi - AI Travel Planner

SafarSathi is an AI-powered travel planning application that helps users create personalized travel itineraries. Using advanced language models, it provides detailed day-by-day plans, accommodation recommendations, food suggestions, and local tips.

## Features

- 🗺️ Detailed day-by-day itineraries
- 🏨 Hotel recommendations within budget
- 🍽️ Food and restaurant suggestions
- 🚗 Transportation options
- 💰 Budget planning and cost breakdown
- 📱 User-friendly interface
- 📥 Downloadable itineraries

## Setup

1. Clone the repository:
```bash
git clone https://github.com/kshamadwivedi004/safarsathi-travel-planner.git
cd safarsathi-travel-planner
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your GROQ API key:
   
   **⚠️ IMPORTANT: You need a FREE GROQ API key to use this application!**
   
   a. Copy the example environment file:
   ```bash
   cp .env.example .env
   ```
   
   b. Get your free API key from: **https://console.groq.com/keys**
      - Sign up (free, no credit card required)
      - Create a new API key
      - Copy the key (starts with `gsk_`)
   
   c. Edit the `.env` file and replace `your_groq_api_key_here` with your actual key:
   ```env
   GROQ_API_KEY=gsk_your_actual_api_key_here
   ```
   
   📖 **For detailed setup instructions, see [`API_KEY_SETUP.md`](API_KEY_SETUP.md)**

4. Run the application:
```bash
streamlit run app.py
```

## Usage

1. Enter your destination city
2. Specify your interests (comma-separated)
3. Select trip dates
4. Enter group details (number of men, women, others)
5. Set budget per person
6. Click "Generate Itinerary"

## Deployment

The application can be deployed on:
- Streamlit Cloud
- AWS
- Google Cloud Platform

## Technologies Used

- Python
- Streamlit
- LangChain
- Groq API


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For any queries or support, please open an issue in the GitHub repository. 
