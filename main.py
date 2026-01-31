import asyncio
import random
from fastapi import FastAPI, BackgroundTasks, HTTPException
from models import AudioPacket

app = FastAPI()

# In-memory storage to track sequences
call_history = {}

async def call_ai_service(call_id: str, sequence: int):
    """Simulates AI service with 25% failure & Exponential Backoff"""
    delay = 1
    for attempt in range(4):
        try:
            if random.random() < 0.25:
                raise Exception("Provider Error")
            
            await asyncio.sleep(0.5)
            print(f" AI Success: Call {call_id} Packet {sequence}")
            return
        except Exception:
            print(f" AI Failed. Retrying in {delay}s...")
            await asyncio.sleep(delay)
            delay *= 2 

@app.post("/v1/call/stream/{call_id}")
async def handle_audio(call_id: str, packet: AudioPacket, background_tasks: BackgroundTasks):
  
    last_seq = call_history.get(call_id, -1)
    
    if packet.sequence != last_seq + 1:
        print(f" SEQUENCE GAP: Call {call_id} expected {last_seq + 1}, got {packet.sequence}")
    
    call_history[call_id] = packet.sequence


    background_tasks.add_task(call_ai_service, call_id, packet.sequence)
    
    return {"status": "accepted", "msg": "Processing in background"}