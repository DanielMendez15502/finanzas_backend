from rest_framework import generics
from ..models import FinancialProfile
from ..serializers import FinancialProfileSerializer

class FinancialProfileListCreateView(generics.ListCreateAPIView):
    queryset = FinancialProfile.objects.all()
    serializer_class = FinancialProfileSerializer

class FinancialProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FinancialProfile.objects.all()
    serializer_class = FinancialProfileSerializer
