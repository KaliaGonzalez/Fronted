from django.shortcuts import render
import requests


def user_list(request):
    response = requests.get('http://localhost:8080/api/users')  # URL del backend
    users = response.json()
    return render(request, 'user_list.html', {'users': users})