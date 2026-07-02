from apps.vocabulary.models import UserVocabulary, VocabularyWord


class VocabularyService:
    @staticmethod
    def get_seen_words(user):
        return set(
            UserVocabulary.objects.filter(user=user).values_list("vocabulary__word", flat=True)
        )

    @staticmethod
    def register_word(user, payload):
        if not payload:
            return None
        word = payload.get("word")
        if not word:
            return None
        vocabulary_word, _ = VocabularyWord.objects.get_or_create(
            word=word,
            defaults={
                "definition": payload.get("definition", ""),
                "difficulty": payload.get("difficulty", ""),
                "examples": payload.get("examples", []),
            },
        )
        user_vocabulary, _ = UserVocabulary.objects.get_or_create(user=user, vocabulary=vocabulary_word)
        user_vocabulary.times_seen += 1
        user_vocabulary.save(update_fields=["times_seen"])
        return {
            "word": vocabulary_word.word,
            "definition": vocabulary_word.definition,
            "examples": vocabulary_word.examples,
        }
