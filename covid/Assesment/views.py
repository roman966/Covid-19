from django.shortcuts import render, redirect

from django.http import HttpResponse

from .forms import BasicForm, InformationForm, AdditionalInfoForm

from .models import Person


def home(request):
    title = 'COVID-19 Self-Assessment System'
    test_yourself = 'Test Yourself'
    see_records = 'See records'

    context = {
        "title": title,
        "test_yourself": test_yourself,
        "see_records": see_records,
    }
    return render(request, 'home.html', context)


person = Person()


def basic(request):
    if request.method == 'POST':
        form = BasicForm(request.POST)
        if form.is_valid():
            person.Age = form.cleaned_data.get('Age')
            person.Sex = form.cleaned_data.get('Sex')
            person.Temp = form.cleaned_data.get('Temparature')
            if(person.Temp > 37.5):
                person.Assessment_Score = 2
            else:
                person.Assessment_Score = 0
            return redirect('/Assesment/info')

    else:
        form = BasicForm

    context = {
        "form": form,
    }
    return render(request, 'basic.html', context)


def information(request):
    if request.method == 'POST':
        form = InformationForm(request.POST)
        if form.is_valid():
            Info = form.cleaned_data.get('Information')
            if Info[0] != '6':
                person.Assessment_Score = person.Assessment_Score+len(Info)-1+3
            return redirect('/Assesment/addi')

    else:
        form = InformationForm

    context = {
        "form": form,
    }

    return render(request, 'info.html', context)


def additional(request):
    if request.method == 'POST':
        form = AdditionalInfoForm(request.POST)
        if form.is_valid():
            addinfo = form.cleaned_data.get('AddiInfo')
            if addinfo[0] != '9':
                person.Assessment_Score = person.Assessment_Score+(len(addinfo)*2)
            if(person.Assessment_Score < 5):
                person.Result = "Negative"
            else:
                person.Result = "Positive"
            person.save()

            return redirect('/Assesment/final')

    else:
        form = AdditionalInfoForm

    context = {
        "form": form,
    }

    return render(request, 'additional.html', context)


def records(request):
    # person = Person.objects.create(
    # Age=25, Sex="Male", Temp=76, Assessment_Score=5, Result="Positive")

    queryset = Person.objects.all()

    context = {
        "queryset": queryset
    }

    return render(request, 'records.html', context)


def final(request):
    if person.Assessment_Score < 5:
        show_string = "You have merely have a chance to affected by Covid-19.Still for better precurement you can take isolation and contact doctor and follow advice"

    elif person.Assessment_Score >= 5 and person.Assessment_Score <= 7:
        show_string = "You have highly chance of affecting by Covid-19.Seek doctor immediately.You can take help from these numbers 16233 and 333."
    else:
        show_string = "It is almost confirmed case of Covid-19.Take isolation and hospitalize yourself.Contact doctor and in case of emergency call 16233 and 333"

    context = {
        "show_string": show_string
    }

    return render(request, 'final.html', context)
