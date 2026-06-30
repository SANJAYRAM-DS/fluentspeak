class ConversationStateMachine:
    @staticmethod
    def advance(state):
        state.goal_progress = min(100, state.goal_progress + 10)
        if state.goal_progress >= 100:
            state.stage = "completed"
        elif state.goal_progress >= 50:
            state.stage = "practice"
        state.save(update_fields=["goal_progress", "stage"])
        return state
