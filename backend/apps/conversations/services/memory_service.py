class MemoryService:
    @staticmethod
    def update_summary(conversation, user_message=None, assistant_reply=None):
        if not conversation.summary:
            conversation.summary = "Conversation started."
        if user_message and assistant_reply:
            conversation.summary = (
                f"{conversation.summary}\nUser: {user_message}\nAssistant: {assistant_reply}"
            ).strip()
        conversation.save(update_fields=["summary", "updated_at"])
        return conversation.summary
