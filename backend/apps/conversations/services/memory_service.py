class MemoryService:
    @staticmethod
    def update_summary(conversation):
        if not conversation.summary:
            conversation.summary = "Conversation started."
            conversation.save(update_fields=["summary", "updated_at"])
        return conversation.summary
