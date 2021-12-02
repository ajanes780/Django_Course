
from django.http.response import HttpResponseNotFound, HttpResponseRedirect, Http404
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
    "dec": None
}

months = list(monthly_challenges.keys())


def index(request):
    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge_by_number(request, month):
    if month != 0 and month <= len(months):
        redirect_month = months[month-1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)

    raise Http404()


def monthlychallenge(request, month):

    try:
        challenge_text = monthly_challenges[month]
        print(challenge_text)
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })

    except:
        #  looks automaticly in the base templates for a 404 page
        raise Http404()
