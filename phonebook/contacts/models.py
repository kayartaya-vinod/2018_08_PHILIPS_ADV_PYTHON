from django.db import models

# Create your models here.


class Contact(models.Model):
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=150)
	phone = models.CharField(max_length=50)
	address = models.CharField(max_length=255)

	def __str__(self):
		return 'id={}, name={}, email={}, phone={}, address={}'.format(
			self.id, self.name, self.email, self.phone, self.address)