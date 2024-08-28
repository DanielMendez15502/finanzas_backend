from rest_framework import generics
from ..models import Debt
from ..serializers import DebtSerializer

class DebtListCreateView(generics.ListCreateAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer

class DebtRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Debt.objects.all()
    serializer_class = DebtSerializer
