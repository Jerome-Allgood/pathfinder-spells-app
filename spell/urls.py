from django.urls import path

from spell.views import SpellListView, SpellDetailedView

urlpatterns = [
    path('', SpellListView.as_view(), name='spell_list'),
    path('<int:pk>/', SpellDetailedView.as_view(), name='spell_detail')
]