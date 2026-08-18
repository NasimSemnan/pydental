from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from .models import Appointment, BlogPost, PortfolioItem


def home(request):
    services = [
        {"icon": "shield-check", "title": "Preventive care", "copy": "Healthy habits and early attention keep small concerns from becoming big ones.", "dark": True},
        {"icon": "sun", "title": "Cosmetic dentistry", "copy": "Subtle, natural-looking improvements that let your best smile shine through.", "dark": False},
        {"icon": "gem", "title": "Restorative care", "copy": "Thoughtful solutions that bring back comfort, function, and confidence.", "dark": False},
        {"icon": "zap", "title": "Emergency visits", "copy": "When you need us, we make room. Same-day appointments are often available.", "dark": False},
    ]
    faqs = [
        {"question": "Do you accept my dental insurance?", "answer": "We work with most major PPO plans and will gladly help you understand your benefits before your visit. We also offer flexible payment options for everyone."},
        {"question": "What should I expect at my first visit?", "answer": "Your first visit is a relaxed conversation, comprehensive exam, and time to ask every question on your mind. We will create a care plan together, with no pressure."},
        {"question": "Do you see children?", "answer": "Absolutely. We welcome growing smiles and make visits easy, playful, and educational for children of all ages."},
        {"question": "How often should I visit?", "answer": "Most patients benefit from a cleaning and checkup every six months. We will recommend a schedule tailored to your smile."},
    ]
    portfolio = PortfolioItem.objects.filter(is_featured=True)[:3]
    return render(request, "index.html", {"services": services, "faqs": faqs, "portfolio": portfolio})


def portfolio(request):
    items = PortfolioItem.objects.filter(is_featured=True)
    return render(request, "portfolio/index.html", {"items": items})


def blog(request):
    posts = BlogPost.objects.filter(is_published=True, published_at__lte=timezone.now())
    return render(request, "blog/index.html", {"posts": posts})


def blog_detail(request, slug):
    post = get_object_or_404(
        BlogPost,
        slug=slug,
        is_published=True,
        published_at__lte=timezone.now(),
    )
    return render(request, "blog/detail.html", {"post": post})


def contact(request):
    if request.method != "POST":
        return redirect("home")

    name = request.POST.get("name", "").strip()
    email = request.POST.get("email", "").strip()
    service = request.POST.get("service", "").strip()
    message = request.POST.get("message", "").strip()

    if not name or not email or not service:
        messages.error(request, "Please complete your name, email, and service preference.")
        return redirect("home")

    Appointment.objects.create(
        name=name,
        email=email,
        service=service,
        message=message,
    )
    messages.success(request, f"Thanks, {name.split()[0]}! We received your request and will be in touch shortly.")
    return redirect("home")
