from django.shortcuts import render

def home_site(request):
	return render(request,"home_site.html")  