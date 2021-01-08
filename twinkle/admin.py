from django.contrib import admin

# Register your models here.
from twinkle.models import parents,children,payments

admin.site.register(parents)
admin.site.register(children)
admin.site.register(payments)

# admin.site.register(paymentone)
# admin.site.register(paymenttwo)
# admin.site.register(paymentthree)
# admin.site.register(paymentfour)

#admin.site.register(payment)
