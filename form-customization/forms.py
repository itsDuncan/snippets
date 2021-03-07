from django import forms

class ModelNameForm(forms.ModelForm):
	class Meta:
		model = ModelName
		fields = '__all__'
		exclude = ['slug', 'created', 'modified']

	def __init__(self, *args, **kwargs):
		super(ModelNameForm, self).__init__(*args, **kwargs)
		for fieldname, field in self.fields.items():
			field.widget.attrs.update({
				'class': 'form-control',
				'placeholder': '',
			})

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)