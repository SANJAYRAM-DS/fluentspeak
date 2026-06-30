class VocabularyService:
    @staticmethod
    def suggest(_user, ai_response):
        return ai_response.get("vocabulary")
