# 🚀 SafarSathi Deployment & Access Guide

## 📱 Accessing the Application

### Option 1: Run Locally (Recommended for Development)

1. **Open Terminal in Project Directory**
   ```bash
   cd c:\Users\vinit\Downloads\Safarsathi-main\Safarsathi-main
   ```

2. **Verify API Key is Configured**
   - Check that `.env` file exists with your GROQ API key
   - If not configured, see [API_KEY_SETUP.md](API_KEY_SETUP.md)

3. **Start the Application**
   ```bash
   python -m streamlit run app.py
   ```

4. **Access in Browser**
   - Streamlit will automatically open in your default browser
   - Or manually open: `http://localhost:8501`
   - The application is now running on your local machine!

### Option 2: Access via Network

If you want others on your local network to access:

1. **Run with Network Access**
   ```bash
   streamlit run app.py --server.address=0.0.0.0
   ```

2. **Find Your Local IP Address**
   - Windows: `ipconfig` (look for IPv4 Address)
   - Your IP might be something like: `192.168.1.100`

3. **Share the URL**
   - Share with others: `http://YOUR_IP:8501`
   - Example: `http://192.168.1.100:8501`

---

## ☁️ Deploy to Cloud (Free Options)

### Method 1: Streamlit Cloud (Recommended - Easiest & Free)

#### Prerequisites:
- GitHub account
- Your GROQ API key

#### Steps:

1. **Push to GitHub**
   ```bash
   # Initialize git if not already done
   git init
   
   # Add all files
   git add .
   
   # Commit
   git commit -m "SafarSathi AI Travel Planner - Ready for deployment"
   
   # Add your GitHub repository as remote
   git remote add origin https://github.com/kshamadwivedi004/safarsathi-travel-planner.git
   
   # Push to GitHub
   git push -u origin main
   ```

2. **Deploy to Streamlit Cloud**
   - Visit: https://share.streamlit.io/
   - Click "New app"
   - Connect your GitHub repository
   - Select:
     - Repository: `kshamadwivedi004/safarsathi-travel-planner`
     - Branch: `main`
     - Main file path: `app.py`
   
3. **Configure Secrets (API Key)**
   - In Streamlit Cloud dashboard, go to your app settings
   - Click "Secrets" section
   - Add your secret:
     ```toml
     GROQ_API_KEY = "gsk_your_actual_api_key_here"
     ```
   - Save and the app will automatically restart

4. **Access Your Deployed App**
   - Your app will be live at: `https://YOUR_APP_NAME.streamlit.app/`
   - Share this URL with anyone!

---

### Method 2: Render (Free Tier Available)

1. **Create `runtime.txt`**
   ```
   python-3.11.0
   ```

2. **Create `setup.sh`**
   ```bash
   mkdir -p ~/.streamlit/
   echo "\
   [server]\n\
   headless = true\n\
   port = $PORT\n\
   enableCORS = false\n\
   \n\
   " > ~/.streamlit/config.toml
   ```

3. **Deploy on Render**
   - Visit: https://render.com/
   - Create new "Web Service"
   - Connect your GitHub repository
   - Set:
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
   - Add environment variable: `GROQ_API_KEY`
   - Deploy!

---

### Method 3: Railway (Free Tier)

1. **Create `Procfile`**
   ```
   web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
   ```

2. **Deploy on Railway**
   - Visit: https://railway.app/
   - Click "Start a New Project"
   - Connect GitHub repo
   - Add environment variable `GROQ_API_KEY`
   - Deploy automatically!

---

## 🔧 Troubleshooting

### App Won't Start Locally

**Error: "ModuleNotFoundError"**
```bash
# Solution: Install dependencies
pip install -r requirements.txt
```

**Error: "GROQ API Key not configured"**
```bash
# Solution: Configure your API key
# 1. Copy .env.example to .env
cp .env.example .env

# 2. Edit .env and add your key
# GROQ_API_KEY=gsk_your_actual_key_here
```

**Port Already in Use**
```bash
# Solution: Use different port
streamlit run app.py --server.port=8502
```

### Deployment Issues

**Build Fails**
- Check `requirements.txt` has all dependencies
- Ensure Python version is compatible (3.8+)

**App Crashes After Deployment**
- Verify environment variables are set correctly
- Check logs in your hosting platform
- Ensure API key is valid

**Slow Performance**
- Free tiers have limited resources
- Consider upgrading to paid tier for production
- Optimize code and reduce API calls

---

## 📊 Monitoring Your App

### Local Development
```bash
# Run with debug mode
streamlit run app.py --logger.level=debug
```

### Production Monitoring

**Streamlit Cloud:**
- Access logs from app dashboard
- View metrics and usage statistics

**Other Platforms:**
- Check platform-specific logs
- Set up error tracking (e.g., Sentry)

---

## 🔐 Security Best Practices

1. **Never commit API keys to GitHub**
   - Use `.env` files (already in `.gitignore`)
   - Use platform secrets management

2. **Rotate API keys regularly**
   - Generate new key from https://console.groq.com/keys
   - Update in all deployment environments

3. **Monitor API usage**
   - Track usage in GROQ dashboard
   - Set up alerts for unusual activity

---

## 🌐 Sharing Your App

Once deployed, you can share your app URL:

### For Streamlit Cloud:
```
🌍 Live App: https://your-app-name.streamlit.app/
```

### Custom Domain (Optional):
- Most platforms support custom domains
- Configure DNS settings
- Add SSL certificate (usually free)

---

## 📈 Scaling & Optimization

### For Higher Traffic:

1. **Upgrade to Paid Tier**
   - More resources
   - Better performance
   - Custom domains

2. **Optimize Code**
   - Use `@st.cache_resource` for expensive operations
   - Minimize API calls
   - Implement rate limiting

3. **Load Balancing**
   - Deploy multiple instances
   - Use CDN for static assets

---

## 💡 Quick Commands Reference

```bash
# Start locally
streamlit run app.py

# Start with specific port
streamlit run app.py --server.port=8502

# Start with network access
streamlit run app.py --server.address=0.0.0.0

# Clear cache and restart
streamlit cache clear
streamlit run app.py

# Check Streamlit version
streamlit --version

# View Streamlit config
streamlit config show
```

---

## 🆘 Need Help?

- **Documentation**: https://docs.streamlit.io/
- **GROQ API**: https://console.groq.com/docs
- **GitHub Issues**: Open an issue in your repository
- **Streamlit Community**: https://discuss.streamlit.io/

---

## 🎉 You're All Set!

Your SafarSathi AI Travel Planner is now deployed and accessible. Start planning amazing trips! ✈️🌍
