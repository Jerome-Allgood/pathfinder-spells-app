from django.http import HttpResponse
from django.views.generic import ListView
from django.views import View


from spell.models import Spell

# Create your views here.


class TestView(ListView):
	model = Spell
	paginate_by = 20

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		return context







