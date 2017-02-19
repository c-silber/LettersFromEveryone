from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Hello, world. You're at the owls index.")

def about_us(request):
	return HttpResponse("We are a grassroots organization that sends postcards.")