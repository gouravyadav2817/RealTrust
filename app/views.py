from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactSubmission, Project,  Client, NewsletterSubscription
from .forms import ContactForm

def subscribe(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').strip()
        if email:
            subscription, created = NewsletterSubscription.objects.get_or_create(email=email)
            if created:
                messages.success(request, '🎉 You’ve successfully subscribed!')
            else:
                messages.info(request, 'ℹ️ You’re already on our list.')
        else:
            messages.error(request, '⚠️ Please enter a valid email address.')
    return redirect('home')


def home(request):
    contact_form = ContactForm(request.POST or None)
    if request.method == 'POST' and contact_form.is_valid():
        contact_form.save()
        messages.success(request, '📨 Your information has been sent!')
        return redirect('home')

    context = {
        'contact_form': contact_form,
        'projects':     Project.objects.all(),
        'clients':      Client.objects.all(),
    }
    return render(request, 'app/home.html', context)