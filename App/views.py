from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import Allcourses
from django.template import loader


def App_index(request):
    #return HttpResponse("Hello World! Yor are in the App/index")
    return render(request, "App/index.html")

def Courses(request):
    ac=Allcourses.objects.all()
    template=loader.get_template('App/courses.html')
    context={
        'ac':ac,
    }
    return HttpResponse(template.render(context, request))

def detail(request, course_id):
    try:
        course=Allcourses.objects.get(pk=course_id)
    except Allcourses.DoesNotExist:
        raise Http404("Course not Available")
    return render(request, "App/detail.html", {"course":course})
    #return HttpResponse('<h2>These are the course details id: '+str(course_id)+'</h2>')
