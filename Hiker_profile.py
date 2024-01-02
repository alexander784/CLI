from database import Session, hiker

def create_hiker_profile(name, contact_info,emergency_contact):

    session = session()
    ##Create hew hiker profile

    new_hiker = hiker(
        name=name,
        contact_info = contact_info,
        emergency_contact=emergency_contact,
    )

    session.add(new_hiker)
    session.commit()
    print(f"Hiker {name} added succesfully.")

