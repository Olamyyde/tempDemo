from django.shortcuts import render

# Create your views here.
def render_template(request):
    my_dict = {"name": "Ok"}
    return render(request, 'tempApp/first.html', context=my_dict)


def render_employee(request):
    my_dict = {"id": 123, "name": "Jon", "salary":10000}
    return render(request, 'tempApp/employeeTemplate.html', context=my_dict)


