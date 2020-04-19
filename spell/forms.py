from django import forms


class FilterForm(forms.Form):
	# components
	somatic_component = forms.BooleanField(required=False)
	verbose_component = forms.BooleanField(required=False)
	material_component = forms.BooleanField(required=False)
	focus_component = forms.BooleanField(required=False)
	divine_focus_component = forms.BooleanField(required=False)
