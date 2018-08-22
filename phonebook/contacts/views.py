from django.shortcuts import HttpResponse, render, redirect
from .models import Contact

# Create your views here.

def home(request):
	# return HttpResponse('<h1>Welcome to the contacts app</h1>')

	context = {}
	context['title'] = 'Phonebook App v1.4'
	context['developer'] = 'Vinod Kumar Kayartaya'
	context['developer_email'] = 'vinod@vinod.co'

	return render(request, 'contacts/home.html', context)

def view_contacts(request):
	context = dict()
	contacts = Contact.objects.all()
	context['contacts'] = contacts
	context['total_contacts'] = len(contacts)

	return render(request, 'contacts/view_all.html', context)


def contact_details(request, id):

	context = dict()
	try:
		contact = Contact.objects.get(pk=id)
		context['contact'] = contact
	except(Exception):
		return redirect('view_contacts')

	return render(request, 'contacts/details.html', context)


def add_new(request):

	c = Contact()
	c.name = request.POST['name']
	c.email = request.POST['email']
	c.phone = request.POST['phone']
	c.address = request.POST['address']
	
	c.save()

	return redirect('view_contacts')









