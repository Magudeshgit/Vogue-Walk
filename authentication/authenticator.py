from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class auth(ModelBackend):
    def authenticate(self,username=None,password=None,**kwargs):
        UserModel = get_user_model()
        try: 
            user = UserModel.objects.get(email=username)
            if user.check_password(password):
                return user
        except UserModel.DoesNotExist:
            return None
        return None
