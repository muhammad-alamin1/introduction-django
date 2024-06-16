from django.shortcuts import render
from about_us.models import Member, Student

# Create your views here.
class Information:
    def student_info(request):
        teach = Student.objects.all()
        
        return render(request, "s_d.html", {"stu": teach})