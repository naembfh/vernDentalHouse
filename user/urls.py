from django.urls import path
from .views import loginUser,signupUser,signoutUser
urlpatterns = [
    path('login/',loginUser,name='login'),
    path('signup/',signupUser,name='signup'),
    path('signout/',signoutUser,name='signout')
]
