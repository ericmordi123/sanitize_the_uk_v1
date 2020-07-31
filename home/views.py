from django.shortcuts import render

from .forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse

# Create your views here.

def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')

def about(request):
    """ A view to return the about us page """

    return render(request, 'home/about.html')

def contact(request):
    """ A view to return the about us page """

    return render(request, 'home/contact.html')

def contact_form(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = f'Message from {form.cleaned_data["name"]}'
            message = form.cleaned_data["message"]
            sender = form.cleaned_data["email"]
            recipients = ['info@sanitizetheuk.com']
            try:
                send_mail(subject, message, sender, recipients, fail_silently=True)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return HttpResponse('Success...Your email has been sent')

    return render(request, 'home/contact.html', {'form': form})