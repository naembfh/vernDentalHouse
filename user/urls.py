from django.urls import path
from .views import loginUser,signupUser
urlpatterns = [
    path('login/',loginUser,name='login'),
    path('signup/',signupUser,name='signup')
]
