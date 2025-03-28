from Model.model import Shopping
from Controller.controller import ControllerShopping  
from View.view import ViewShopping 
model = Shopping()

# Agregado de productos de ejemplo
model.add_product(1, 'Manzana', 1500, 100)
model.add_product(2, 'Pera', 1000, 100)
model.add_product(3, 'Banana', 400, 100)
model.add_product(4, 'Naranja', 500, 100)
model.add_product(5, 'Uva', 200, 100)
model.add_product(6, 'Sandía', 2500, 100)  
model.add_product(7, 'Mango', 1800, 100)  
model.add_product(8, 'Maracuya', 900, 100)  
model.add_product(9, 'Limon', 300, 100)  
model.add_product(10, 'Melon', 1700, 100)  

controller = ControllerShopping(model, None)  
view = ViewShopping(controller)
controller.view = view