from django.contrib import admin

# Register your models here.
from .models import Role, Admin, Category, Supplier, Product

admin.site.register(Role)
admin.site.register(Admin)
admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Product)
