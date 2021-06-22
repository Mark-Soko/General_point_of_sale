from django.contrib import admin
from .models import product,cash_sales,category,credited_customer,credits

admin.site.register(product)
admin.site.register(cash_sales)
admin.site.register(category)
admin.site.register(credited_customer)
admin.site.register(credits)
