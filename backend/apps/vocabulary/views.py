from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserVocabulary, VocabularyWord
from .serializers import UserVocabularySerializer


class LearnedWordsView(APIView):
    def get(self, request):
        words = UserVocabulary.objects.filter(user=request.user).select_related("vocabulary")
        return Response(UserVocabularySerializer(words, many=True).data)

    def post(self, request):
        word = request.data.get("word")
        if not word:
            return Response({"detail": "word is required."}, status=status.HTTP_400_BAD_REQUEST)
        vocabulary_word, _ = VocabularyWord.objects.get_or_create(
            word=word,
            defaults={
                "definition": request.data.get("definition", ""),
                "difficulty": request.data.get("difficulty", ""),
                "examples": request.data.get("examples", []),
            },
        )
        learned_word, _ = UserVocabulary.objects.get_or_create(user=request.user, vocabulary=vocabulary_word)
        learned_word.times_seen += 1
        learned_word.save(update_fields=["times_seen"])
        return Response(UserVocabularySerializer(learned_word).data, status=status.HTTP_201_CREATED)


class MarkMasteredView(APIView):
    def post(self, request, pk):
        item = get_object_or_404(UserVocabulary, id=pk, user=request.user)
        item.mastered = True
        item.save(update_fields=["mastered"])
        return Response(UserVocabularySerializer(item).data)

    def delete(self, request, pk):
        item = get_object_or_404(UserVocabulary, id=pk, user=request.user)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class VocabularyStatsView(APIView):
    def get(self, request):
        queryset = UserVocabulary.objects.filter(user=request.user)
        return Response(
            {
                "words_learned": queryset.count(),
                "words_mastered": queryset.filter(mastered=True).count(),
                "total_seen": sum(item.times_seen for item in queryset),
            },
            status=status.HTTP_200_OK,
        )
