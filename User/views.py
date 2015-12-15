from django.shortcuts import render, HttpResponseRedirect

from .home_form import LoginForm
from .models import UserDetail


# Create your views here.

def home(request):
    form = LoginForm(request.POST or None)

    if form.is_valid():
        login = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        id_exists = UserDetail.objects.filter(username=username, password=password)
        if id_exists:
            url = "homepage"
        # new_join.save()
        else:
            url = ""

        return HttpResponseRedirect("/%s" % (url))

    context = {'home_form': form}
    template = "home.html"

    return render(request, template, context)


def about(request):
    context = {}
    template = "About.html"
    return render(request, template, context)


def homepage(request):
    context = {}
    template = "HomePage.html"
    return render(request, template, context)