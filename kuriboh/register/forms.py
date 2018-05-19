from django import forms

class LoginForm(forms.Form):
	name = forms.CharField()
	passwd = forms.CharField()

	def login_account(self):
		pass

