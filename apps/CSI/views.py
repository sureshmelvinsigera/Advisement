from django.shortcuts import render
from apps.CSI.forms import StudentAdvisementForm


# Create your views here.

def index_view(request):
    if request.method == 'POST':
        form = StudentAdvisementForm(request.POST)
        if form.is_valid():
            pass
        else:
            print(form.errors)
    else:
        form = StudentAdvisementForm()
        return render(request, 'public/index.html', {'studentadvisementform': form})
