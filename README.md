# SciSolve - AI Science Solver

AI-powered solver for Math, Physics, and Chemistry problems using Google Gemini Vision API.

## Features

- 🎨 Draw equations on canvas
- 🤖 AI-powered problem solving
- 📚 Supports Math, Physics, and Chemistry
- 📝 Step-by-step solutions
- 💾 Save and view history
- 🌓 Dark mode support

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript, MathJax
- **Backend**: Python, FastAPI, Google Gemini API
- **AI**: Google Gemini 2.5 Flash Vision Model

## Local Development

### Backend Setup

```bash
cd MiniProjectSem4
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Create .env file with your Gemini API key
echo "GEMINI_API_KEY=your_api_key_here" > .env

# Run backend
python backend.py
```

Backend runs on: http://localhost:8000

### Frontend Setup

```bash
# Serve frontend with Python
python3 -m http.server 3000
```

Frontend runs on: http://localhost:3000

## Deployment

### Backend Deployment (Render/Railway)

1. Create account on [Render.com](https://render.com) or [Railway.app](https://railway.app)
2. Create new Web Service
3. Connect your GitHub repository
4. Set environment variable: `GEMINI_API_KEY=your_key`
5. Deploy!

### Frontend Deployment (Netlify/Vercel)

1. Create account on [Netlify](https://netlify.com) or [Vercel](https://vercel.com)
2. Drag and drop `index.html` or connect GitHub repo
3. Update the API URL in `index.html` to your deployed backend URL
4. Deploy!

## Environment Variables

- `GEMINI_API_KEY`: Your Google Gemini API key
- `PORT`: Port for backend (auto-set by hosting platforms)

## API Endpoints

- `POST /analyze`: Analyze drawn equation image
- `GET /models`: List available Gemini models (debug)

## License

MIT License - Feel free to use for educational purposes!

## Made By

Pranav and Team
