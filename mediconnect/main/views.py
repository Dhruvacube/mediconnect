from django.shortcuts import render
from asgiref.sync import sync_to_async
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *
from django.contrib import messages

@sync_to_async
@login_required
def home(request):
    no_of_feedback_question = GeneralDiagnosticQuestions.objects.count()
    if request.method == "POST":
        data={}
        for i in range(no_of_feedback_question):
            data[i]=request.POST.get("question"+str(i))
        Feedback.objects.create(patient=request.user, feedback=data)
        messages.success(request, "Feedback submitted successfully")
    return render(request, "index.html", {"questions": GeneralDiagnosticQuestions.objects.all()})

@sync_to_async
@login_required
@csrf_exempt
@require_POST
def data_acquisition(request):
    username = request.POST.get("username")
    doctor = Doctor.objects.get(user__username=username)
    appointment_id = request.POST.get("appointment_id")
    data = request.POST.get("data")
    
    return HttpResponse("OK")

