from pydantic import BaseModel

class AudioPacket(BaseModel):
    sequence: int
    data: str  # Base64 audio string
    timestamp: float