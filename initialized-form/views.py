from django.shortcuts import render
from .form import InitializedForm

def initialized_form(request):
	template_name = 'initialized_form.html'

	if request.method == 'POST':
		form = InitializedForm(request.POST)

		if form.is_valid():
			username = request.user
			form.save()
	else:
		form = InitializedForm(request.POST)

	context = {
		'form': form,
	}
	return render(request, template_name, context)