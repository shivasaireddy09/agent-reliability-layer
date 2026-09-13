from fastapi import FastAPI

app = FastAPI(title="AI Agent Reliability Layer")


@app.get("/health")
async def health_check():
    return {"status": "ok"}
