import random

from django.shortcuts import render
from django.views import View
# Create your views here.
from courses.models import Category, Course


class HomePageView(View):
    def get(self,request):
        category_shuffle_list = list(Category.objects.all())
        random.shuffle(category_shuffle_list)
        category_shuffle_list = category_shuffle_list[0:3]
        return render(request, 'courses/home.html',{'category_shuffle_list':category_shuffle_list})




class CategoryListView(View):
    def get(self, request):
        categorys_list = Category.objects.all().order_by('-name')
        return render(request, "courses/courses_list.html", {'categorys_list': categorys_list})

class CourseListView(View):
    def get(self, request,category_slug=None):
        if category_slug:
            category = Category.objects.get(slug=category_slug)
            course_list = Course.objects.filter(category=category)
        return render(request, "courses/courses_by_category_list.html", {'course_list': course_list,'category':category})

class LessonDetailsView(View):
    def get(self, request, id, category_slug):
        category = Category.objects.get(slug=category_slug)
        course_list = Course.objects.filter(category=category)
        lesson = Course.objects.get(id=id)
        return render(request, 'courses/course_details.html', {'lesson': lesson,'course_list':course_list})

