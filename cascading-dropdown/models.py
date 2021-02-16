from django.db import models

class Directorate(models.Model):
	title = models.CharField(
		max_length=100,
		blank=True,
		null=True,
		)
	
	slug = models.SlugField(
		max_length=100,
		blank=True,
		null=True,
		)

	details = models.TextField(
		blank=True,
		null=True,
		)
	
	def __str__(self):
		return self.title

class Department(models.Model):
	title = models.CharField(
		max_length=100,
		blank=True,
		null=True,
		)
	slug = models.SlugField(
		max_length=100,
		blank=True,
		null=True,
		)

	region = models.ForeignKey(
		Region,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name=('region+'),
		verbose_name=('Region')
		)

	directorate = models.ForeignKey(
		Directorate,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name=('directorate'),
		verbose_name=('Directorate')
		)

	details = models.TextField(
		blank=True,
		null=True,
		)
	
	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		super(Department, self).save(*args, **kwargs)

class Section(models.Model):
	title = models.CharField(
		max_length=100,
		blank=True,
		null=True,
		)

	slug = models.SlugField(
		max_length=100,
		blank=True,
		null=True,
		)

	region = models.ForeignKey(
		Region,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name=('region+'),
		verbose_name=('Region')
		)

	directorate = models.ForeignKey(
		Directorate,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name=('directorate+'),
		verbose_name=('Directorate')
		)

	department = models.ForeignKey(
		Department,
		on_delete=models.SET_NULL,
		null=True,
		blank=True,
		related_name=('department'),
		verbose_name=('Department')
		)

	details = models.TextField(
		blank=True,
		null=True,
		)
	
	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		super(Section, self).save(*args, **kwargs)