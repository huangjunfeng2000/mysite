from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime 
from django.template import Template, Context
from django.template.loader import get_template

def hello(request):
	return HttpResponse("Hello world")

def current_datetime1(request): 
	now = datetime.datetime.now() 
	html = "<html><body>It is now %s.</body></html>" % now 
	t = Template("<html><body>It is now2 {{ current_date }}.</body></html>")
	t = get_template('current_datetime2.html')
	html = t.render(Context({'current_date' : now}))
	return HttpResponse(html)

def current_datetime2(request): 
	now = datetime.datetime.now() 
	return render_to_response('current_datetime.html', {'current_date' : now})

def current_datetime(request): 
	current_date = datetime.datetime.now() 
	return render_to_response('current_datetime2.html', locals())

def hours_ahead2(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()

	assert False

	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		hour_offset = int(offset)
	except ValueError:
		raise Http404()

	next_time = datetime.datetime.now() + datetime.timedelta(hours=hour_offset)
	return render_to_response('hours_ahead.html', locals())

