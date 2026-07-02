import json


class PromptBuilder:
    @staticmethod
    def build(conversation, user_message, learned_words):
        scenario_title = conversation.scenario.title if conversation.scenario else ""
        topic_title = conversation.topic.title if conversation.topic else ""
        level = getattr(conversation.user.profile, "level", "beginner")
        return [
            {
                "role": "system",
                "content": (
                    "You are an English conversation tutor. "
                    "Return strict JSON with keys: reply, correction, optimized_response, vocabulary, examples, next_question. "
                    "Use simple, natural English. Introduce exactly one new vocabulary word if possible."
                ),
            },
            {
                "role": "user",
                "content": json.dumps(
                    {
                        "topic": topic_title,
                        "scenario": scenario_title,
                        "level": level,
                        "summary": conversation.summary,
                        "learned_words": sorted(learned_words),
                        "message": user_message,
                    }
                ),
            },
        ]
