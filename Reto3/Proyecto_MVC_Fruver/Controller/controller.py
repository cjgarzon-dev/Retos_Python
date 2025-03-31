from tkinter import messagebox

class ControllerShopping:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.cart = [] 

    def get_products(self):
        return self.model.products
    
    def reduce_stock(self):
        return self.model.quantity

    def add_to_cart(self, id_prod, quantity):  
        product = self.model.get_product(id_prod)
        if product:
            if quantity <= 0:
                raise ValueError('Valor incorrecto')
            if quantity > product.stock:
                raise ValueError("Stock insuficiente")
            self.cart.append({"producto": product.name, "cantidad": quantity, "precio_total": product.price * quantity})
            product.reduce_stock(quantity)
        else:
            raise ValueError("Producto no encontrado")
        
    def calculate_total(self):
        total = sum(item['precio_total'] for item in self.cart)
        return total

    def finish_shopping(self):
        total = sum(item["precio_total"] for item in self.cart)
        messagebox.showinfo('Compra finalizada', f'Total: ${total}')
        for item in self.cart:
            producto_id = next((p_id for p_id, p in self.model.products.items() if p.name == item["producto"]), None)
            if producto_id is not None:
                self.model.register_sale(producto_id, item["cantidad"])
            else:
                messagebox.showerror("Error", "Producto no encontrado en la tienda")

        if self.view:
            self.view.update_view_products() 
        self.cart.clear()
        self.view.reset_total()
        self.view.reset_cart()

    def get_sales_history(self):
        return self.model.history
    
    def get_products_cart(self):
        return self.cart