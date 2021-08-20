from django.shortcuts import render


# Create your views here.
def about(request):
    return render(request, "landing/about.html")


def contact(request):
    return render(request, "landing/contact.html")