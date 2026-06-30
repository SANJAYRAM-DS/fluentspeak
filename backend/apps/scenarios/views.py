from rest_framework import generics

from .models import Scenario
from .serializers import ScenarioSerializer


class ScenarioListCreateView(generics.ListCreateAPIView):
    serializer_class = ScenarioSerializer

    def get_queryset(self):
        return Scenario.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ScenarioDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ScenarioSerializer

    def get_queryset(self):
        return Scenario.objects.filter(user=self.request.user)
