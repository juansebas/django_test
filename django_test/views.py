from django.http import HttpResponse
from django.template import loader, Context, Template
from django.shortcuts import render

from datetime import datetime


def time(request):

    document = """
        <html>
            <body>
                <h1>
                    Current date and time %s
                </h1>
            </body>
        </html>
    """ % datetime.utcnow().strftime("%Y/%m/%d %H-%M-%S")
    return HttpResponse(document)


def calculate_age(request, current_age=0, year=0):
    period = year - datetime.utcnow().year
    age = current_age + period
    context = {'age': age, 'year': year}

    return render(request, "current_age.html", context)
