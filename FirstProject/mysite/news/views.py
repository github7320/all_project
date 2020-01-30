
from django.shortcuts import render
from django.views.generic import TemplateView

from .forms import EmployeeForm
from .models import Employee
from django.shortcuts import render, redirect

# Create your views here.
class Home(TemplateView):
    template_name='news/index.html'

class about_me(TemplateView):
    template_name='news/aboutme.html'
    def get(self, request):
        data = dict()
        request.session["user_full_name"] = "Full Name"
        data["user_full_name"]=request.session["user_full_name"]
        return render(request, self.template_name, data)

def news_submit_action(request):
    print("Hello")
    
    fname = request.GET["fname"]
    lname = request.GET["lname"]
    mydata = My_Info(first_name=fname, last_name=lname)
    mydata.save()
    print(fname)
    print(lname)
    return render(request, 'news/index.html')

class artical_list(TemplateView):
    template_name='news/artical_list.html'
    def get(self, request):
        data = dict()
        my_list = [1,2,3,4,5]
        data['my_list']=my_list
        return render(request, self.template_name, data)

def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "news/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST,instance= employee)
        if form.is_valid():
            form.save()
        return redirect('employee_list')

def employee_list(request):
    context = {'employee_list': Employee.objects.all()}
    return render(request, "news/employee_list.html", context)

def employee_delete(request,id):
    employee = Employee.objects.get(pk=id)
    employee.delete()
    return redirect('employee_list')



