from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
from .forms import SignUpForm,ContactForm

def home(request):
	title="welcome"
	#f request.user.is_authenticated():
	#title="my title %s"%(request.user) #concatanation in python
	#add a form
	#f request.method == "POST":
	#print request.POST
	form=SignUpForm(request.POST or None)
	context = {
		"title": title,
		"abc": 123,
		"form":form,
	}

	if form.is_valid():
		#form.save()
		instance=form.save(commit=False)
		full_name=form.cleaned_data.get("full_name")
		
		if not full_name:
			full_name="new full name"
		instance.full_name=full_name
		instance.save()
		context={
		"title": "thank you"
		}
		#print instance.email
		#print instance.timestamp
		#instance.save()
	return render(request,"home.html",context)

def contact(request):
	form=ContactForm(request.POST or None)
	if form.is_valid():
		#for key,value in form.cleaned_data.iteritems():
		#	print key,value
			#print form.cleaned_data.get(key)
			form_email=form.cleaned_data.get("email")
			form_full_name=form.cleaned_data.get("full_name")
			form_message=form.cleaned_data.get("message")
			subject='first mail'
			from_email=settings.EMAIL_HOST_USER
			to_email=[from_email,'aniket.marlapalle@gmail.com']
			contact_message="%s: %s via %s"%(
			form_full_name,
			form_message,
			form_email)

			send_mail(subject,contact_message,from_email,to_email,fail_silently=True)
	
	context={
		"form":form,
	}
	return render(request,"forms.html",context)
