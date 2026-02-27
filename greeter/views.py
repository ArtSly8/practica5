from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .forms import NameForm
from .models import NameEntry

@require_http_methods(["GET", "POST"])
def home(request):
    greeting = None
    saved_name = None

    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            saved_name = form.cleaned_data["name"]
            NameEntry.objects.create(name=saved_name)
            greeting = f"Привет, {saved_name}!"
            form = NameForm()  # очистить поле после успешной отправки
    else:
        form = NameForm()

    last = NameEntry.objects.order_by("-id").first()
    if last and not greeting:
        greeting = f"Привет, {last.name}!"
        saved_name = last.name

    recent_names = NameEntry.objects.order_by("-id")[:10]

    return render(request, "greeter/home.html", {
        "form": form,
        "greeting": greeting,
        "saved_name": saved_name,
        "recent_names": recent_names,
    })
