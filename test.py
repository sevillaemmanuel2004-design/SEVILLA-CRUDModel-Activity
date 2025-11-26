from fastapi import FastAPI, HTTPException, status
from sqlmodel import Session, select
from database import create_db_and_tables, engine
from models import Coffee, Tea, NonCaffeine
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

# ---------------- Coffee Endpoints ----------------
@app.get("/coffee")
async def get_all_coffee():
    with Session(engine) as session:
        statement = select(Coffee)
        results = session.exec(statement).all()
        return results

@app.post("/coffee")
async def create_coffee_endpoint(coffee: Coffee):
    with Session(engine) as session:
        session.add(coffee)
        session.commit()
        session.refresh(coffee)
        return f"Coffee '{coffee.name}' created."

@app.put("/coffee/{item_id}")
async def update_coffee_endpoint(item_id: int, coffee: Coffee):
    with Session(engine) as session:
        item = session.get(Coffee, item_id)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Coffee not found")
        item.name = coffee.name
        item.roast_level = coffee.roast_level
        item.price = coffee.price
        session.add(item)
        session.commit()
        session.refresh(item)
        return f"Coffee {item_id} updated."

@app.delete("/coffee/{item_id}")
async def delete_coffee_endpoint(item_id: int):
    with Session(engine) as session:
        item = session.get(Coffee, item_id)
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Coffee not found")
        session.delete(item)
        session.commit()
        return f"Coffee {item_id} deleted."

# ---------------- Tea Endpoints ----------------
@app.get("/tea")
async def get_all_tea():
    with Session(engine) as session:
        statement = select(Tea)
        return session.exec(statement).all()

@app.post("/tea")
async def create_tea_endpoint(tea: Tea):
    with Session(engine) as session:
        session.add(tea)
        session.commit()
        session.refresh(tea)
        return f"Tea '{tea.name}' created."

# ---------------- Non-Caffeine Endpoints ----------------
@app.get("/non_caffeine")
async def get_all_non_caffeine():
    with Session(engine) as session:
        statement = select(NonCaffeine)
        return session.exec(statement).all()

@app.post("/non_caffeine")
async def create_non_caffeine_endpoint(nc: NonCaffeine):
    with Session(engine) as session:
        session.add(nc)
        session.commit()
        session.refresh(nc)
        return f"Non-Caffeine drink '{nc.name}' created."
