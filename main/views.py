from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306165950',
        'name': 'Orlando Devito',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)