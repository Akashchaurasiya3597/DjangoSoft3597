from sched import scheduler

from django.shortcuts import render
from .models import FeedbackDatabase,ContactDatabase,CoursesDatabase
from .forms import FeedbackForm,ContactForm
from django.http.response import HttpResponse
from django.contrib import messages


def Home_View(request):
    return render(request, 'Institute/Home.html')
def Contact_View(request):
    if request.method == 'POST':
        Cform = ContactForm(request.POST)
        if Cform.is_valid():
            Name = Cform.cleaned_data.get('Name')
            Mobile_Number = Cform.cleaned_data.get('Mobile_Number')
            Email = Cform.cleaned_data.get('Email')
            courses = Cform.cleaned_data.get('courses')
            trainers = Cform.cleaned_data.get('trainers')
            locations = Cform.cleaned_data.get('locations')
            shifts = Cform.cleaned_data.get('shifts')
            gender = Cform.cleaned_data.get('gender')
            start_date = Cform.cleaned_data.get('start_date')
            data = ContactDatabase(
                Name=Name,
                Mobile_Number=Mobile_Number,
                Email=Email,
                courses=courses,
                trainers=trainers,
                locations=locations,
                shifts=shifts,
                gender=gender,
                start_date=start_date,
            )
            data.save()
            Cform = ContactForm()
            messages.success(request,'data saved')
            context = {'Cform': Cform}
            return render(request, 'Institute/Contact.html', context)

        else:
            messages.warning(request, 'Enter valid data')
    else:
        Cform = ContactForm()
    context = {'Cform':Cform}
    return render(request,'Institute/Contact.html',context)




def Service_View(request):
    show = CoursesDatabase.objects.all()
    context = {'show':show}
    return render(request, 'Institute/Service.html',context)

def Feedback_View(request):
    if request.method == 'POST':
        Fform = FeedbackForm(request.POST)
        if Fform.is_valid():
            name = request.POST.get('name')
            ratting = request.POST.get('ratting')
            Feedback = request.POST.get('Feedback')
            data = FeedbackDatabase(
                name=name,
                ratting=ratting,
                Feedback=Feedback

            )
            data.save()
            messages.success(request,'data saved')
            Fform = FeedbackForm()
            Ffeedback = FeedbackDatabase.objects.all()
            context = {'Fform': Fform, 'Ffeedback': Ffeedback}
            return render(request, 'Institute/Feedback.html', context)
        else:
            messages.warning(request, 'Invalid data')

    else:
        Fform = FeedbackForm()
        Ffeedback = FeedbackDatabase.objects.all()
        context = {'Fform': Fform , 'Ffeedback':Ffeedback}
        return render(request,'Institute/Feedback.html',context)


def Gallery_View(request):
    return render(request, 'Institute/Gallery.html')

def Login_View(request):
    return render(request, 'Institute/Login.html')

