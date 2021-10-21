from django.shortcuts import render
from .forms import ReachOutForm


# Create your views here.

def homepage(request):
    form = ReachOutForm()
    return render(request, 'basesite/homepage.html', {'reachoutform': form})


def send_file_to_user(request):
    if request.method == 'POST':
        filled_form = ReachOutForm(request.POST)
        if filled_form.is_valid():
            note = 'תודה על הרשמתך, הקובץ בדרך אלייך'
            new_form = ReachOutForm()
            return render(request, 'basesite/thanks.html', {'note': note})
    else:
        form = ReachOutForm()
        return render(request, 'basesite/homepage.html', {'reachoutform': form})


def about(request):
    return render(request, 'basesite/about.html')