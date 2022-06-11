from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from api.models import HealthCareFacility as hf

h = hf.objects.get(pk=71)
print(h, h.name, h.GPSCoordinates, h.id)


distance = 500
point = Point(38.76111384105613,9.043677387443639, srid=4326)
within_distance = hf.objects.filter(GPSCoordinates__distance_lte=(point,D(m=1000)))
sorted = within_distance.annotate(distance=Distance("GPSCoordinates", point)).order_by('distance')
near_5 = sorted[0:5]
print([(hcf.name, str(hcf.GPSCoordinates), hcf.id) for hcf in near_5])
