from django.shortcuts import render

# Create your views here.
def home(request):
		departments={'pension','education','backward classes'}
		context={'dept':departments}
		return render(request, "users.html" ,context)