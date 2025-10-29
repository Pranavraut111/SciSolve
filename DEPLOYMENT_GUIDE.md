# 🚀 SciSolve Deployment Guide

## Quick Deployment Steps

### Option 1: Deploy Backend to Render (Recommended - Free)

1. **Create GitHub Repository**
   ```bash
   cd /Users/pranavraut/Desktop/MiniProjectSem4
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   ```

2. **Deploy to Render**
   - Go to [render.com](https://render.com)
   - Sign up/Login with GitHub
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure:
     - **Name**: scisolve-backend
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `uvicorn backend:app --host 0.0.0.0 --port $PORT`
   - Add Environment Variable:
     - Key: `GEMINI_API_KEY`
     - Value: `AIzaSyCXwWi1EIf1o3Orf7I89YoIGkJe4JslSPs`
   - Click "Create Web Service"
   - Wait 5-10 minutes for deployment
   - Copy your backend URL (e.g., `https://scisolve-backend.onrender.com`)

### Option 2: Deploy Backend to Railway

1. **Deploy to Railway**
   - Go to [railway.app](https://railway.app)
   - Sign up/Login with GitHub
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Add Environment Variable:
     - `GEMINI_API_KEY=AIzaSyCXwWi1EIf1o3Orf7I89YoIGkJe4JslSPs`
   - Railway auto-detects Python and deploys
   - Copy your backend URL

---

### Deploy Frontend to Netlify (Easiest)

1. **Update API URL in index.html**
   - Open `index.html`
   - Find line: `const response = await fetch('http://localhost:8000/analyze', {`
   - Replace with: `const response = await fetch('https://YOUR-BACKEND-URL.onrender.com/analyze', {`
   - Save the file

2. **Deploy to Netlify**
   - Go to [netlify.com](https://netlify.com)
   - Sign up/Login
   - Drag and drop your `index.html` file to Netlify
   - OR: Click "Add new site" → "Import from Git" → Connect GitHub repo
   - Your site is live! (e.g., `https://scisolve-ai.netlify.app`)

### Alternative: Deploy Frontend to Vercel

1. **Update API URL** (same as above)

2. **Deploy to Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Sign up/Login with GitHub
   - Click "New Project"
   - Import your GitHub repository
   - Click "Deploy"
   - Your site is live!

---

## 📝 Post-Deployment Checklist

- [ ] Backend deployed and running
- [ ] Backend URL copied
- [ ] Frontend `index.html` updated with backend URL
- [ ] Frontend deployed
- [ ] Test the live application
- [ ] Share your live URL!

---

## 🔧 Troubleshooting

### Backend Issues

**Error: "Application failed to start"**
- Check if `requirements.txt` is present
- Verify Python version in `runtime.txt`
- Check environment variable `GEMINI_API_KEY` is set

**Error: "Port already in use"**
- Hosting platforms auto-assign ports via `$PORT` variable
- Make sure backend.py uses `os.getenv("PORT", 8000)`

### Frontend Issues

**Error: "Failed to fetch" or CORS error**
- Update the API URL in `index.html` to your deployed backend URL
- Make sure backend has CORS enabled (already configured)

**Math equations not rendering**
- MathJax CDN might be slow, wait a few seconds
- Check browser console for errors

---

## 🎉 Your App is Live!

Once deployed, you'll have:
- **Backend**: `https://your-app.onrender.com`
- **Frontend**: `https://your-app.netlify.app`

Share your live app with friends and teachers! 🚀

---

## 💰 Cost

- **Render Free Tier**: 750 hours/month (enough for demos)
- **Railway Free Tier**: $5 credit/month
- **Netlify Free Tier**: Unlimited static sites
- **Vercel Free Tier**: Unlimited static sites

All completely FREE for your project! 🎊
