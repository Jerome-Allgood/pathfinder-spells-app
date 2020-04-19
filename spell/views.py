from time import timezone

from django.http import HttpResponse
from django.views.generic import ListView
from django.views import View

from django.views.generic import ListView, DetailView

from spell.models import Spell

# Create your views here.


class SpellListView(ListView):
	model = Spell
	paginate_by = 20

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		return context


class SpellDetailedView(DetailView):
	template_name = "../templates/spell/spell_detail.html"
	model = Spell
	queryset = Spell.objects.all()
