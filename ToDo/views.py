from django.shortcuts import render, redirect
from .models import mytask
from .forms import task_form


def regi_task(request, id=0):
    workall = mytask.objects.all()
    if request.method == "GET":
        if id == 0:
            form = task_form()
        else:
            work = mytask.objects.get(pk=id)
            form = task_form(instance=work)
        return render(request, 'index.html', {'f': form, 'w': workall})
    else:
        if id == 0:
            form = task_form(request.POST)
        else:
            work = mytask.objects.get(pk=id)
            form = task_form(request.POST, instance=work)
        if form.is_valid():
            form.save()
            return redirect('/todo/')
        return render(request, 'index.html', {'f': form, 'w': work})


def Delete(request, id):
    dele = mytask.objects.get(pk=id)
    dele.delete()
    return redirect('/todo/')
