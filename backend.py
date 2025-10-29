import os
import base64
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import google.generativeai as genai
from PIL import Image
import io
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

class ImageRequest(BaseModel):
    image_data: str  

@app.get("/models")
async def list_models():
    """Debug endpoint to list available models"""
    try:
        models = genai.list_models()
        model_list = [m.name for m in models if 'generateContent' in m.supported_generation_methods]
        return {"available_models": model_list}
    except Exception as e:
        return {"error": str(e)}

SYSTEM_PROMPT = """
You are an expert in Mathematics, Physics, and Chemistry. Analyze the provided image and provide a well-structured response.

FORMAT YOUR RESPONSE EXACTLY AS FOLLOWS:

📚 **SUBJECT:** [Mathematics/Physics/Chemistry]

📝 **PROBLEM:**
[Write the equation or problem statement in LaTeX format using $$...$$]

💡 **SOLUTION:**

**Step 1:** [First step with explanation]
$$[equation if applicable]$$

**Step 2:** [Second step with explanation]
$$[equation if applicable]$$

**Step 3:** [Continue as needed...]
$$[equation if applicable]$$

✅ **FINAL ANSWER:**
$$[final answer in LaTeX]$$

📖 **EXPLANATION:**
[Provide a clear explanation of the concepts, laws, or principles used. For Physics/Chemistry, include relevant formulas, constants, and units.]

CRITICAL RULES:
- Use ONLY $$...$$ for mathematical expressions (double dollar signs)
- NEVER use single dollar signs like $x$ in explanatory text
- When referring to variables in text, write them as: "the variable x" or "the amplitude A" (no dollar signs)
- When referring to values in text, write them as: "0.3" not "$0.3$"
- Keep all mathematical notation inside $$...$$ blocks only
- Number each step clearly
- Provide pedagogical explanations without dollar signs in regular text
"""

@app.post("/analyze")
async def analyze_image(request: ImageRequest):
    try:
        # Convert base64 to image bytes
        image_bytes = base64.b64decode(request.image_data.split(",")[1])
        image = Image.open(io.BytesIO(image_bytes))
        
        # Use the latest available Gemini model with vision support
        model_names = [
            'models/gemini-2.5-flash',
            'models/gemini-2.0-flash',
            'models/gemini-flash-latest',
            'models/gemini-2.5-pro'
        ]
        
        last_error = None
        for model_name in model_names:
            try:
                model = genai.GenerativeModel(model_name)
                response = model.generate_content([SYSTEM_PROMPT, image])
                
                # Ensure LaTeX formatting
                solution = response.text
                solution = solution.replace("\\(", "$").replace("\\)", "$")
                
                return {"solution": solution}
            except Exception as e:
                last_error = e
                continue
        
        # If all models failed, raise the last error
        raise last_error
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)