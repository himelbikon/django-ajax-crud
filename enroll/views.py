from django.shortcuts import render
from django.http import JsonResponse
from .forms import *
from .models import *
# from django.views.decorators.csrf import csrf_exempt


def home(request):
    form = StudentRegistration()
    data = {'form': form, 'students': DemoUser.objects.all().order_by('-id')}
    return render(request, 'enroll/home.html', data)


def save_data(request):
    if request.method == 'POST':
        stuid = request.POST.get('stuid', None)
        try:
            if stuid != '':
                student = DemoUser.objects.get(pk=stuid)
                form = StudentRegistration(request.POST, instance=student)
            else:
                form = StudentRegistration(request.POST)
            form.save()
            students_data = list(DemoUser.objects.values().order_by('-id'))
            return JsonResponse({'status': 'success', 'students_data': students_data})
        except Exception as e:
            return JsonResponse({
                'status': str(e)
            })


def delete_data(request):
    if request.method == 'POST':
        id = request.POST.get('id', None)  # got a default value
        user = DemoUser.objects.get(pk=id)
        user.delete()
        return JsonResponse({
            'status': 'deleted'
        })


def edit_data(request):
    if request.method == 'POST':
        id = request.POST.get('id', None)  # got a default value
        student = DemoUser.objects.get(pk=id)
        student_data = {
            'id': id,
            'name': student.name,
            'email': student.email,
            'password': student.password
        }
        return JsonResponse(student_data)
