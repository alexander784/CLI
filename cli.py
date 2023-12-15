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

@main.command()
def plan_trip_cmd():
    plan_trip()

@main.command()
def manage_equipment_cmd():
    manage_equipment()

    if __name__ == "__main__":
        main()

    







