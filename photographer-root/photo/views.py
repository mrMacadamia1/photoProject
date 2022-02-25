from django.shortcuts import render

# Create your views here.


def home(request):
	return render(request, 'home.html')

def connection(request):
	return render(request, 'connection.html')

def work(request):
	return render(request, 'work.html')