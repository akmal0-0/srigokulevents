from django.shortcuts import render

def home(request):
    return render(request,"catering/index.html")
def about(request):
    return render(request,"catering/about.html")
def catering(request):
    return render(request,"catering/catering.html")
def decoration(request):
    return render(request,"catering/decoration.html")
def photography(request):
    return render(request,"catering/photography.html")
def makeup(request):
    return render(request,"catering/makeup.html")
def entertainment(request):
    return render(request,"catering/entertainment.html")
def contact(request):
    return render(request,"catering/contact.html")



