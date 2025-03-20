from Model.model import Shopping
from Controller.controller import ControllerShopping  
from View.view import ViewShopping 
model = Shopping()

# Agregado de productos de ejemplo
model.add_product(1, 'Manzana', 1.5, 100)
model.add_product(2, 'Pera', 2, 100)
model.add_product(3, 'Banana', 1, 100)
model.add_product(4, 'Naranja', 1.5, 100)
model.add_product(5, 'Uva', 3, 100)
model.add_product(6, 'Sandía', 5, 100)  

controller = ControllerShopping(model, None)  
view = ViewShopping(controller)
controller.view = view