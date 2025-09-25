from typing import Any

from django.core.paginator import EmptyPage, Page, PageNotAnInteger, Paginator
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from contacts.form import ContactForm
from contacts.models import Contact


def paginate_contacts(request, all_contacts) -> Page[Any]:
    paginator = Paginator(all_contacts, 10)
    page = request.GET.get("page")
    try:
        return paginator.page(page)
    except PageNotAnInteger:
        return paginator.page(1)
    except EmptyPage:
        return paginator.page(paginator.num_pages)


def index(request) -> HttpResponse:
    form = ContactForm()
    all_contacts = Contact.objects.all().order_by("id")
    contacts = paginate_contacts(request, all_contacts)
    return render(request, "contacts/index.html", {"form": form, "contacts": contacts})


def edit(request, contact_id) -> HttpResponse:
    contact = get_object_or_404(Contact, id=contact_id)

    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect("contacts:index")
    else:
        form = ContactForm(instance=contact)
    return render(request, "contacts/edit.html", {"form": form, "contact": contact})


def delete(request, contact_id) -> HttpResponse:
    if request.method == "POST":
        Contact.objects.filter(id=contact_id).delete()
    return redirect("contacts:index")


def add(request) -> HttpResponse:
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("contacts:index")
    else:
        form = ContactForm()

    all_contacts = Contact.objects.all().order_by("id")
    contacts = paginate_contacts(request, all_contacts)
    return render(request, "contacts/index.html", {"form": form, "contacts": contacts})


def search(request) -> HttpResponse:
    q = request.GET.get("q")
    all_contacts = (
        Contact.objects.filter(
            Q(name__icontains=q) | Q(phone__icontains=q) | Q(email__icontains=q)
        )
        if q
        else Contact.objects.all()
    )
    contacts = paginate_contacts(request, all_contacts)
    return render(request, "contacts/index.html", {"contacts": contacts})
