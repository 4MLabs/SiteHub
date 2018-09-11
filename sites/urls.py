from django.urls import path
from . views import (
    IndexView,
    SiteView,
    CategoryView,
    LoginView,
    LogoutView,
)

app_name = 'sites'
urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('site/', SiteView.as_view(), name='sites'),
    path('category/', CategoryView.as_view(), name='categories'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
