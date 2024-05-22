from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from src.referral_system.forms import MyInputForm
from account.models import MyUser
from src.referral_system.cache import create, get, delete

# Create your views here.


@login_required
def create_referral_view(request):
    form = MyInputForm(request.POST)

    if request.method == 'POST' and form.is_valid():
        username = request.user.username
        data = form.cleaned_data['data']
        if get(username):
            delete(data)
            delete(username)

        create(username, data)
        create(data, username)

    return render(request, 'referral_system/test_create.html', {'form': form})


@login_required
def delete_referral_view(request):
    username = request.user.username
    data = get(username)
    delete(username)
    delete(data)

    return redirect('home')


@login_required
def add_referral_view(request):
    form = MyInputForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data['data']
        referral_name = get(data)
        if referral_name:
            username = request.user
            user = MyUser.objects.get(username=username)
            user.referred_by = referral_name
            user.save()
        else:
            return HttpResponseNotFound('Такой реферральной ссылки не существует!')

    return render(request, 'referral_system/test_add_referral.html', {'form': form})


@login_required
def show_referrers_view(request):
    username = request.user.username
    referrals = MyUser.objects.values('username').filter(referred_by=username)
    context = {'referrals': referrals}
    return render(request, 'referral_system/test_get_referrals.html', context)
