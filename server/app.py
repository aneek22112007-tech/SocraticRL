from openenv_core.env_server import create_fastapi_app
from server.environment import SocraticEnvironment
from models import SocraticAction, SocraticObservation

app = create_fastapi_app(SocraticEnvironment, SocraticAction, SocraticObservation)

# Add health check endpoint for HuggingFace Space
@app.get("/health")
async def health_check():
    """Health check endpoint for container readiness"""
    return {"status": "healthy", "service": "socratic-rl"}

@app.get("/")
async def root():
    """Root endpoint with basic info"""
    return {
        "name": "SocraticRL Environment",
        "description": "RL environment for training LLMs to use Socratic questioning",
        "docs": "/docs",
        "health": "/health"
    }
