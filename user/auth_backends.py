# from django.contrib.auth.backends import ModelBackend
# from .models import CustomUser
# from django.db import models

# class EmailOrUsernameModelBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, email=None, **kwargs):
#         try:
#             user = CustomUser.objects.get(models.Q(username=username) | models.Q(email=email))
#         except CustomUser.DoesNotExist:
#             return None

#         if user.check_password(password):
#             return user

#     def get_user(self, user_id):
#         try:
#             return CustomUser.objects.get(pk=user_id)
#         except CustomUser.DoesNotExist:
#             return None
