from django.test import TestCase
from django.http import HttpRequest
from django.utils.html import strip_tags
from re import findall
from math import ceil
from blog.utils import paginate, count_words, get_read_time


class UtilsTestCase(TestCase):
	""" Test functions from the util module """

	def setUp(self):
		pass

	def test_paginate(self):
		context = {}

		request = HttpRequest()

		# check the PageNotAnInteger case: "hello" string
		request.GET['page'] = 'hello'
		result = paginate(
			[1, 2, 3, 4], 3, request, context, var_name='objects_list')
		self.assertEqual(len(result['objects_list']), 3)
		self.assertEqual(result['is_paginated'], True)
		self.assertEqual(len(result['page_obj']), 3)
		self.assertEqual(result['objects_list'][0], 1)
		self.assertEqual(result['objects_list'][1], 2)
		self.assertEqual(result['objects_list'][2], 3)

		# check the empty page case: should be the last page
		request.GET['page'] = '9999'
		result = paginate([1, 2, 3, 4], 3, request, context, 
			var_name='objects_list')
		self.assertEqual(len(result['objects_list']), 1)
		self.assertEqual(result['objects_list'][0], 4) 

		# check the valid page: third page
		request.GET['page'] = '3'
		result = paginate([1, 2, 3, 4, 5, 6], 2, request, context, 
			var_name='the_list')
		self.assertEqual(len(result['the_list']), 2)
		self.assertEqual(result['the_list'][0], 5)
		self.assertEqual(result['the_list'][1], 6)


	def test_count_words(self):
		html_string = "<h1>Test this string</h1>"

		# check count of matching words in the string
		word_string = strip_tags(html_string)
		matching_words = findall(r'\w+', word_string)
		count = len(matching_words)
		self.assertEqual(count, 3)

		# check the reading time of the string
		count = count_words(html_string)
		read_time = int(ceil(count / 200.0))
		self.assertEqual(read_time, 1)


