from django.shortcuts import render

# Create your views here.

# def index(request):
#     p_title = "Django Templating Language"
#     author = 'Demi'
#     yob = 2001
#     current_year = 2023
#     age = current_year-yob
#     return render(request, 'index.html',{'p_title':p_title,'author':author,'age':age, 'current_year':current_year})

def index(request):
    continent = ''
    if request.method=='POST':
        continent = request.POST['continent']
        return render(request,'index.html',{'continent':continent})
    else:
        return render(request,'index.html',{'continent':continent})
        # return render(request,'index.html')
        # p_title = "Django Templating Language"
        # author = 'Demi'
        # yob = 2001
        # current_year = 2023
        # Africa = 'African'
        # #Asian = 'True'
        # items =  [p_title,author,yob,current_year]
        # return render(request, 'index.html',{'items':items, 'Africa':Africa,})



def data_collect(request):
    if request.method =='POST':
        name = request.POST['username']
        age= request.POST['age']
        phone = request.POST['phone']
        context = [name, age, phone]
        print(context)
        return render(request, 'loop.html',{'context':context})
    else:
         return render(request,'data_collect.html')


        