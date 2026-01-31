import asyncio
import httpx

async def run_test():
    url = "http://127.0.0.1:8000/v1/call/stream/test_call_001"
    
    # Test 1: Normal Packet
    print("Sending Packet 0...")
    async with httpx.AsyncClient() as client:
        await client.post(url, json={"sequence": 0, "data": "audio_data", "timestamp": 1.0})
    
    # Test 2: Skip a packet to trigger "The Twist"
    print("Sending Packet 2 (Skipping Packet 1)...")
    async with httpx.AsyncClient() as client:
        await client.post(url, json={"sequence": 2, "data": "audio_data", "timestamp": 2.0})

if __name__ == "__main__":
    asyncio.run(run_test())