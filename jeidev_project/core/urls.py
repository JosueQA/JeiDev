from django.urls import path
from .views import HomeView, ContactView, AboutView, DonateView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("contact/", ContactView.as_view(), name="contact"),
    path("about/", AboutView.as_view(), name="about"),
    path("donate/", DonateView.as_view(), name="donate"),
]
        