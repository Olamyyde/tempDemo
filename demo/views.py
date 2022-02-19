from django.shortcuts import render

# Create your views here.
def render_template(request):
    my_dict = {"name": "Ok"}
    return render(request, 'tempApp/first.html', context=my_dict)

