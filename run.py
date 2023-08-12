from fastapi import FastAPI
from routes.notes import notes_router
import uvicorn

app = FastAPI()
app.include_router(notes_router)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
