from sqlmodel import Session
from database import create_db_and_tables, engine
from models import Coffee, Tea, NonCaffeine

def create_coffee(_name, _roast, _price):
    with Session(engine) as session:
        coffee = Coffee(name=_name, roast_level=_roast, price=_price)
        session.add(coffee)
        session.commit()

def create_tea(_name, _type, _origin, _price):
    with Session(engine) as session:
        tea = Tea(name=_name, type=_type, origin=_origin, price=_price)
        session.add(tea)
        session.commit()

def create_non_caffeine(_name, _category, _desc, _price):
    with Session(engine) as session:
        nc = NonCaffeine(name=_name, category=_category, description=_desc, price=_price)
        session.add(nc)
        session.commit()

def main():
    create_db_and_tables()

    # Add some sample drinks
    create_coffee("Espresso", "Dark", 4.50)
    create_coffee("Latte", "Medium", 5.00)
    create_tea("Chamomile", "Herbal", "Egypt", 3.25)
    create_tea("Jasmine Green", "Green", "China", 3.75)
    create_non_caffeine("Lemonade", "Juice", "Fresh lemons", 2.99)
    create_non_caffeine("Chocolate Milk", "Milk-based", "Rich cocoa", 3.50)

if __name__ == "__main__":
    main()
