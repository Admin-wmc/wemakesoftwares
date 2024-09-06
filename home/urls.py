
from django.urls import path,include
from . import views
# urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
urlpatterns = [
    path('', views.home,name="home"),
    path('about', views.about,name="about"),
    path('services', views.services,name="services"),
    path('service_details', views.service_details,name="service_details"),
    path('pricing_plan', views.pricing_plan,name="pricing_plan"),
    path('contact', views.contact,name="contact"),
    path('study_grid', views.study_grid,name="study_grid"),
    path('study_details', views.study_details,name="study_details"),
    path('team_grid', views.team_grid,name="team_grid"),
    path('team_details', views.team_details,name="team_details"),
    path('faq', views.faq,name="faq"),
    path('blog_grid', views.blog_grid,name="blog_grid"),
    path('blog_list', views.blog_list,name="blog_list"),
    path('blog_details', views.blog_details,name="blog_details"),
    path('error_404', views.error_404,name="error_404"),
    path('register_api/', views.RegisterView.as_view(), name='register'),
    path('login_api/', views.LoginView.as_view(), name='login'),
    path('register/', views.Register_form, name = "register"),
    path('login/',views.login_form,name='login'),
 

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
