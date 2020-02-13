from django.contrib import admin
from spell.models import Spell
# Register your models here.


@admin.register(Spell)
class SpellAdmin(admin.ModelAdmin):
	pass
