from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from src.referral_system.forms import MyInputForm
from account.models import MyUser
from src.referral_system.cache import create, get, delete

# Create your views here.


@login_required
def create_referral_view(request):
    form = MyInputForm()

    if form.is_valid():
        username = request.user.username
        data = str(form['data'])
        if get(username):
            delete(data)
            delete(username)

        create(username, data)
        create(data, username)

    return render(request, 'referral_system/test_create.html', {'form': form})


@login_required
def delete_referral_view(request):
    form = MyInputForm(request.post)

    if form.is_valid():
        username = request.user.username
        data = get(username)
        delete(username)
        delete(data)

    return


@login_required
def add_referral_view(request):
    form = MyInputForm(request.post)
    data = str(form['data'])
    referral_name = get(data)
    if not referral_name:
        return HttpResponseNotFound('Такой реферральной ссылки не существует!')
    user = request.user
    user.referred_by = referral_name
    user.save()

    return


@login_required
def get_referrals_view(request):
    username = request.user.username
    referrals = MyUser.objects.values('username').filter(referred_by=username)

    return
