from django.http import response
from django.http.response import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse

monthly_challenges = {
    "jan": "Run 5 miles every day",
    "feb": "Study python 30 mins a day",
    "march": "It's your birthday",
    "april": "Easter is coming",
    "may": "Get ready for spring",
    "june": "keep working out",
    "july": "how far can you run ",
    "aug": "Ready for the beach",
    "sept": "ready for school",
    "oct": "spooky",
    "nov": "what to do here",
    "dec": "christmass is here "
}

months = list(monthly_challenges.keys())


def index(req):
    list_items = ""
    for month in months:
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{month.capitalize()}</a></li>"
        response_body = f"<ul>{list_items}</ul>"

    return HttpResponse(response_body)


def monthly_challenge_by_number(request, month):
    if month != 0 and month <= len(months):
        redirect_month = months[month-1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)

    return HttpResponseNotFound("This month is not supported yet ")


def monthlychallenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
    except:
        return HttpResponseNotFound("This month is not supported")
