from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView


class LoginUser(LoginView):
    template_name: str = "users/login_simple.html"
    def get_success_url(self):
        success_url = reverse_lazy("index")

        return success_url