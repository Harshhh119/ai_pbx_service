# AI-PBX Microservice

A high-concurrency audio ingestion service built with FastAPI.

##Methodology
This service is built to handle the "three pillars" of real-time backend engineering.
Ultra-Low Latency: Uses FastAPI BackgroundTasks to ensure responses are returned in < 50ms, decoupling ingestion from heavy AI processing.
Sequence Integrity (The Twist): Implements state-tracking logic to detect and log dropped or out-of-order audio packets in real-time.
Fault Tolerance: To handle a 25% failure rate in downstream AI services, I implemented Exponential Backoff ($wait = 2^{attempt}$) to ensure eventual consistency without crashing.

## Key Features
* **Low Latency:** Responds in < 50ms using asynchronous background tasks.
* **The Twist:** Detects and logs sequence gaps in audio packets.
* **Fault Tolerance:** Implements Exponential Backoff for flaky AI API calls.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Start server: `uvicorn main:app --reload`
3. Test via Swagger UI: `http://127.0.0.1:8000/docs`
