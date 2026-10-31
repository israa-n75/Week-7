from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Student


# View and Search Students
@login_required(login_url='login')
def student_list(request):
    query = request.GET.get('search')

    if query:
        students = Student.objects.filter(
            name__icontains=query
        ) | Student.objects.filter(
            course__icontains=query
        )
    else:
        students = Student.objects.all()

    return render(request, 'student_list.html', {
        'students': students,
        'query': query
    })

def add_student(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        age = request.POST.get('age', '').strip()
        email = request.POST.get('email', '').strip()
        course = request.POST.get('course', '').strip()

        if not name or not age or not email or not course:
            return render(request, 'add_student.html', {
                'error': 'All fields are required!'
            })

        if not age.isdigit() or int(age) <= 0:
            return render(request, 'add_student.html', {
                'error': 'Enter a valid age!'
            })

        Student.objects.create(
            name=name,
            age=int(age),
            email=email,
            course=course
        )

        return redirect('student_list')

    return render(request, 'add_student.html')


# Update student
@login_required(login_url='login')
def update_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        age = request.POST.get('age', '').strip()
        email = request.POST.get('email', '').strip()
        course = request.POST.get('course', '').strip()

        if not name or not age or not email or not course:
            return render(request, 'edit_student.html', {
                'student': student,
                'error': 'All fields are required!'
            })

        if not age.isdigit() or int(age) <= 0:
            return render(request, 'edit_student.html', {
                'student': student,
                'error': 'Enter a valid age!'
            })

        student.name = name
        student.age = int(age)
        student.email = email
        student.course = course

        student.save()

        return redirect('student_list')

    return render(request, 'edit_student.html', {'student': student})


# Delete student
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()

    return redirect('student_list')


# Login
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'login.html')


# Logout
@login_required(login_url='login')
def user_logout(request):
    logout(request)
    return redirect('login')

# Dashboard
@login_required(login_url='login')
def dashboard(request):
    total_students = Student.objects.count()

    return render(request, 'dashboard.html', {
        'total_students': total_students
    })