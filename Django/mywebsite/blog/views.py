from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
from blog.forms import UserForm
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            Name = request.POST.get('Name','')
            Email_ID = request.POST.get('Email_ID','')
            DOB = request.POST.get('DOB','')
            Flag =  request.POST.get('Flag','')
            ORG =  request.POST.get('ORG','')
        user_obj = Post(Name=Name,Email_ID=Email_ID,DOB=DOB,Flag=Flag,ORG=ORG)
        user_obj.save()

        return render(request, 'blog/signup.html',{'user_obj':user_obj,'is_registered':True})
    else:
        form = UserForm()

	return render(request,'blog/signup.html',{'form':form})

def showdata(request):
    all_users = Post.objects.all()
    return render(request, 'blog/showdata.html', {'all_users': all_users, })


