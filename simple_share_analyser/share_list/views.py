from django.shortcuts import render
from .models import Share
from .forms import ShareForm
from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
from django.urls import reverse
import json


def home(request):
    return render(request, 'home.html')


def share_list(request):
    shares = Share.objects.extra(select={'d_field': 'price / amount'}).extra(order_by=['d_field'])

    if request.method == 'DELETE':
        id = json.loads(request.body)['id']
        shares = Share.objects.get(pk=id)
        shares.delete()

    return render(request, 'share_list.html', {"shares": shares})


def share_list_bought(request):
    shares = Share.objects.extra(select={'d_field': 'price / amount'}).extra(order_by=['d_field']).filter(type_of_trade='Bought')

    if request.method == 'DELETE':
        id = json.loads(request.body)['id']
        shares = Share.objects.get(pk=id)
        shares.delete()

    return render(request, 'share_list.html', {"shares": shares})


def share_list_sold(request):
    shares = Share.objects.extra(select={'d_field': 'price / amount'}).extra(order_by=['d_field']).filter(type_of_trade='Sold')

    if request.method == 'DELETE':
        id = json.loads(request.body)['id']
        shares = Share.objects.get(pk=id)
        shares.delete()

    return render(request, 'share_list.html', {"shares": shares})


def share_form(request):
    form = ShareForm()
    if request.method == "POST":
        form = ShareForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(redirect_to=reverse("share_list"))
    context = {'form': form}
    return render(request, 'share_form.html', context)


def share_delete(request, id):
    context = {}
    obj = get_object_or_404(Share, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect(redirect_to=reverse("share_list"))

    return render(request, "share_delete.html", context)


