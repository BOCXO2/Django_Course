from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Course
# Create your views here.
def index(request):
    courses = Course.objects.all()
    return render(request, 'shop/courses.html', {'courses': courses})

def single_course(request, course_id):
    # OPTION 1
    try:
        course = Course.objects.get(pk=course_id)
        return render(request, 'shop/single_course.html', {'course': course})
    except Course.DoesNotExist:
        raise Http404()
    