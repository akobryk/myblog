from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import re
import datetime
import math
from django.utils.html import strip_tags

def paginate(objects, size, request, context, var_name='object_list'):
	""" Paginate objects provided by view.

	This function takes:
		* a list of elements;
		* a number of objects per page;
		* a request object to get url parameters form;
		* a context to set a new variable info;
		* var_name - the variable name for the list of
			objects;

	It retunrs an updated context object. """ 

	# apply a pagination 
	paginator = Paginator(objects, size)

	# try to get a page number from the request
	page = request.GET.get('page', '1')
	try:
		object_list = paginator.page(page)
	except PageNotAnInteger:
		# if page is not an integer, deliver first page
		object_list = paginator.page(1)
	except EmptyPage:
		# if page is out of range (e.g. 9999),
		# deliver the last page of a result 
		objects_list = paginator.page(paginator.num_pages)

	# set a variables info context 
	context[var_name] = object_list
	context['is_paginated'] = object_list.has_other_pages()
	context['page_obj'] = object_list
	context['paginator'] = paginator

	return context

def count_words(html_string):
	# html_string ="""
	# <h1>Test stringdsadsadsadsada </h1>
	# """
	word_string = strip_tags(html_string)
	matching_words = re.findall(r'\w+', word_string)
	count = len(matching_words)
	return count

def get_read_time(html_string):
	count = count_words(html_string)
	read_time = int(math.ceil(count / 200.0)) # assuming 200 words/min reading
	return read_time

