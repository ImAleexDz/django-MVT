from django.shortcuts import redirect, render
from fam.models import Family
from datetime import date
from .forms import PersonForm
# Create your views here.

def familiar(request):
    form = PersonForm()

    if request.method == 'POST':
        #print(request.POST)
        form = PersonForm(request.POST)

        if form.is_valid():
            print("Válido")

            person = Family()

            person.name = form.cleaned_data['name']
            person.lastname = form.cleaned_data['lastname']
            person.phone = form.cleaned_data['phone']
            person.birthday = form.cleaned_data['birthday']
            person.age = form.cleaned_data['age']

            person.save()
            return redirect('/family/list-family/')

        else:
            print("Inválido")

    return render(request, 'create_person.html', {'form': form})

def list_people(request):
    people = Family.objects.all()

    context = {
        'people': people
    }

    return render(request, 'list_family.html', context=context)


