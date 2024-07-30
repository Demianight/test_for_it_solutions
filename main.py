from contextlib import asynccontextmanager
from fastapi import FastAPI

from database import database, models
from logs import logger_setup
import announcements
import users


@asynccontextmanager
async def lifespan(app: FastAPI):
    models.Base.metadata.create_all(bind=database.engine)
    logger_setup()
    yield


app = FastAPI(lifespan=lifespan)


app.include_router(users.router)
app.include_router(announcements.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
