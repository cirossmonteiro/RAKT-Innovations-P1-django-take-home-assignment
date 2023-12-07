import csv
import datetime as dt

from django.core.management.base import BaseCommand, CommandError
from main.models import FoodTruck


class Command(BaseCommand):
    help = "Load data from CSV file."

    def handle(self, *args, **options):
        with open("main/management/commands/food-truck-data.csv") as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)
            for row in reader:
                FoodTruck.objects.create(
                    location_id=row[0],
                    applicant=row[1],
                    facility_type=row[2],
                    cnn=int(row[3]),
                    location_description=row[4],
                    address=row[5],
                    # blocklot=row[6],
                    block=row[7],
                    lot=row[8],
                    permit=row[9],
                    status=row[10],
                    food_items=row[11],
                    x=None if row[12] == "" else float(row[12]),
                    y=None if row[13] == "" else float(row[13]),
                    latitude=float(row[14]),
                    longitude=float(row[15]),
                    schedule=row[16],
                    dayshours=row[17],
                    # NOISENT=row[18]
                    approved=None if row[19] == "" else dt.datetime.strptime(row[19], "%m/%d/%Y %I:%M:%S %p"),
                    received=dt.date.fromisoformat(row[20]),
                    prior_permit=row[21] == "1",
                    expiration_date=None if row[22] == "" else dt.datetime.strptime(row[22], "%m/%d/%Y %I:%M:%S %p"),
                    # location=row[23]
                    fire_prevention_districts=None if row[24] == "" else int(row[24]),
                    police_districts=None if row[25] == "" else int(row[25]),
                    supervisor_districts=None if row[26] == "" else int(row[26]), 
                    zip_code=None if row[27] == "" else int(row[27]),
                    neighborhoods_old=None if row[28] == "" else int(row[28])
                )