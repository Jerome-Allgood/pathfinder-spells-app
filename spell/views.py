from django.views.generic import ListView, DetailView

from spell.models import Spell

# Create your views here.


class SpellListView(ListView):
	model = Spell
	paginate_by = 20

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

	def get_queryset(self):
		spells = Spell.objects.all()
		query = self.request.GET.get('q')
		if query:
			result = spells.filter(name__icontains=query)
			return result
		else:
			return spells


class SpellDetailedView(DetailView):
	template_name = "../templates/spell/spell_detail.html"
	model = Spell
	queryset = Spell.objects.all()
