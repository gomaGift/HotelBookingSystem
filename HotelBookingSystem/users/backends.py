from typing import Any
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q


class CustomUserEmailOrPhoneBackend(ModelBackend):
     def authenticate(self, request, username=None, password=None, **kwargs):
        print(username)
        
        User = get_user_model()
        user = User.objects.filter(Q(email=username) | Q(phone_number=username)).first()
        
        if user and user.check_password(password):
            return user
        return None

