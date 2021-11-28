from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def monthlychallenge(request, month):
    print(month)
    if month == "march":
      return HttpResponse("its your birthday !")

    return HttpResponse("Some really cool stuff")
