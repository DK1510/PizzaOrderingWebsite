# Pizza Ordering Site with Django Forms

## Overview

This Django project is a pizza ordering site that utilizes Django forms for a seamless user experience. The application consists of models for pizza size and pizza details. Users can place orders, edit them, and order multiple pizzas through the provided forms.

## Models

### Size

- **title**: Char field (max length = 50)

### Pizza

- **topping1**: Char field (max length = 100)
- **topping2**: Char field (max length = 100)
- **size**: Foreign Key from Size

## Views

### Homepage

- Renders `home.html`

### Order

- Renders `order.html`
- Allows users to order pizza using Django model form (`PizzaForm`).

### Edit

- Renders `edit.html`
- Enables users to edit their placed orders.

### Pizzas

- Renders `pizzas.html`
- Allows users to order multiple pizzas using Django formset (`MultiplePizzaForm`).

## Forms

### PizzaForm

- Model form for the `Pizza` model with fields: `topping1`, `topping2`, `size`.

### MultiplePizzaForm

- Django form with a field `number` to generate formset.
- Formset replicates the `PizzaForm` as many times as mentioned in the `MultiplePizzaForm`.

## Templates

### base.html

- Acts as the base template for all other templates.
- Includes head, CSS, JS, and a navigation bar.

### home.html

- Homepage for the project.

### order.html

- Allows users to place an order using the Django model form.

### edit.html

- Allows users to edit their placed orders.

### pizzas.html

- Formset template used to place multiple pizzas.

## How to Run

1. Clone the repository: `git clone https://github.com/your-username/your-repo.git`
2. Navigate to the project directory: `cd your-repo`
3. Install dependencies: `pip install -r requirements.txt`
4. Apply migrations: `python manage.py migrate`
5. Create a superuser: `python manage.py createsuperuser`
6. Run the development server: `python manage.py runserver`
7. Access the site at [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
