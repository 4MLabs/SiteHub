from django.urls import path
from . views import (
    IndexView,
    SiteView,
    CategoryView,
    LoginView,
    LogoutView,
    APICategoryView,
    APISiteView,
)

app_name = 'sites'

api_version = 'v1'

urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('site/', SiteView.as_view(), name='sites'),
    path('category/', CategoryView.as_view(), name='categories'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/{}/site/'.format(api_version), APISiteView.as_view(), name='api-site'),
    path('api/{}/category/'.format(api_version), APICategoryView.as_view(), name='api-category'),
]
