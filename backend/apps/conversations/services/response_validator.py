class ResponseValidator:
    REQUIRED_KEYS = {"reply", "correction", "optimized", "next_question", "vocabulary", "examples"}

    @classmethod
    def validate(cls, response):
        missing = cls.REQUIRED_KEYS.difference(response)
        if missing:
            raise ValueError(f"AI response missing keys: {', '.join(sorted(missing))}")
        return response
