from django.shortcuts import render


def contact(request):
    return render(request, "landing/contact.html")