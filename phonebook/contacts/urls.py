"""phonebook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from contacts import views

urlpatterns = [
    path('', views.home, name='home'),
    path('view_contacts/', views.view_contacts, name='view_contacts'),
    path('view_contacts/<int:id>', views.contact_details, name='contact_details'),
    path('add_new/', views.add_new, name='add_new'),
]




