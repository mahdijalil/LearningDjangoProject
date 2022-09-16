from django.shortcuts import render
md = 'templates/main'
from .models import *
# Create your views here.
def home(request):
	dummies = Dummy.objects.all()
	context = {
		'dummies': dummies
	}
	return render(request, f'{md}/home.html', context)

	
def post(request, pk):
		post = Dummy.objects.get(id=pk)
		context = {
			'post' : post,
		}
		return render(request, f'{md}/post.html', context)