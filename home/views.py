from django.shortcuts import render
from rest_framework_simplejwt.tokens import RefreshToken
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

def Register_form(request):
    
    return render(request,'register9.html')

def login_form(request):
    
    return render(request,'login9.html')







from rest_framework import generics, status
from rest_framework.response import Response

from .serializers import RegisterSerializer, LoginSerializer

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': RegisterSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
