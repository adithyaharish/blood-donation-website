from django.shortcuts import render
#from .models import Blog
from django.http import HttpResponse
from django.shortcuts import redirect
l=[]

def main(request):
    return render(request,'blog/main.html')

def blog_list(request):
    import couchdb
    couch=couchdb.Server('http://127.0.0.1:5984/')
    db = couch['donor']
    #b=Blog.objects.all().order_by('date')
    
    for id in db:
        b=db.get(id)
        Table = []
        for key,value in b.items():    # or .items() in Python 3
            temp = []
            temp.extend([key,value])
            #Note that this will change depending on the structure of your dictionary
            Table.append(temp)
        Table=Table[2:]
        l.append(Table)
    return render(request,'blog/blog_list.html',{'blog':l}) 

def donor(request):
    if request.method=='GET':
        import couchdb
        couch=couchdb.Server('http://127.0.0.1:5984/')
        db1 = couch['donor']
        temp=dict()
        temp["val"]=""
        n=str(request.GET.get('name'))
        p=str(request.GET.get('phone'))
        b=str(request.GET.get('bloodgrp'))
        c=str(request.GET.get('city'))
        #temp["val"]=eval(s)
        #print(s)
        if(n !="None"):
          doc={'name':n,'phone':p,'bloodgrp':b,'city':c}
          db1.save(doc)
          return redirect('/blog/main/')
    return render(request,'blog/donor.html')

def signup(request):
    
    if request.method=='GET':
        import couchdb
        n=""
        e=""
        p=""
        couch=couchdb.Server('http://127.0.0.1:5984/')
        db1 = couch['users']
        temp=dict()
        temp["val"]=""
        n=str(request.GET.get('name'))
        p=str(request.GET.get('password'))
        e=str(request.GET.get('email'))
        #temp["val"]=eval(s)
        #print(s)
        if(n !="None"):
          doc={'name':n,'password':p,'email':e}
          db1.save(doc)
          return redirect('/blog/main/')
    return render(request,'blog/signup.html',temp)
    
def login(request):
    if request.method=='GET':
        import couchdb
        n1=""
        p1=""
        couch=couchdb.Server('http://127.0.0.1:5984/')
        db1 = couch['users']
        temp1=dict()
        temp1["val"]=""
        n1=str(request.GET.get('name'))
        p1=str(request.GET.get('password'))
        #temp["val"]=eval(s)
        for id in db1:
            b=db1.get(id)
            if(b['name']==n1 and b['password']==p1):
                  return redirect('/blog/main/')
    return render(request,'blog/login.html',temp1)





