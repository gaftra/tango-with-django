import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tangowithdjango.settings')

import django
django.setup()

from rango.models import Category, Page

def populate():
	python_cat = add_cat('Python',128,64)
	
	add_page(cat=python_cat,
		title="Official Python Tutorial",
		url="http://docs.python.org/2/tutorial",
		views=200)
		
	add_page(cat=python_cat,
		title="How to Think like a Computer Scientist",
		url="http://www.greenteapress.com/thinkpython/")
	
	add_page(cat=python_cat,
		title="Learn Python in 10 Minutes",
		url="http://www.korokithakisnet/tutorials/python/")
		
	django_cat = add_cat("Django",64,32)
	
	add_page(cat=django_cat,
		title="Official Django Tutorial",
		url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")
		
	add_page(cat=django_cat,
		title="Django Rocks",
		url="http://www.djangorocks.com/",
		views=100)
		
	add_page(cat=django_cat,
		title="How to Tango with Django",
		url="http://www.tangowithdjango.com/",
		views=50)
		
	frame_cat = add_cat("Other Frameworks",32,16)
	
	add_page(cat=frame_cat,
		title="Bottle",
		url="http://bottlepy.org/docs/dev/",
		views=49)
		
	add_page(cat=frame_cat,
		title="Flask",
		url="httP://flask.pocoo.org",
		views=2)
		
	for c in Category.objects.all():
		for p in Page.objects.filter(category=c):
			print "- {0} - {1}".format(str(c), str(p))
			
def add_page(cat, title, url, views=0):
	p = Page.objects.get_or_create(category=cat, title=title)[0]
	p.url=url
	p.views=views
	p.save()
	return p
	
def add_cat(name, views, likes):
	c = Category.objects.get_or_create(name=name)[0]
	c.views = views
	c.likes = likes
	return c
	
if __name__ == '__main__':
	print "Starting Rango population scirpt..."
	populate()