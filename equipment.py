from database import Session,Equipment

def manage_equipment():
    session = Session()

      ##Add new equipment
    new_equipment = Equipment(name="Hiking Boots", condition="Good")
    session.add(new_equipment)

    session.commit()
    session.close()

    




    

    