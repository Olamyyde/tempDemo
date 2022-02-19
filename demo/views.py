from django.shortcuts import render

# Create your views here.
def render_template(request):
    return render(request, 'tempApp/first.html')

