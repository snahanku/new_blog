from django.shortcuts import render
from blogapp.models import user_blogs,user
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from blogapp.serializers import blogserializer
from rest_framework.viewsets import ModelViewSet
from blogapp.forms import CreateblogForm

def blogs(request):
    if request.method=="POST":
        title=request.POST['blog_name']
        content=request.POST['blog_content']
        user_data=user_blogs.objects.create(
        blog_title= title,
        blog_content = content
        )
        user_data.save()
        return redirect('/dashboard/feature/')
   
    
    return render(request , 'blog.html')
    

def featured_blogs(request):
    return render(request,"blog_dashboard.html" ,{'blog_data':user_blogs.objects.all() } )


from django.shortcuts import render, redirect 
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import login , logout , authenticate 
from django.contrib.auth.models import User
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm


def dashboard(request):
    return render(request , "dashboard.html")

def userlogin(request):
     if request.method=="POST":
        username=request.POST.get('username')# fetching the usernamee data
        password=request.POST.get('password')#fetching the  password data
        user_name= authenticate(username)
        user_password=authenticate(password)
        user= authenticate(request , username=username , password=password)
        if user is not None:
          login(request , user)
          return redirect("/dashboard/new_page/")
        else:
            messages.success( request , message="There was not logged in error, Try Again.....")# raise excepttion
            return render(request , "login.html")
    
    

     return render(request ,"login.html")


          
def signup(request):
    if request.method=="POST":
        username= request.POST.get("username")#fetch data
        email=request.POST.get("email")#fetch email data
        password=request.POST.get("password")
        user_data= User.objects.create_user(
                                   username=username,  #
                                   email=email,        # create data
                                   password=password    #
                                 )
        user_data.save()    # save data

        return redirect('/dashboard/news/')
     
    
    return render(request , "signup.html")

    
    def forgetPassword(request):
        pass






def blog_create(request):
    if request.method=="POST":
        blog_title= request.POST.get("title")
        blog_content= request.POST.get("body")
        query= user_blogs.objects.create(blog_title=blog_title ,
                                         blog_content=blog_content,
                                           )
        query.save()

    return render(request , "blog.html" ,{})






def blog_update(request ,id):
    if request.method=="POST":#  get the data by post method
        data=user_blogs.objects.get(pk=id)#get the data by id 
        fm=CreateblogForm(request.POST, instance=data)#
        if fm.is_valid():#
             fm.save() # change and validate data
             return HttpResponse("ok")# redirect to the parse page

    else:
         data=User.objects.get(pk=id) # get the data by GET method
         fm=CreateblogForm(instance=data)

    return render(request , "update.html" ,{'form':fm})







def blog_delete(request ,id):
     data=user_blogs.objects.all().filter(id=id).delete()
     return redirect('/dashboard/feature/')





def news(request):
    import requests

    api_key='5bec0d7f092a4f90b179c37559c759fd'
   # query=request.POST.get("search")
    query='technology'
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
    response = requests.get(url)
    data = response.json()

    for value in data['articles']:
        print(value)

    articles = data['articles']

    for article in articles:
        print("\n")
        print(f"Title: {article['title']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}")
        print(f"Published At: {article['publishedAt']}")
        print("\n")

    return render(request ,'dashboard.html', {'news_data':articles})



@api_view(['GET']) 
def postdata(request):
    data= user_blogs.objects.all()
    serializer= blogserializer(data , many=True)
    return  Response(serializer.data)

class blogViewSet(ModelViewSet):
    queryset = user_blogs.objects.all()
    serializer_class = blogserializer






def update_data(request ,id): ### update the user  data
    if request.method=="POST":#  get the data by post method
        data=user_blogs.objects.get(pk=id)#get the data by id 
        fm=CreateblogForm(request.POST, instance=data)#
        if fm.is_valid():#
             fm.save() # change and validate data
             return redirect("/dashboard/feature/")# redirect to the parse page

    else:
         data=user_blogs.objects.get(pk=id) # get the data by GET method
         fm=CreateblogForm(instance=data)

    return render(request , "update.html" ,{'form':fm})


    