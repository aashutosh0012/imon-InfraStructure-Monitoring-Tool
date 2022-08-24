from django.shortcuts import render



def homeView(request):
	return render(request,'templates/_base.html')
