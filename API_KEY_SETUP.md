# 🔑 API Key Setup Guide for SafarSathi

## Quick Setup (5 minutes)

Your SafarSathi application needs a **GROQ API key** to generate travel itineraries. Don't worry - it's completely **FREE** and takes just a few minutes!

---

## Step 1: Get Your Free GROQ API Key

1. **Visit GROQ Console**: https://console.groq.com/keys

2. **Sign Up or Log In**:
   - Use your email or sign in with Google/GitHub
   - It's completely free - no credit card required!

3. **Create API Key**:
   - Click "Create API Key"
   - Give it a name (e.g., "SafarSathi")
   - Copy the key (it will start with `gsk_`)

---

## Step 2: Configure Your Application

1. **Open the `.env` file** in this project directory

2. **Replace the placeholder** with your actual key:
   ```env
   GROQ_API_KEY=gsk_your_actual_key_here
   ```

3. **Save the file**

---

## Step 3: Restart the Application

1. **Stop the current application** (if running):
   - Press `Ctrl+C` in the terminal

2. **Start it again**:
   ```bash
   streamlit run app.py
   ```

3. **You're all set!** 🎉

---

## Troubleshooting

### ❌ "Invalid API Key" Error

**Solution:**
- Make sure you copied the entire key (starts with `gsk_`)
- No extra spaces before or after the key
- Save the `.env` file after editing
- Restart the application

### ❌ "Rate Limit" Error

**Solution:**
- GROQ has generous free limits
- Wait a minute and try again
- Check your usage at: https://console.groq.com/usage

### ❌ Application Won't Start

**Solution:**
- Make sure all dependencies are installed: `pip install -r requirements.txt`
- Check that Python 3.8+ is installed
- Verify the `.env` file is in the same directory as `app.py`

---

## Why GROQ?

✅ **Free** - No credit card needed  
✅ **Fast** - Super quick response times  
✅ **Powerful** - Uses advanced AI models  
✅ **Reliable** - Great uptime and support  

---

## Security Notes

🔒 **Keep your API key private**:
- Never commit the `.env` file to public repositories
- Don't share your API key with others
- Regenerate if you accidentally expose it

🔒 **The `.env` file is already in `.gitignore`** (if you're using Git)

---

## Need Help?

- **GROQ Documentation**: https://console.groq.com/docs
- **GROQ Support**: https://console.groq.com/support
- **Check GROQ Status**: https://status.groq.com/

---

**Once configured, SafarSathi will generate amazing, detailed travel itineraries instantly!** ✈️🌍
