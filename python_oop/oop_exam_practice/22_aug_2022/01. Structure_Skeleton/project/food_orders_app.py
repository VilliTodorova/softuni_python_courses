from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter


class FoodOrdersApp:
    VALID_FOOD_TYPES = {"Starter": Starter, "MainDish": MainDish, "Dessert": Dessert}
    receipt_id = 1

    def __init__(self):
        self.menu = []
        self.clients_list = []

    def register_client(self, client_phone_number: str):
        client = self._find_client_by_phone(client_phone_number)
        if client:
            raise Exception("The client has already been registered!")

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)

        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if type(meal).__name__ in self.VALID_FOOD_TYPES:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        result = []
        for meal in self.menu:
            result.append(meal.details())

        return "\n".join(result)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        client = self._find_client_by_phone(client_phone_number)
        current_order = []
        current_bill = 0

        if client is None:
            self.register_client(client_phone_number)   # maybe will throw an error, simply add them to the list

        for meal_name, order_quantity in meal_names_and_quantities.items():
            for meal in self.menu:
                if meal.name == meal_name:
                    if meal.quantity >= order_quantity:
                        current_order.append(meal)
                        current_bill += meal.price * order_quantity
                        break
                    else:
                        raise Exception(f"Not enough quantity of {type(meal).__name__}: {meal_name}!")
            else:
                raise Exception(f"{meal_name} is not on the menu!")

        client.shopping_cart.extend(current_order)
        client.bill += current_bill

        for meal_name, meal_quantity in meal_names_and_quantities.items():

            if meal_name not in client.ordered_meals:
                client.ordered_meals[meal_name] = 0
            client.ordered_meals[meal_name] += meal_quantity

            for meal in self.menu:
                if meal.name == meal_name:
                    meal.quantity -= meal_quantity
                    break

        return f"Client {client_phone_number} successfully ordered {', '.join(m.name for m in client.shopping_cart)} " \
               f"for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self._find_client_by_phone(client_phone_number)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        for ordered_meal, quantity in client.ordered_meals.items():
            for menu_meal in self.menu:
                if ordered_meal == menu_meal.name:
                    menu_meal.quantity += quantity
        client.shopping_cart = []
        client.bill = 0
        client.ordered_meals = {}

        return f"Client {client_phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self._find_client_by_phone(client_phone_number)

        if not client.shopping_cart:
            raise Exception("There are no ordered meals!")

        money_paid = client.bill
        current_receipt_id = self.receipt_id
        client.shopping_cart = []
        client.bill = 0
        client.ordered_meals = {}

        self.receipt_id += 1

        return f"Receipt #{current_receipt_id} " \
               f"with total amount of {money_paid:.2f} was successfully paid for {client_phone_number}."

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

    #   helper methods

    def _find_client_by_phone(self, phone):
        client = [c for c in self.clients_list if c.phone_number == phone]

        return client[0] if client else None

