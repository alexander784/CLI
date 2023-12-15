from database import Session, hiker

def create_hiker_profile():

    session = session()

    name = input("Alex")
    contact_info = input("07464")
    emergency_contact = input("123")
    preferences = input("great")

    ##Create hew hiker profile

    new_hiker = hiker(
        name=name,
        contact_info = contact_info,
        emergency_contact=emergency_contact,
        preferences=preferences
    )

    session.add(new_hiker)
    session.commit()

