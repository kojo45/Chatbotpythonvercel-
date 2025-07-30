
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.post("/api/chatbot")
async def chat(request: Request):
    data = await request.json()
    msg = data.get("message", "")
    return JSONResponse(content={"response": f"Vous avez dit: {msg}"})
