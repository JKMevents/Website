from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="Blog"),
    path("tickets", views.tickets, name="tickets"),
    path("member", views.member, name="member"),
    path('generate_qr_code/', views.tickets, name="generate_qr_code"),
    path("tickets_generator", views.tickets_generator, name="tickets_generator")
]
