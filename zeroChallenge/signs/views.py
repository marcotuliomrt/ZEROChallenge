from django.shortcuts import render, redirect
from .models import Sign


def index(request, solved_status=None):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        return redirect('index')
    else:
        if solved_status is None:
            signs = Sign.objects.all()
        else:
            signs = Sign.objects.filter(solved=(solved_status == 'True'))

        context = {'signs': signs, 'solved_status': solved_status}
        return render(request, 'signs/index.html', context)
    
        # all_signs = Sign.objects.all()
        # return render(request, 'signs/index.html', {'signs': all_signs})
    