from django.shortcuts import render
from django.core.mail import send_mail
from .forms import ContactForm
from django.conf import settings
from django.http import HttpResponse

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # Send email
            send_mail(
                subject=f"New message from {contact.name}",
                message=contact.message + f"\n\nSender Email: {contact.email}",
                from_email=settings.EMAIL_HOST_USER,   # your Gmail
                recipient_list=[settings.EMAIL_HOST_USER],  # send to yourself
                fail_silently=False,
            )

            return render(request, 'contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
def send_test_email(request):
    send_mail(
        subject="Test Email",
        message="This is a test email from Django.",
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.EMAIL_HOST_USER],
        fail_silently=False,
    )
    return HttpResponse("Test email sent successfully!")