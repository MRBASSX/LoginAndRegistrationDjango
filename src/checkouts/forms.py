from django import forms
from .models import Checkout


# creating a form
class CheckoutForm(forms.ModelForm):

	# create meta class
	class Meta:
		# specify model to be used
		model = Checkout

		# specify fields to be used
		fields = [
            "email",
			"first_name",
            "surname",
			"last_name",
            "address",
            ]

		# add Bootstrap
		widgets = {
			'email' : forms.TextInput(attrs= {'placeholder':'user', 'style':'width:100%','class':"form-control"}),
			'first_name' : forms.TextInput(attrs= {'placeholder':'user', 'style':'width:100%','class':"form-control"}),
			'surname' : forms.TextInput(attrs= {'placeholder':'user', 'style':'width:100%','class':"form-control"}),
			'address' : forms.TextInput(attrs= {'placeholder':'user', 'style':'width:100%','class':"form-control"}),
			'last_name' : forms.TextInput(attrs= {'placeholder':'user', 'style':'width:100%','class':"form-control"}),
			}
		
		