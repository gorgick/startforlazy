from django.shortcuts import render
from .forms import LoginForm, RegisterForm
from django.views import View
from django.contrib.auth import login, authenticate
from .models import Customer
from django.http import HttpResponseRedirect
from django.contrib import messages
from courses.models import Course
from django.core.mail import send_mail
from django.conf import settings


class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'users/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.add_message(request, messages.INFO, "Успех")
                return HttpResponseRedirect('/')
        return render(request, 'users/login.html', {'form': form})


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST or None, request.FILES)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.first_name = form.cleaned_data['first_name']
            new_user.last_name = form.cleaned_data['last_name']
            new_user.email = form.cleaned_data['email']
            new_user.save()
            new_user.set_password(form.cleaned_data['password1'])
            new_user.save()
            Customer.objects.create(
                user=new_user,
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address'],
                image_user=form.cleaned_data['image_user']
            )
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            subject = 'Welcome to my site'
            message = "'I'm glad to see you here!"
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [user.email],
                fail_silently=False
            )
            messages.add_message(request, messages.INFO, "Успех")
            return HttpResponseRedirect('/')
        return render(request, 'users/register.html', {'form': form})


class CartView(View):
    """Куратор курса"""
    def get(self, request, *args, **kwargs):
        course = Course.objects.get(slug=kwargs['slug'])
        owner = course.owner
        return render(request, 'users/owner.html', {'course': course, 'owner': owner})


class PersonalAreaView(View):
    def get(self, request, *args, **kwargs):
        customer = Customer.objects.get(user=request.user)
        return render(request, 'users/personalarea.html', {'customer': customer})
