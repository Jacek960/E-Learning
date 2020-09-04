import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
# Create your views here.
from django.views.generic import CreateView

from courses.forms import OrderForm
from courses.models import Category, Course, Banner


class HomePageView(View):
    def get(self,request):
        category_shuffle_list = list(Category.objects.all())
        random.shuffle(category_shuffle_list)
        category_shuffle_list = category_shuffle_list[0:3]
        banner = list(Banner.objects.filter(is_active=True))
        return render(request, 'courses/home.html',{'category_shuffle_list':category_shuffle_list,'banner':banner})




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

class PremiumOrderCreateView(LoginRequiredMixin,CreateView):
    form_class = OrderForm
    success_url = reverse_lazy('categorys_list')
    template_name = 'courses/order_premium.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.GET.get('next', self.success_url)




