from rest_framework.viewsets import ModelViewSet
from .serializers import PersonSerializer
from .models import Person
from rest_framework.response import Response

# Create your views here.


class PersonViewsets(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
