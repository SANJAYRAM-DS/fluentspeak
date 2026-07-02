from django.views.generic import TemplateView


class AuthView(TemplateView):
    template_name = "web/auth.html"


class DashboardView(TemplateView):
    template_name = "web/dashboard.html"


class ChatView(TemplateView):
    template_name = "web/chat.html"


class VocabularyView(TemplateView):
    template_name = "web/vocabulary.html"


class ProgressView(TemplateView):
    template_name = "web/progress.html"
