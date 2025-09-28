from fastapi import FastAPI
from auth_routes import auth_router
from order_routes import order_router
app = FastAPI()

@app.get("/ping")
async def ping():
    return {"ping": "pong!"}

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(order_router,prefix="/order",tags=["order"])