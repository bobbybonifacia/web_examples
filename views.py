# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
from django.http import HttpResponse
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.template import Template
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from posts.models import Person
import math

PRINT_REQUEST = 0

def print_req(request):
    if not PRINT_REQUEST:
        return
    print 'request.META', request.META

def root_page(request):
    #print_req(request)
    
    return render_to_response("base.html")


def txt_hello_page(request):
    print_req(request)
    response = HttpResponse("Hello world")
    return response

def html_hello_page(request):
    print_req(request)
    response = HttpResponse()
    html = "<html><head></head><body>";
    html+= "<p> Hello world!</p>";
    html+= "<a href='/'>root</a>";
    html+= "</body></html>";
    
    response.write(html)
    return response

def simple_redirect_page(request):
    print_req(request)
    return HttpResponseRedirect("/html/hello")


def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fac(n-1)

def factorial_page(request, n_param):
    print_req(request)
    try:
        n = int(n_param)
    except ValueError:
        print "invalid number"
        n = 1
    
    html = "<html><head></head><body>";
    html+= "<p>Factorial(" + str(n) + ")=" + str(fac(n)) + " </p>";
    html+= "</body></html>";

    return HttpResponse(html)

def power_page(request, n_p, m_p):
    print_req(request)
    try:
        n = int(n_p)
        m = int(m_p)
    except ValueError:
        print "invalid numbers"
    return render_to_response('power_page.html', {'n' : n, 'm' : m, 'result' : math.pow(n, m)})


def form(request):
    if request.method == "POST":
        name = request.POST['name']
        age = int(request.POST['age'])
        p = Person(name=name, age=age)
        p.save()
        print name, age
    
    c = {}
    c.update(csrf(request))
    for p in Person.objects.all():
        print p.id, p.name, p.age

    c['persons'] = Person.objects.all()
    #print c
    return render_to_response('form_page.html', c)

def my_render_to_response(request, template, context = None):
    if context == None:
        context = {}
    context.update(csrf(request))
    return render_to_response(template, context)

def contact(request):
    return my_render_to_response(request, 'contact.html')

