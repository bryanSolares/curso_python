from django.db import models
from django.db.models import Q


class CustomerManager(models.Manager):
    def get_all_customers(self):
        return self.all().values('id', 'name', 'last_name', 'status')

    def get_customer_by_name(self, name):
        return self.filter(name__icontains=name).order_by('id').values('id', 'name', 'last_name', 'status')

    def get_customer_and_interests(self, name):
        return self.filter(name__icontains=name).order_by('id').values('id', 'name', 'last_name', 'status', 'interests')

    def get_customer_and_interests_by_id(self, identity):
        return self.filter(id=identity).order_by('id').values('id', 'name', 'last_name', 'status', 'interests')

    def get_customer_by_id(self, identity):
        customer = self.get(id=identity)
        return customer.interests.all()

    def get_interests_by_id_customer(self, identity):
        return self.filter(interests__id=identity)

