from django import forms
from .models import Pizza
# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label='Topping1',max_length=50,widget=forms.Textarea)
#     topping2 = forms.CharField(label='Topping2', max_length=50,widget=forms.PasswordInput)
#     size = forms.ChoiceField(label='Size',choices=[('Small','Small'),('Medium','Medium'),('Large','Large')],widget=forms.CheckboxSelectMultiple)


class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ['topping1','topping2','size']
        labels = {'topping1':'Topping 1','topping2':'Topping2'}


class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2,max_value=10)

