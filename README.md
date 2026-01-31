# AI-PBX Microservice

A high-concurrency audio ingestion service built with FastAPI.

## Key Features
* **Low Latency:** Responds in < 50ms using asynchronous background tasks.
* **The Twist:** Detects and logs sequence gaps in audio packets.
* **Fault Tolerance:** Implements Exponential Backoff for flaky AI API calls.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Start server: `uvicorn main:app --reload`
3. Test via Swagger UI: `http://127.0.0.1:8000/docs`
