from .models import Directorate, Section, Department

def load_directorates(request):
	template		= 'includes/directorate_options.html'
	directorate_id	= request.GET.get('directorate')
	departments		= Department.objects.filter(directorate_id=directorate_id)
	return render(request, template, {'departments': departments})

def load_departments(request):
	template		= 'includes/department_options.html'
	directorate_id	= request.GET.get('directorate')
	departments		= Department.objects.filter(directorate_id=directorate_id)
	return render(request, template, {'departments': departments})

def load_sections(request):
	template		= 'includes/section_options.html'
	department_id	= request.GET.get('department')
	sections		= Section.objects.filter(department_id=department_id)
	return render(request, template, {'sections': sections})