from django.urls import path
from .views import AppViews, AppPageViews

urlpatterns = [
    path('', AppViews.as_view(), name='app_home'),
    path('<slug:slug>/', AppPageViews.as_view(), name='app'),
]
        