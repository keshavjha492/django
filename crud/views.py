from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student, ClassRoom, StudentProfile

@login_required
def student(request):
    students = Student.objects.all().order_by('-id')
    return render(request, template_name="crud/student.html", context={"students": students})

@login_required
def classroom(request):
    if request.method == "POST":
        print(request.POST)
        classroom_name = request.POST.get("classroom_name")
        ClassRoom.objects.create(name=classroom_name)
        return redirect("crud_classroom")
    classrooms = ClassRoom.objects.all().order_by('-id')
    return render(request, template_name="crud/classroom.html", context={"classrooms": classrooms})

@login_required
def classroom_update(request, id):
    c = ClassRoom.objects.get(id=id)
    if request.method == "POST":
        n = request.POST.get("classroom_name")
        c.name = n
        c.save()
        return redirect("crud_classroom")
    return render(request, template_name="crud/classroom_update.html", context={"classroom": c})

@login_required
def classroom_delete(request, id):
    c = ClassRoom.objects.get(id=id)
    if request.method == "POST":
        c.delete()
        return redirect("crud_classroom")
    return render(request, template_name="crud/classroom_delete.html", context={"classroom": c})

@login_required
def add_student(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        address = request.POST.get("address")
        classroom_id = request.POST.get("classroom")
        phone = request.POST.get("phone")
        bio = request.POST.get("bio")
        if classroom_id != "null":
            s = Student.objects.create(name=name, age=age, email=email, address=address, classroom_id=classroom_id)
        else:
            s = Student.objects.create(name=name, age=age, email=email, address=address)
        StudentProfile.objects.create(phone=phone, bio=bio, student=s)
        return redirect("crud_student")
    classrooms = ClassRoom.objects.all()
    return render(request, template_name="crud/add_student.html", context={"classrooms": classrooms})

@login_required
def details_students(request,id):
    s =Student.objects.get(id=id)
    return render(request, template_name="crud/details_students.html",context={"student": s})
@login_required
def delete_student(request, id):
    s = Student.objects.get(id=id)
    if request.method == "POST":
        s.delete()
        return redirect("crud_student")
    return render(request, template_name="crud/delete_student.html", context={"student": s})
@login_required
def update_student(request, id):
    s = Student.objects.get(id=id)
    if request.method =="POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        email = request.POST.get("email")
        address = request.POST.get("address")
        classroom_id = request.POST.get("classroom")
        phone= request.POST.get("phone")
        bio = request.POST.get("bio")
        pp = request.FILES.get("profile_picture")
        Student.objects.filter(id=id).update(name=name, age=age, email=email, address=address, classroom_id=classroom_id)
        sp, created = StudentProfile.objects.update_or_create(student=s, defaults={"phone": phone, "bio": bio})
        if pp:
            sp.profile_picture = pp
            sp.save()
        return redirect("details_students", id)
    classrooms = ClassRoom.objects.all()
    return render(request, template_name="crud/update_student.html",context={"student":s,"classrooms":classrooms})