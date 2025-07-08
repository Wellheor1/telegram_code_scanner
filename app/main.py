from fastapi import FastAPI


app = FastAPI()


@app.get("/", tags=["Приложение"])
async def root():
    return {"ok": True, "message": "hello world"}
