from sqlmodel import Field, SQLModel

class Coffee(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    roast_level: str
    price: float

class Tea(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    type: str
    origin: str
    price: float

class NonCaffeine(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    category: str
    description: str | None = None
    price: float
