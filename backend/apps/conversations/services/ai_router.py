class AIRouter:
    @staticmethod
    def generate_reply(prompt):
        message = prompt["message"].strip()
        return {
            "reply": "Thanks for sharing. Can you tell me a little more?",
            "correction": "",
            "optimized": message,
            "next_question": "Can you add one more detail?",
            "vocabulary": None,
            "examples": [],
        }
