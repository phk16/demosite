from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound,Http404,HttpResponseRedirect
from django.urls import reverse
from . import models

def example_view(request):
    return render(request,'my_app/example.html')

def variable_view(request):
    my_var={'first_name': 'praveen', 'last_name':'krishna', 'some_list':[1,2,3],'logged_in':True}
    return render(request,'my_app/variable.html', context=my_var)

def list_patients(request):
    all_patients=models.patient.objects.all()
    context_list={'patients':all_patients}
    return render(request, 'my_app/variable.html', context=context_list)

def list(request):
    all_cars=models.patient.objects.all()
    con={'patients':all_cars}
    return render(request, 'my_app/list.html', context=con)

def add(request):
    if(request.method=='POST'):
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        age=int(request.POST['age'])
        heart_rate=int(request.POST['heart_rate'])
        models.patient.objects.create(first_name=first_name, last_name=last_name, age=age, heart_rate=heart_rate)
        return redirect(reverse('my_app:list'))
    else:
        return render(request, 'my_app/add.html')

def delete(request):
    return render(request, 'my_app/delete.html')

# def simple_view(response):
#     return render(response,'my_app/example.html')         #join a template

# articles={
#     'sports':'sports news',
#     'finance':'finance news',
#     'poltics':'politics news'
# }
# # Create your views here.
# def news_view(request,topic):
#     try:
#         resultq=articles[topic]
#         return HttpResponse(resultq)
#     except:
#         # resultq="response not found"
#         # return HttpResponseNotFound(resultq)
#         raise Http404("page not found!")

# def add_view(request, num1,num2):
#     result=num1+num2
#     return HttpResponse(str(result))

# def num_page_view(request, num):
#     topics_list=list(articles.keys())
#     topic=topics_list[num]
#     webpage=reverse('topic-page',args=[topic])
#     return HttpResponseRedirect(webpage)