from django.http import HttpResponse
import datetime 
from django.template import Template, Context

def hello(request):
	return HttpResponse("Hello world")

def current_datetime(request): 
	now = datetime.datetime.now() 
	html = "<html><body>It is now %s.</body></html>" % now 
	t = Template("<html><body>It is now2 {{ current_date }}.</body></html>")
	html = t.render(Context({'current_date' : now}))
	return HttpResponse(html)

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()

	assert False

	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)
