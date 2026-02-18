from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime
from django.contrib import messages
from .models import Contact
from django.db import models

def index(request):

    if request.method == "POST":

        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        subject = request.POST.get("subject", "").strip()
        message = request.POST.get("message", "").strip()
        contact = request.POST.get("contact", "").strip()
        date = models.DateTimeField(auto_now_add=True) 
        # date = models.Text

        # 🔥 IMPORTANT VALIDATION
        if name and email and message:

            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message,
                contact=contact,
                date = date,
            )

            send_mail(
                subject=f"New Contact from {name}",
                message=f"Name: {name}\nEmail: {email}\n\nSubject: {subject}\n\nMessage:\n{message}",
                from_email=settings.EMAIL_HOST_USER,  # ⚠️ quotes काढले
                recipient_list=['mpawarraj102102@gmail.com'],
                fail_silently=False,
            )
        messages.success(request, 'Your message hs been sent')
        return redirect("/")   # PRG Pattern

    return render(request, "index.html")
