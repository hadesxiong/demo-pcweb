# codingt=utf8
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model

class CustomAuthBackend(BaseBackend):

    def authenticate(self,request,notes_id=None,password=None,**kwargs):

        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(notes_id=notes_id)
            if user.check_password(password):
                return user
            
        except UserModel.DoesNotExist:
            return None
        
    def getUser(self,notes_id):
        
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(notes_id=notes_id)
        except UserModel.DoesNotExist:
            return None
