from django.shortcuts import render

# Create your views here.


def home(requests):
    return render(requests,"index.html")

def about(requests):
    return render(requests,"about.html")

def services(requests):
    return render(requests,"services.html")
def service_details(requests):
    return render(requests,"service_details.html")
def pricing_plan(requests):
    return render(requests,"pricing_plan.html")
def contact(requests):
    return render(requests,"contact.html")
def study_grid(requests):
    return render(requests,"study_grid.html")
def study_details(requests):
    return render(requests,"study_details.html")
def team_grid(requests):
    return render(requests,"team_grid.html")
def team_details(requests):
    return render(requests,"team_details.html")
def faq(requests):
    return render(requests,"faq.html")
def error_404(requests):
    return render(requests,"404.html")
def blog_grid(requests):
    return render(requests,"blog_grid.html")
def blog_list(requests):
    return render(requests,"blog_list.html")
def blog_details(requests):
    return render(requests,"blog_details.html")