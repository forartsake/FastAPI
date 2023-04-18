import asyncio
from src.routers import router
from src.app import App

app = App(title="Users Stats")
app.include_router(router)


@app.on_event('startup')
async def startup():
    loop = asyncio.get_running_loop()
    task = loop.create_task(app.pika_client.consume(loop))
    await task
