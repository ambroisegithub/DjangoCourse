from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# request config
def index(request):
    path = request.path
    scheme = request.scheme
    method= request.method
    address = request.META["REMOTE_ADDR"]
    user_agent = request.META["HTTP_USER_AGENT"]
    path_info=request.path_info
    response= HttpResponse()
    response.headers['Age']= 30
    
    # string format
    
    msg = f"""<br> 
         <br>path:{path}
         <br>scheme:{scheme}
         <br>method:{method}
         <br>address:{address}
         <br>user_agent:{user_agent}
         <br>path_info:{path_info}
         <br>  response.headers:{response.headers}
         
         <br>
         
    """     
         
    # response ="<html><body><h1>welcome to home page</h1></body></html>"
    return HttpResponse(msg,content_type="text/html",charset="utf-8")
    # return HttpResponse(path, content_type="text/html", charset="utf-8")
    
    # url parameter to return data from url
    
def menuitems(request,dish):
    items={
        "pasta":"Pasta is a type of noddle made from combination of wheat,eggs and milk",
        "falafel":"falafel are deep fried patties or balls made fr",
        "cheesecake":"chees customize"
    }
    
    description = items[dish]
    
    return HttpResponse(f"<h2>{dish}</h2>" + description)

# regular expression in url
# error handling in python

# this is for pagge not found: to handle this we use handler404 class
# handler404 = "my_project.views.handler404" 

# class based views:It helps to organize data from create views from inheretance class
# format example of class based views over functions views

# class myView(view):
#     def food(self,request):
        # view logic
        # return HttpResponse("this is class based views")