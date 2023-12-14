from database import Session, Trip, hiker

def plan_trip():

    session = Session()

    #Create new trip
    new_trip = Trip(name="Example Trip", destination="Mountain X", date="2023-12-31")
    session.add(new_trip)


    session.commit()
    session.close()
