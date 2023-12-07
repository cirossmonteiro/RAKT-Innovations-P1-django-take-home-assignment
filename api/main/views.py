from rest_framework import viewsets

from main.models import FoodTruck
from main.serializers import FoodTruckSerializer

DX = 100
DY = 100
DLAT = 1
DLONG = 1
MAX_COUNT = 100000000

class FoodTruckViewSet(viewsets.ModelViewSet):
    queryset = FoodTruck.objects.all()
    serializer_class = FoodTruckSerializer

    def get_queryset(self):
        # scale of rectangle of search
        count = 1

        # data provided by user
        x = self.request.query_params.get('x')
        y = self.request.query_params.get('y')
        latitude = self.request.query_params.get('latitude')
        longitude = self.request.query_params.get('longitude')

        while count < MAX_COUNT: # "almost always" truthy
            queryset = FoodTruck.objects.all()

            if x is not None:
                x = float(x)
                # x-count*DX < x' < x+count*DX
                queryset = queryset.filter(x__gte=x-count*DX).filter(x__lte=x+count*DX)
            
            if y is not None:
                y = float(y)
                # y-count*DY < y' < y+count*DY
                queryset = queryset.filter(y__gte=y-count*DY).filter(y__lte=y+count*DY)
            
            if latitude is not None:
                latitude = float(latitude)
                # lat-count*DLAT < lat' < lat+count*DLAT
                queryset = queryset.filter(latitude__gte=latitude-count*DLAT).filter(latitude__lte=y+count*DLAT)
            
            if longitude is not None:
                longitude = float(longitude)
                # long-count*DLONG < long' < long+count*DLONG
                queryset = queryset.filter(longitude__gte=longitude-count*DLONG).filter(longitude__lte=longitude+count*DLONG)
            
            # check if query is returning enough data (a minimum of 5 food trucks)
            if len(queryset) < 5:
                count += 1 # then increase the rectangle of search
            else:
                break

        return queryset
