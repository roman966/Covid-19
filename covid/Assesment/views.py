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

Age=0
Sex=0
Temp=0
Assessment_Score=0
Result=0

def basic(request):
    global Age
    global Sex
    global Temp
    global Assessment_Score
    if request.method == 'POST':
        form = BasicForm(request.POST)
        if form.is_valid():
            Age = form.cleaned_data.get('Age')
            Sex = form.cleaned_data.get('Sex')
            Temp = form.cleaned_data.get('Temparature')
            if(Temp > 37.5):
                Assessment_Score = 2
                
            else:
                Assessment_Score = 0
                
            return redirect('/info')

    else:
        form = BasicForm

    context = {
        "form": form,
    }
    return render(request, 'basic.html', context)


def information(request):
    global Age
    global Sex
    global Temp
    global Assessment_Score
    if request.method == 'POST':
        form = InformationForm(request.POST)
        
        if form.is_valid():
            Info = form.cleaned_data.get('Information')
            if Info[0] != '6':
                Assessment_Score = Assessment_Score+len(Info)-1+3
                
            return redirect('/addi')

    else:
        form = InformationForm

    context = {
        "form": form,
    }

    return render(request, 'info.html', context)


def additional(request):
    global Age
    global Sex
    global Temp
    global Assessment_Score
    if request.method == 'POST':
        form = AdditionalInfoForm(request.POST)
        if form.is_valid():
            addinfo = form.cleaned_data.get('AddiInfo')
            if addinfo[0] != '9':
                Assessment_Score = Assessment_Score +(len(addinfo)*2)
                    
            return redirect('/final')
    else:
        form = AdditionalInfoForm  


    context = {
        "form": form,
    }

    return render(request, 'additional.html', context)



def final(request):
    global Age
    global Sex
    global Temp
    global Assessment_Score
    if Assessment_Score < 5:
        Result = "Negative"
        show_string = "You have merely have a chance to affected by Covid-19.Still for better precurement you can take isolation and contact doctor and follow advice"

    elif Assessment_Score >= 5 and Assessment_Score <= 7:
        Result = "Positive"
        show_string = "You have highly chance of affecting by Covid-19.Seek doctor immediately.You can take help from these numbers 16233 and 333."
    else:
        Result = "Positive"
        show_string = "It is almost confirmed case of Covid-19.Take isolation and hospitalize yourself.Contact doctor and in case of emergency call 16233 and 333"
    person = Person()
    person.Age = Age
    person.Sex = Sex
    person.Temp = Temp
    person.Assessment_Score = Assessment_Score
    person.Result = Result
    person.save()
    context = {
        "show_string": show_string
    }

    return render(request, 'final.html', context)


def records(request):

    queryset = Person.objects.all()

    context = {
        "queryset": queryset
    }

    return render(request, 'records.html', context)

