# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from models import Adult
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.db.models import Q
# Create your views here.
from django.http import HttpResponse


def view(request):
	sex = Adult.objects.values('sex').distinct()
	race = Adult.objects.values('race').distinct()
	relationship = Adult.objects.values('relationship').distinct()
	
	if (request.GET.get('sex') and request.GET.get('race')):
			
			sex_filter= request.GET.get('sex')
			race_filter=request.GET.get('race')
           		filter=Adult.objects.filter(Q(sex= sex_filter) & Q(race = race_filter))
           		print filter
   
	else:
			filter=Adult.objects.all()[:20]


	context={'sex_filter': filter,'sex': sex ,'race': race, 'relationship' : relationship}
	return render(request, 'view.html', context)
    
# def index(request, template_name='view.html'):

#     if request.GET.get('featured'):
#         featured_filter = request.GET.get('featured')
#         listings = Listing.objects.filter(featured_choices=featured_filter)
#     else:
#         listings = Listing.objects.all()

#     context_dict = {'listings': listings}
#     return render(request, template_name, context_dict)

def sex_filter(request):

	if request.GET.get('sex'):
		import pdb; pdb.set_trace()
		sex_filter= request.GET.get('sex')
		filter=Adult.objects.filter(sex=sex_filter)[:20]

	else:
		filter=Adult.objects.all()[:20]

	context={'sex_filter' : filter}
	return render(request, 'view.html', context)
