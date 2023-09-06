from django.contrib.auth.backends import ModelBackend
from kpi_server.models import UserAuth

class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserAuth.objects.get(user_name=username)
        
        except UserAuth.DoesNotExist:
            return None

        if user.check_password(password):
            return user

        return None