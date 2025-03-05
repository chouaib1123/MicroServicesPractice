import subprocess
from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.Routers.ProductRouter import router
from app.Routers.OrderRouter import  order_router



@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup event
    try:
        subprocess.check_call(["alembic", "upgrade", "head"])  # Run Alembic migrations
        yield  # The app will run normally after this point
    except subprocess.CalledProcessError as e:
        print(f"Error running migrations: {e}")
        yield  # Even if migrations fail, let the app continue, you can handle errors better if necessary
    finally:
        # Shutdown event (if any cleanup needed)
        print("App is shutting down.")

app = FastAPI(lifespan=lifespan)

app.include_router(router)
app.include_router(order_router)
