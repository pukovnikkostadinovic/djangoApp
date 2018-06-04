from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
	numbers = [1,2,3,4,5]
	name = 'Hasan Hasanovic'
	args = {'name':name, 'numbers':numbers}
	return render(request, 'accounts/home.html',args)