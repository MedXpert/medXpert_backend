# Generated by Django 4.0.4 on 2022-06-11 15:26

from django.db import migrations

from django.contrib.gis.geos import Point
from json import loads
from csv import reader
from pathlib import Path

def seed_data(apps, schema_editor):
    HealthCareFacility = apps.get_model('api', 'HealthCareFacility')

    parse = lambda x: loads(x) if (x is not None) and (x != "") else None

    file_name = "health_facility.csv"
    relative_file_path = Path(__file__).parents[2] / file_name
    with open(relative_file_path) as f:
        rows = reader(f)
        i = -1
        for row in rows:
            i += 1
            print("|||||||||||||||||||||||||||||||||||||||||||", i)
            print(row)
            if i == 0: continue

            coord = parse(row[0])

            HealthCareFacility(
                name=row[7],
                address=row[4],
                phoneNumbers=parse(row[9]),
                faxNumbers=parse(row[5]),
                website=row[13],
                imageGallaryLinks=parse(row[10]),
                foundedIn=row[6],
                numberOfEmployeesRange=parse(row[8]),
                source_addedBy=row[11],
                source_identifier=row[12],
                verificationIndexPer10=int(row[3]),
                # 900...
                GPSCoordinates=Point(
                    coord[0], coord[1], srid=4326) if coord else None,
                facility_type="Health Care"
            ).save()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data)
    ]
