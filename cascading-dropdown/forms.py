from django import forms
from .models import (
	Section,
	Department,
	Directorate,
	)

class CascadingForm(forms.Form):

	directorate = forms.ModelChoiceField(
		queryset=Directorate.objects.all(),
		widget=forms.Select(attrs={
			'class': 'form-control',
			}),
	)

	department = forms.ModelChoiceField(
		queryset=Department.objects.none(),
		widget=forms.Select(attrs={
			'class': 'form-control',
			}),
	)

	section = forms.ModelChoiceField(
		queryset=Section.objects.none(),
		widget=forms.Select(attrs={
			'class': 'form-control',
			}),
	)

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		self.fields['department'].queryset = Department.objects.none()
		self.fields['section'].queryset = Section.objects.none()

		if 'directorate' in self.data:
			try:
				directorate_id = int(self.data.get('directorate'))
				self.fields['department'].queryset = Department.objects.filter(directorate_id=directorate_id).order_by('title')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['department'].queryset = self.instance.directorate.department_set.order_by('title')

		if 'department' in self.data:
			try:
				department_id = int(self.data.get('department'))
				self.fields['section'].queryset = Section.objects.filter(department_id=department_id).order_by('title')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['section'].queryset = self.instance.department.section_set.order_by('title')

	def save(self, commit=False, *args, **kwargs):
		form = super(CascadingForm, self).save(commit=False)
		self.modified = timezone.now()

		if commit:
			form.save()

		return form

		super(CascadingForm, self).save(*args, **kwargs)