from rest_framework import generics

from .models import Topic
from .serializers import TopicSerializer


class TopicListView(generics.ListAPIView):
    serializer_class = TopicSerializer

    def get_queryset(self):
        return Topic.objects.filter(is_active=True)


class TopicDetailView(generics.RetrieveAPIView):
    serializer_class = TopicSerializer
    queryset = Topic.objects.all()
