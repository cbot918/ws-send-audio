from fastapi import FastAPI, WebSocket,WebSocketDisconnect

app = FastAPI()

# WebSocket route for receiving audio data
@app.websocket("/audio")
async def audio_websocket(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            audio_data = await websocket.receive_bytes()
            print(audio_data)
            # Process the audio data as needed (e.g., save to a file, perform analysis)
    except WebSocketDisconnect:
        print("error")
        pass