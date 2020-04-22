from django.shortcuts import render
from .models import feedback

def home(request):
	context = {
		'feedback1' : feedback.objects.all().first(),
		'feedback2'	: feedback.objects.all().last()
	}
	return render(request,'casino/index.html',context)
