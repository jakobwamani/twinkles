from django.conf.urls import url
from twinkle import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^register/$',views.register,name='register'),
    url(r'^about/$',views.about,name='about'),
    url(r'^parents/$',views.view_parent,name='view_parents'),
    url(r'^children/$',views.view_children,name='view_children'),
    url(r'^addpayments/',views.view_payments,name='view_payments'),
    url(r'^payments/$',views.add_payments,name='add_payments'),
    url(r'^show_payment_history/$',views.show_payment_history,name='show_payment_history'),

    # url(r'^paymentone/',views.add_payment_one,name='add_payment_one'),
    # url(r'^paymenttwo/$',views.add_payment_two,name='add_payment_two'),
    # url(r'^paymentthree/$',views.add_payment_three,name='add_payment_three'),
    # url(r'^paymentfour/$',views.add_payment_four,name='add_payment_four'),
]