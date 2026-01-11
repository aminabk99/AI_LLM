from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.chat import router as chat_router
from app.routes.ui import router as ui_router

app = FastAPI(
    title="AI-Built FastAPI Service",
    version="1.0.1",
    description="A minimal API generated and iterated by an AI coding agent running locally with Ollama.",
)

# Optional CORS (useful if you later serve UI separately)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Service is running", "try": ["/health", "/docs", "/chat", "/ui"]}

@app.get("/health")
def health():
    return {"status": "healthy"}

app.include_router(chat_router)
app.include_router(ui_router)

