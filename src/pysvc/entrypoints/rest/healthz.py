"""Rest handler for health checks"""

from fastapi import APIRouter, status
from pydantic import BaseModel

router = APIRouter(
    prefix="/healthz",
    tags=["health"]
)

class LivenessCheckResponse(BaseModel):
    """Response model for Liveness check results"""

    status: str = "OK"

@router.get(
    "/live",
    summary="Perform liveness check",
    status_code=status.HTTP_200_OK,
    response_model=LivenessCheckResponse
)
def get_health() -> LivenessCheckResponse:
    """
    ## Perform a health check

    Returns:
        : Return JSON response with the health check status
    """
    return LivenessCheckResponse(status="OK")


