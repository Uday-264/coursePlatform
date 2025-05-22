from django.shortcuts import render
from emails.forms import EmailForm
from emails.models import Email,EmailVerificationEvent
from emails import services

def login_logout_template_view(request):
    return render(request,"auth/login-logout.html",{})

def home(request,*args,**kwargs):
    template='home.html'
    form=EmailForm(request.POST or None)
    context={
        "form":form,
        "message":""
    }
    if form.is_valid():
        email_val=form.cleaned_data.get('email')
        obj=services.start_verification_event(email_val)
        context["form"]=EmailForm()
        context["message"]="Success,Please check your email"
    else:
        print(form.errors)
    return render(request,template,context)