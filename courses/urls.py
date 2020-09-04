from django.urls import path
from .views import HomePageView, CategoryListView, CourseListView, LessonDetailsView, PremiumOrderCreateView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('categorys/', CategoryListView.as_view(), name='categorys_list'),
    path('course/<slug:category_slug>/', CourseListView.as_view(), name='course_list'),
    path('lesson/<int:id>/<slug:category_slug>/', LessonDetailsView.as_view(), name='lesson'),
    path('premium/', PremiumOrderCreateView.as_view(), name='order_premium'),
]
