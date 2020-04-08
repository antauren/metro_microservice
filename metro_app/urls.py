from django.urls import path

from .views import VerificateView

urlpatterns = [

    path('verificate/', VerificateView.as_view()),

]
