from django.shortcuts import render
from .forms import PizzaForm,MultiplePizzaForm
from django.forms import formset_factory
from .models import Pizza
# Create your views here.
def homepage(request):
    return render(request,'pizza/home.html')


def order(request):
    multiple_pizza_form = MultiplePizzaForm()   #empty form
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.id
            note = 'Thanks for ordering %s %s and %s pizaa!!'%(filled_form.cleaned_data['size'],filled_form.cleaned_data['topping1'],filled_form.cleaned_data['topping2'])
            new_form = PizzaForm()
            return render(request, 'pizza/order.html', {'pizzaform': new_form,'note':note,'pizzas_form':multiple_pizza_form,'created_pizza_pk':created_pizza_pk})

    else:
        form = PizzaForm()  #contructor
        return render(request,'pizza/order.html',{'pizzaform':form,'pizzas_form':multiple_pizza_form})

def pizzas(request):
    number_of_pizzas = 2
    multiple_filled_form = MultiplePizzaForm(request.GET)
    if multiple_filled_form.is_valid():
        number_of_pizzas = multiple_filled_form.cleaned_data['number']
        print(multiple_filled_form['number'])
        print(number_of_pizzas)

    PizzaFormSet = formset_factory(PizzaForm,extra =number_of_pizzas)
    FormSet = PizzaFormSet()
    note = ''
    if request.method == 'POST':
        l = []
        filled_multiple_form = PizzaFormSet(request.POST)
        if filled_multiple_form.is_valid():
            for form in filled_multiple_form:
                created_pizza = form.save()
                created_pizza_pk = created_pizza.id
                l.append(created_pizza_pk)
            note = 'Order placed!!'
        else:
            note = 'Order not placed, please try again'
        return render(request, 'pizza/pizzas.html', {'formset': filled_multiple_form,'note':note})

    else:
        return render(request, 'pizza/pizzas.html',{'formset':FormSet})

def edit(request,pk):
    form_obj = Pizza.objects.get(pk = pk)
    form = PizzaForm(instance=form_obj)
    note = ''
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST,instance=form_obj)
        if filled_form.is_valid():
            filled_form.save()
            note = 'Your Order Edited Successfully!!'
        else:
            note = 'Order not edited, please try again....'
        return render(request, 'pizza/edit.html', {'pizzaform': filled_form, 'pizza': form_obj,'note':note})
    else:
        return  render(request,'pizza/edit.html',{'pizzaform':form,'pizza':form_obj})

