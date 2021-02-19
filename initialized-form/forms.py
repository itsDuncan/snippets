from django import forms
import time 

class InitializedForm(forms.Form):
	username = forms.CharField(
		widget = forms.TextInput()
	)

	ref = forms.CharField(
		widget=forms.TextInput(attrs={
			'readonly': 'readonly',
			}),
	)

	def __init__(self, *args, **kwargs):
		super(InitializedForm, self).__init__(*args, **kwargs)

		curr_timestamp = time.strftime(r"%d%m%Y%H%M%S", time.localtime())
		self.fields['ref'].initial =  ('DUMMY_TEXT_VER_'+curr_timestamp)