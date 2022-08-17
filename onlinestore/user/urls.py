from django.urls import path
from user.views import user_profile

urlpatterns = [
    path('<slug:username>', user_profile),
]

# path('<str:username>', user_profile, name='user_profile'),



