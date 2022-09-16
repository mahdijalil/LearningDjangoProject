from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class Dummy(models.Model):
	pic = models.ImageField(upload_to="dummies")
	title = models. CharField(max_length=50, blank=False)
	text = RichTextField(max_length=50000, blank= False)
	created = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return str(self.title)

