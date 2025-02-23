from django.shortcuts import render
def index(request):
    return render(request,"index.html");
def explore(request):
    return render(request,"explorepage.html");
def about(request):
    try:
        if request.method=="POST":
            n1=request.POST.get('name')
            n2=request.POST.get('email')
    except:
        pass
    return render(request,"aboutpage.html");
def seemore(request):
    return render(request,"seemoreartwork.html");
def seemore1(request):
    return render(request,"seemorephotos.html");
def seemore2(request):
    return render(request,"seemorevideos.html");


