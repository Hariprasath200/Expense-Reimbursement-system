from django.shortcuts import render
from .forms import Emp
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import demp # Replace YourModel with your actual model name

from django.shortcuts import redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,"reimbursement/Home.html")
def Admin(request):
    employees = demp.objects.all()
    return render(request,"reimbursement/Admin.html",{'employees': employees})
def Manager(request):
    employees = demp.objects.all()
    context = {'employees': employees}
    return render(request, "reimbursement/Manager.html", context)

def update_status(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        new_status = request.POST.get('status')
        try:
            employee = demp.objects.get(id=employee_id)
        except demp.DoesNotExist:
            return HttpResponse("Employee not found", status=404)
        
        # Update the status of the employee
        employee.status = new_status
        employee.save()  # Save the updated employee object
        
        return HttpResponseRedirect(reverse('Managerpage') + '?status_updated=true')
    else:
        return HttpResponse("Method not allowed", status=405)
def admin_update_status(request):
    if request.method == 'POST':
        employee_id = request.POST.get('employee_id')
        new_status = request.POST.get('status')
        try:
            employee = demp.objects.get(id=employee_id)
        except demp.DoesNotExist:
            return HttpResponse("Employee not found", status=404)
        
        # Update the status of the employee
        employee.status = new_status
        employee.save()  # Save the updated employee object
        
        return HttpResponseRedirect(reverse('Managerpage') + '?status_updated=true')
    else:
        return HttpResponse("Method not allowed", status=405)

def Employee(request):
    if request.method == 'POST':
        form = Emp(request.POST, request.FILES)
        if form.is_valid():
            new_item = demp(
                employee_name=form.cleaned_data['employee_name'],
                employee_code=form.cleaned_data['employee_code'],
                mobile_number=form.cleaned_data['mobile_number'],
                email=form.cleaned_data['email'],
                upload=request.FILES['upload'],
                description=form.cleaned_data['description']
            )
            new_item.save()  # Save the new instance to the database
            return redirect('Successpage')  # Redirect to a success URL
    else:
        form = Emp()  # Create a new form instance for GET requests
    
    # Fetch all employees from the database
    employees = demp.objects.all()
    
    return render(request, "reimbursement/Employee.html", {'form': form, 'employees': employees})

def success_view(request):
    return render(request,"reimbursement/sub_success.html")


