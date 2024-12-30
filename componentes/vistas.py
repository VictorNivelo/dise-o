from django.shortcuts import render


def botones(request):
    return render(request, "botones.html")

def entradas(request):
    return render(request, "entradas.html")
