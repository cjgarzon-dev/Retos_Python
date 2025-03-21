import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class ViewShopping:
    def __init__(self, controller):
        self.controller = controller
        self.controller.view = self
        self.window = tk.Tk()
        self.window.title("CAJA FRUVER - Frutas y Verduras")
        self.window.geometry("800x600")

        # Cargar imagen de fondo
        self.bg_image = Image.open('../Retos_Python/Reto3/Proyecto_MVC_Fruver/View/background.jpg')
        self.bg_image = self.bg_image.resize((800, 600), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.bg_image)

        self.canvas = tk.Canvas(self.window, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")

        self.configure_interface()  
        self.load_products()  
        self.window.mainloop()  
        
    def configure_interface(self):
        # Crear Treeview para mostrar productos
        self.treeview_products = ttk.Treeview(self.window, columns=("Name", "Price", "Stock"), show="headings")
        self.treeview_products.heading("Name", text="Nombre")
        self.treeview_products.heading("Price", text="Precio")
        self.treeview_products.heading("Stock", text="Stock")

        # Entradas y botones de la interfaz
        self.entry_quantity = tk.Entry(self.window)
        self.button_add_product = tk.Button(self.window, text="Agregar Producto", command=self.add_product)
        self.button_finish = tk.Button(self.window, text="Finalizar Compra", command=self.controller.finish_shopping)
        self.button_history = tk.Button(self.window, text="Ver Historial de Ventas", command=self.show_history)  # Nuevo botón para ver historial
        self.etiqueta_total = tk.Label(self.window, text="Total: $0.00")
        
        # Ubicar elementos en el Canvas
        self.canvas.create_window(400, 150, window=self.treeview_products)
        self.canvas.create_window(400, 350, window=self.entry_quantity)
        self.canvas.create_window(400, 400, window=self.button_add_product)
        self.canvas.create_window(400, 450, window=self.button_finish)
        self.canvas.create_window(400, 500, window=self.etiqueta_total)
        self.canvas.create_window(400, 550, window=self.button_history)  # Posicionar el nuevo botón

    def load_products(self):
        # Insertar productos en el Treeview desde el controlador
        for id_product, product in self.controller.get_products().items():
            self.treeview_products.insert("", "end", iid=str(id_product), values=(product.name, product.price, product.stock))

    def add_product(self):
        try:
            selected_item = self.treeview_products.selection()
            if not selected_item:
                raise ValueError('Debe Seleccionar un producto de la lista.')
            selected_item = self.treeview_products.selection()[0]
            id_producto = int(selected_item)
            quantity = int(self.entry_quantity.get())
            self.controller.add_to_cart(id_producto, quantity)
            messagebox.showinfo("Éxito", "Producto agregado correctamente")
            print(f'CANT: {quantity}')
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

        self.update_view_products()

    def update_view_products(self):
        # Actualizar la vista de productos en el Treeview
        for row in self.treeview_products.get_children():
            self.treeview_products.delete(row)
            
        for id_producto, product in self.controller.get_products().items():
            self.treeview_products.insert("", "end", iid=str(id_producto), values=(product.name, product.price, product.stock)) # - int(self.entry_quantity.get())))
            
        total = self.controller.calculate_total()
        self.etiqueta_total.config(text=f"Total: ${total}")

    def reset_total(self):
        self.etiqueta_total.config(text="Total: $0.00")

    def show_history(self):
        # Obtener el historial de ventas desde el controlador
        history_sales = self.controller.get_sales_history()
        history_window = tk.Toplevel(self.window)
        history_window.title("Historial de Ventas")

        # Crear Treeview para el historial de ventas
        treeview_history = ttk.Treeview(history_window, columns=("Producto", "Cantidad", "Precio Total"), show="headings", height=10)
        treeview_history.heading("Producto", text="Producto")
        treeview_history.heading("Cantidad", text="Cantidad")
        treeview_history.heading("Precio Total", text="Precio Total")
        treeview_history.column("Producto", width=200)
        treeview_history.column("Cantidad", width=100)
        treeview_history.column("Precio Total", width=150)

        # Insertar las ventas al Treeview 
        for sale in history_sales:
            treeview_history.insert("", "end", values=(sale["Nombre"], sale["Cantidad"], f"${sale['Precio_total']:.2f}"))
        treeview_history.pack(padx=20, pady=20)

        # Mostrar las ganancias totales
        total_earnings = sum(sale["Precio_total"] for sale in history_sales)
        label_earnings = tk.Label(history_window, text=f"Ganancias Totales: ${total_earnings:.2f}", font=("Arial", 14, "bold"))
        label_earnings.pack(pady=10)

        # Agregar botón para cerrar la ventana del historial de ventas
        button_close = tk.Button(history_window, text="Cerrar", command=history_window.destroy)
        button_close.pack(pady=10)

        history_window.mainloop()