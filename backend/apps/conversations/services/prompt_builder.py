class PromptBuilder:
    @staticmethod
    def build(conversation, user_message):
        topic = conversation.topic.title if conversation.topic else ""
        scenario = conversation.scenario.title if conversation.scenario else ""
        return {
            "topic": topic,
            "scenario": scenario,
            "summary": conversation.summary,
            "message": user_message,
        }
