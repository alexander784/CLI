from database import Session,Equipment

def manage_equipment( name, condition):
    session = Session()

      ##Add new equipment
    new_equipment = Equipment(name="name", condition="condition")
    session.add(new_equipment)
    session.commit()
    print(f"Equipment {name} added successfully.")

    




    

    