from django import forms
from datetime import date
from twinkle.models import parents,children,payments

class parentForm(forms.ModelForm):
    father_firstname = forms.CharField(max_length=100)
    father_lastname = forms.CharField(max_length=100)
    father_phonenumber_one = forms.IntegerField()
    father_phonenumber_two = forms.IntegerField()
    mother_firstname = forms.CharField(max_length=100)
    mother_lastname = forms.CharField(max_length=100)
    mother_phonenumber_one = forms.IntegerField()
    mother_phonenumber_two = forms.IntegerField()
    address = forms.CharField(max_length=100)

    class Meta:
        model = parents
        fields =('father_firstname','father_lastname','father_phonenumber_one','father_phonenumber_two','mother_firstname'
                    ,'mother_lastname','mother_phonenumber_one','mother_phonenumber_two','address')


class childrenForm(forms.ModelForm):
    #tutorial_category = models.ForeignKey(TutorialCategory, default=1, verbose_name="Category", on_delete=models.SET_DEFAULT)
    #parent = forms.ForeignKey(parents,default=1,verbose_name="parent",on_delete=models.SET_DEFAULT)
    firstname = forms.CharField(max_length=100)
    middlename = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    classlevel = forms.CharField(max_length=100)
    age = forms.IntegerField()
    time_of_study = forms.CharField(max_length=100)
    campus = forms.CharField(max_length=100)

    class Meta:
        model = children
        exclude = ('parent',)

class payments_form(forms.ModelForm):
    child = forms.IntegerField()
    amount = forms.IntegerField()
    time = forms.DateField()
    bank = forms.CharField(max_length=100)
    term = forms.IntegerField()
    year = forms.IntegerField()
    installment = forms.IntegerField()

    class Meta:
        model = payments
        exclude = ('id',)

# class payment_one_form(forms.ModelForm):
#     amount = forms.IntegerField()
#     date = forms.DateField()
#     bank = forms.CharField(max_length=100)
#     term = forms.IntegerField()
#     year = forms.IntegerField()

#     class Meta:
#         model = paymentone
#         fields = ('amount','date','bank','term','year',)

# class payment_two_form(forms.ModelForm):
#     amount = forms.IntegerField()
#     date = forms.DateField()
#     bank = forms.CharField(max_length=100)
#     term = forms.IntegerField()
#     year = forms.IntegerField()

#     class Meta:
#         model = paymenttwo
#         fields = ('amount','date','bank','term','year',)

# class payment_three_form(forms.ModelForm):
#     amount = forms.IntegerField()
#     date = forms.DateField()
#     bank = forms.CharField(max_length=100)
#     term = forms.IntegerField()
#     year = forms.IntegerField()

#     class Meta:
#         model = paymentthree
#         fields = ('amount','date','bank','term','year',)

# class payment_four_form(forms.ModelForm):
#     amount = forms.IntegerField()
#     date = forms.DateField()
#     bank = forms.CharField(max_length=100)
#     term = forms.IntegerField()
#     year = forms.IntegerField()

#     class Meta:
#         model = paymentfour
#         fields = ('amount','date','bank','term','year',)
# class payment_form(forms.ModelForm):
#     child = forms.IntegerField()
#     #paymentone = forms.IntegerField()
#     #paymenttwo = forms.IntegerField()
#     #paymentthree = forms.IntegerField()
    
#     class Meta:
#         model = payment
#         fields = ('child',)