from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserVocabulary
from .serializers import UserVocabularySerializer


class LearnedWordsView(APIView):
    def get(self, request):
        words = UserVocabulary.objects.filter(user=request.user).select_related("vocabulary")
        return Response(UserVocabularySerializer(words, many=True).data)


class MarkMasteredView(APIView):
    def post(self, request, pk):
        item = get_object_or_404(UserVocabulary, id=pk, user=request.user)
        item.mastered = True
        item.save(update_fields=["mastered"])
        return Response(UserVocabularySerializer(item).data)


class VocabularyStatsView(APIView):
    def get(self, request):
        queryset = UserVocabulary.objects.filter(user=request.user)
        return Response(
            {
                "words_learned": queryset.count(),
                "words_mastered": queryset.filter(mastered=True).count(),
            },
            status=status.HTTP_200_OK,
        )
