from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import ReviewForm, OrderForm
from django.contrib import messages


class BaseView(View):
    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        return render(request, 'courses/courses.html', {'courses': courses})


class CourseView(View):
    def get(self, request, *args, **kwargs):
        course = Course.objects.get(slug=kwargs['slug'])
        form = ReviewForm()
        return render(request, 'courses/course.html', {'course': course, 'form': form})

    def post(self, request, *args, **kwargs):
        course = Course.objects.get(slug=kwargs['slug'])
        form = ReviewForm(request.POST or None)
        if form.is_valid():
            review = form.save(commit=False)
            review.course = course
            review.reviewer = request.user.customer
            if request.user.customer.id in course.reviewers_id_in_review_values():
                messages.add_message(request, messages.ERROR, 'Вы голосовали!')
                return redirect('/')
            review.save()
            if course.reviews.filter(vote='Down'):
                with open('death_note', 'a') as file:
                    file.write(str(request.user.customer) + '\n')
            course.vote_amount = course.reviews.count()
            course.vote_ratio = course.calculate_reviews()
            return redirect('/')
        return render(request, 'courses/course.html', {'course': course, 'form': form})


class OrderView(View):
    def get(self, request, *args, **kwargs):
        course = Course.objects.get(slug=kwargs['slug'])
        form = OrderForm()
        return render(request, 'courses/order.html', {'form': form, 'course': course})

    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST or None)
        course = Course.objects.get(slug=kwargs['slug'])
        customer = Customer.objects.get(user=request.user)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.customer = customer
            new_order.course = course
            new_order.first_name = form.cleaned_data['first_name']
            new_order.last_name = form.cleaned_data['last_name']
            new_order.phone = form.cleaned_data['phone']
            new_order.address = form.cleaned_data['address']
            new_order.start_time = form.cleaned_data['start_time']
            new_order.order_date = form.cleaned_data['order_date']
            new_order.comment = form.cleaned_data['comment']
            form.save()
            customer.orders.add(new_order)
            messages.add_message(request, messages.INFO, 'Ваш заказ успешно получен')
            return redirect('/')
        return render(request, 'courses/order.html', {'form': form, 'course': course})
