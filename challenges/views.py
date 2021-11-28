from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
# Create your views here.


monthly_challenges = {
    "jan": " run 5 miles every day ",
    "feb": "Study python 30 mins a day ",
    "march": "its your birthday",
    "april": "Easter is coming",
    "may": "get ready for spring",
    "june": "keep working out",
    "july": "how far can you run ",
    "aug": "Ready for the beach",
    "sept": " ready for school",
    "oct": "spooky",
    "nov": "what to do here",
    "dec": "christmass is here "
}


def monthly_challenge_by_number(request, month):

    if month != 0 and month <= 12:
        months = list(monthly_challenges.keys())
        redirect_month = months[month-1]
        return HttpResponseRedirect("/challenges/" + redirect_month)
      
    return HttpResponseNotFound(" this month is not supported yet ")


def monthlychallenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported")
