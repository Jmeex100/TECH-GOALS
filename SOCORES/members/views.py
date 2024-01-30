from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib import messages

# Create your views here.


def Login_page(requst):
    return render(requst,'members/login_page.html')