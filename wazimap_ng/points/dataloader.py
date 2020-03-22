from django.contrib.gis.geos import Point
from django.db import transaction

from . import models
from ..boundaries.models import GeographyBoundary


@transaction.atomic
def loaddata(name, category, iterable):

    datarows = []
    for idx, row in enumerate(iterable):

        try:
            if "longitude" not in row:
                print(f"Missing Longitude - skipping it.")
                continue

            if "latitude" not in row:
                print(f"Missing Latitude - skipping it.")
                continue

            if "name" not in row:
                print(f"Missing Name - skipping it.")
                continue

            location = row.pop("name")
            coordinates = Point(row.pop("longitude"), row.pop("latitude"))

            dd = models.Location(
                name=location, category=category,
                coordinates=coordinates, data=row
            )

            datarows.append(dd)

            if len(datarows) >= 10000:
                models.Location.objects.bulk_create(datarows, 1000)
                datarows = []
        except Exception:
            # TODO Add log to help user identify the problem
            continue

    models.Location.objects.bulk_create(datarows, 1000)
