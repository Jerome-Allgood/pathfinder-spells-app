from django.urls import path

from spell.views import TestView

urlpatterns = [
    path('', TestView.as_view(), name='test'),
]