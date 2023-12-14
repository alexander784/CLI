from database import Session, equipment

def manage_equipment():

    session = Session()

    new_equipment = equipment(name="Hiking Boots", condition="Good")

    session.add(new_equipment)


    

    