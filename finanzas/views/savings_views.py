from rest_framework import generics
from ..models import Savings
from ..serializers import SavingsSerializer

class SavingsListCreateView(generics.ListCreateAPIView):
    queryset = Savings.objects.all()
    serializer_class = SavingsSerializer

class SavingsRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Savings.objects.all()
    serializer_class = SavingsSerializer
