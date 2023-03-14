from django.shortcuts import render

# Create your views here.
def jinja_one(request):
    d={'name':'laxman'}
    return render(request,'jinja_one.html',context=d)