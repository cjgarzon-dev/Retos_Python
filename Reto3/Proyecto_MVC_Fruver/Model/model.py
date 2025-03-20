class Product:
    def __init__(self, id_prod, name, price, stock):
        self.id_prod = id_prod
        self.name = name
        self.price = price
        self.stock = stock

    def reduce_stock(self, quantity):
        if quantity > self.stock:
            raise ValueError('No hay suficiente stock')
        self.stock -= quantity

class Shopping:
    def __init__(self):
        self.products = {}  # Diccionario para almacenar productos por su id
        self.history = []  # Lista para almacenar el historial de ventas

    def add_product(self, id_prod, name, price, stock):
        """Añade un producto a la lista de productos."""
        self.products[id_prod] = Product(id_prod, name, price, stock)  

    def get_product(self, id_prod):
        """Busca un producto por su id y lo retorna."""
        return self.products.get(id_prod, None) 
    
    def register_sale(self, id_prod, quantity):
        """Registra una venta y actualiza el stock del producto."""
        product = self.get_product(id_prod)
        if product:
            product.reduce_stock(quantity)
            total = product.price * quantity
            self.history.append({
                "Nombre": product.name,
                "Cantidad": quantity,
                "Precio_total": total
            })
        else:
            raise ValueError('Producto no encontrado')