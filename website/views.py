from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request,'home.html',{})


def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		#envoyer mail avec coordonées client
		send_mail(
			'Rendez-vous : ' + message_name,   #sujet
			message, #message
			message_email, #email client
			['emaildereception@gmail.com'],  #email du docteur
			fail_silently=False,  #signal si erreur dans emission

			)
		return render(request,'contact.html',{'message_name':message_name})
	else:
		return render(request,'contact.html',{})
	
