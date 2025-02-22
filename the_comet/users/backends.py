from django.contrib.auth.backends import ModelBackend
from .models import CustomerUser

class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = CustomerUser.objects.get(email=username)
            if user.check_password(password):
                return user
        except CustomerUser.DoesNotExist:
            return None