from django.shortcuts import render
from django.http import HttpResponse
from shieldedapp.models import Users, Post
import json
# Create your views here.

#pip install django-cors-headers
# https://dzone.com/articles/how-to-fix-django-cors-error

def index(request):
    return HttpResponse('index')

def Login(request):
    if request.method == 'POST':
        try:
            s = (request.body).decode("utf-8")
            print(json.loads(s))

            login_data = request.POST.get('login')
            password = request.POST.get('password')
            if len(login_data)>0 and len(password)>0:
                try:
                    obj = Users.objects.get(Username=login_data, Password=password)
                    return HttpResponse('{"Sucess":"{"id":'+str(obj.Id)+'}"}')
                except Exception:
                    obj = Users.objects.get(Email=login_data, Password=password)
                    return HttpResponse('{"Sucess":"{"id":'+str(obj.Id)+'}"}')
                return HttpResponse('{"Error":"Account Not Exist"}')
            else:
                return HttpResponse('{"Error":"Data Cant Be Empty"}')
        except Exception as e:
            return HttpResponse('{"Error":"Something Went Wrong : '+str(e)+'"}')
    else:
        #print(Users.objects.all())
        return HttpResponse('{"Error":"Only Post Request Allowed"}')

def Signup(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            if len(username)>0 and len(email)>0 and len(password):
                obj = Users(Username=username, Email=email, Password=password)
                obj.save()
                obj = Users.objects.get(Username=username, Email=email, Password=password)
                return HttpResponse('{"Succes":{"id":"'+str(obj.Id)+'"}}')
            else:
                return HttpResponse('{"Error":"Data Cant Be Empty"}')
        except Exception as e:
            return HttpResponse('{"Error":"Something Went Wrong : '+str(e)+'"}')
    else:
        return HttpResponse('{"Error":"Only Post Request Allowed"}')

def Posts(request):
    if request.method == 'POST':
        #   Add Post
        content = request.POST.get('content')
        if content != "":
            obj = Post(Content=content)
            obj.save()
            return HttpResponse('{"Success":"1"}')
        else:
            return HttpResponse('{"Error":"Content Empty"}')
    else:
        # Show Posts
        postes = Post.objects.all()
        print(postes)
        result = {}
        for post in postes:
            result[post.Id] = {'Content':post.Content, 'Date':str(post.Date)}
        return HttpResponse(json.dumps(result))
