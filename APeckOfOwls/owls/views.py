from django.shortcuts import get_object_or_404, get_list_or_404, render
from django.http import HttpResponseBadRequest, HttpResponse, Http404
from django.template import loader

# Create your views here.
def index(request):
	template=loader.get_template('index.html')
	return HttpResponse(template.render())