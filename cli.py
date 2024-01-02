import click
from database import initialize_database
from trip_planning import plan_trip
from equipment import manage_equipment

@click.group()
def main():
    pass

@main.command()
def init_db():
    initialize_database()

    while True:
        print("\nHikers Management System\n")
        print("1. Create Hiker Profile")
        print("2. Create Equipment Entry")
        print("3. Plan Trip")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            name = input("Enter hiker's name: ")
            contact_info = input("Enter contact information: ")
            emergency_contact = input("Enter emergency contact: ")
            create_hiker(name, contact_info, emergency_contact)

        elif choice == '2':
            name = input("Enter equipment name: ")
            condition = input("Enter equipment condition: ")
            create_equipment(name, condition)

        elif choice == '3':
            trip_name = input("Enter trip name: ")
            hikers = [int(id) for id in input("Enter hiker IDs (comma-separated): ").split(',')]
            plan_trip(trip_name, hikers)

        elif choice == '4':
            print("Exiting Hikers Management System.")
            break

        else:
            print("Invalid choice. Please enter a valid option.")



@main.command()
def plan_trip_cmd():
    plan_trip()

@main.command()
def manage_equipment_cmd():
    manage_equipment()

#     if __name__ == "__main__":
#         main()

    







