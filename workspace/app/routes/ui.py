from fastapi import APIRouter
from fastapi.responses import FileResponse
from pathlib import Path

router = APIRouter(tags=["ui"])

# workspace/app/routes/ui.py -> workspace/app -> workspace/
WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
STATIC_DIR = WORKSPACE_ROOT / "app" / "static"

@router.get("/ui")
def ui_page():
    """
    Serves a simple ChatGPT-style web UI.
    """
    return FileResponse(STATIC_DIR / "ui.html")
