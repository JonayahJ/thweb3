# Contact views
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Inquiry form link
def inquiry(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        # sent_date = request.POST['sent_date']

        contact = Contact(
            first_name=first_name, 
            last_name=last_name, 
            email=email, 
            phone=phone, 
            message=message, 
            # sent_date=sent_date
        )

        #getting superuser email address
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        # Sending an email
        send_mail(
            'New contact inquiry submission from ' + first_name + ' ' + last_name + ' for Think Halcyon', # subject
            message, # message
            email, # from field
            ['jonayah@thinkhalcyon.com'], # to field
            fail_silently=False,
        )

        contact.save()
        messages.success(request, "Thanks for reaching out! We'll be in touch shortly.")

        return redirect('thankyou') # Return to contact page

# Thank You page
def thankyou(request):
    return render(request, "thankyou.html", {})