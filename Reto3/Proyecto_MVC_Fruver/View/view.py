import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class ViewShopping:
    def __init__(self, controller):
        self.controller = controller
        self.controller.view = self
        self.window = tk.Tk()
        self.window.title("CAJA FRUVER - Frutas y Verduras")
        self.window.geometry("900x600")

        # Cargar imagen de fondo
        self.bg_image = Image.open('../Retos_Python/Reto3/Proyecto_MVC_Fruver/View/background.jpg')
        self.bg_image = self.bg_image.resize((900, 600), Image.LANCZOS)
        self.bg_image = ImageTk.PhotoImage(self.bg_image)
        
        '''
        self.canvas = tk.Canvas(self.window, width=900, height=600)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.bg_image, anchor="nw")
        '''
        
        self.configure_interface()  
        self.load_products()  
        self.window.mainloop()  
        
    def configure_interface(self):
        # Crear Treeview principal
        frame_principal = tk.Frame(self.window, padx=30, pady=30, bg="#f4f4f9")
        frame_principal.pack(fill="both", expand=True)
        
        # Título
        title = tk.Label(frame_principal, text="Bienvenido a la Tienda Fruver", font=("Arial", 20, "bold"), fg="green", bg="#f4f4f9")
        title.grid(row=0, column=0, columnspan=3, pady=20)
        
        # Frame para la lista de productos
        frame_products = tk.Frame(frame_principal, bg="#f4f4f9")
        frame_products.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        
        # Etiqueta para seleccionar un producto
        tag_list_products = tk.Label(frame_products, text="Selecciona un Producto:", font=("Arial", 14), bg="#f4f4f9")
        tag_list_products.pack(pady=10)

        # Crear Treeview para mostrar productos
        self.treeview_products = ttk.Treeview(frame_products, columns=("Name", "Price", "Stock"), show="headings")
        self.treeview_products.heading("Name", text="Nombre")
        self.treeview_products.heading("Price", text="Precio")
        self.treeview_products.heading("Stock", text="Stock")
        self.treeview_products.column("Name", width=220)
        self.treeview_products.column("Price", width=100)
        self.treeview_products.column("Stock", width=150)

        # Entradas y botones de la interfaz
        # Frame para ingreso y botón de cantidad
        frame_cant = tk.Frame(frame_principal, bg='#f4f4f9')
        frame_cant.grid(row=2, column=0, padx=10, pady=10, sticky='nsew')
        
        # Campo para cantidad
        tag_cant = tk.Label(frame_cant, text="Cantidad:", font=("Arial", 12), bg="#f4f4f9")
        tag_cant.pack(pady=10)

        self.entry_quantity = tk.Entry(frame_cant, font=("Arial", 12), width=10)
        self.entry_quantity.pack(pady=10)
        
        # Botón para agregar cantidad
        self.button_add_product = tk.Button(frame_cant, text="Agregar Producto", command=self.add_product, bg="#81c784", font=("Arial", 12))
        self.button_add_product.pack(pady=10)
        
        # Frame para mostrar carrito de compras
        frame_selected = tk.Frame(frame_principal, bg="#f4f4f9")
        frame_selected.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
        
        # Etiqueta para mostrar carrito de compras
        tag_cart = tk.Label(frame_selected, text="Carrito de compras actual:", font=("Arial", 14), bg="#f4f4f9")
        tag_cart.pack(pady=10)
        
        # Treeview para mostrar carrito de compras
        self.treeview_cart = ttk.Treeview(frame_selected, columns=("Producto", "Cantidad"), show="headings", height=10)
        self.treeview_cart.heading("Producto", text="Producto")
        self.treeview_cart.heading("Cantidad", text="Cantidad")
        self.treeview_cart.column("Producto", width=200)
        self.treeview_cart.column("Cantidad", width=100)
        self.treeview_cart.pack(pady=10)
        
        # Frame para total y botones finalizar e historial
        frame_buttons = tk.Frame(frame_principal, bg='#f4f4f9')
        frame_buttons.grid(row=2, column=1, padx=10, pady=10, sticky='nsew')
        
        # Etiqueta para valor total
        self.tag_total = tk.Label(frame_buttons, text="Total: $0.00", font=("Arial", 14, "bold"), bg="#f4f4f9")
        self.tag_total.pack(pady=10)
        
        # Boton para finalizar compra y ver historial
        self.button_finish = tk.Button(frame_buttons, text="Finalizar Compra", command=self.controller.finish_shopping, bg="#4caf50", font=("Arial", 14, "bold"))
        self.button_finish.pack(pady=10)
        
        self.button_history = tk.Button(frame_buttons, text="Ver Historial de Ventas", command=self.show_history, bg="#4caf50", font=("Arial", 14, "bold")) 
        self.button_history.pack(pady=10)
        
        '''
        # Ubicar elementos en el Canvas
        self.canvas.create_window(400, 150, window=self.treeview_products)
        self.canvas.create_window(400, 350, window=self.entry_quantity)
        self.canvas.create_window(400, 400, window=self.button_add_product)
        self.canvas.create_window(400, 450, window=self.button_finish)
        self.canvas.create_window(400, 500, window=self.etiqueta_total)
        self.canvas.create_window(400, 550, window=self.button_history)  # Posicionar el nuevo botón
        self.canvas.create_window(400, 550, window=self.button_cart)
        '''
    def load_products(self):
        # Insertar productos en el Treeview desde el controlador
        for id_product, product in self.controller.get_products().items():
            self.treeview_products.insert("", "end", iid=str(id_product), values=(product.name, product.price, product.stock))
        self.treeview_products.pack(pady=10)
    
    def add_product(self):
        try:
            selected_item = self.treeview_products.selection()
            if not selected_item:
                raise ValueError('Debe Seleccionar un producto de la lista.')
            selected_item = self.treeview_products.selection()[0]
            id_producto = int(selected_item)
            quantity = int(self.entry_quantity.get())
            self.controller.add_to_cart(id_producto, quantity)
            
            self.update_cart()
                        
            messagebox.showinfo("Éxito", "Producto agregado correctamente")
            self.entry_quantity.delete(quantity)
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error: {e}")

        self.update_view_products()
        
    def update_cart(self):
        cart_history = self.controller.get_products_cart()
        for row in self.treeview_cart.get_children():
            self.treeview_cart.delete(row)
        for product in cart_history:
            self.treeview_cart.insert("", "end", values=(product['producto'], product['cantidad']))
    
    def update_view_products(self):
        # Actualizar la vista de productos en el Treeview
        for row in self.treeview_products.get_children():
            self.treeview_products.delete(row)
            
        for id_producto, product in self.controller.get_products().items():
            self.treeview_products.insert("", "end", iid=str(id_producto), values=(product.name, product.price, product.stock)) # - int(self.entry_quantity.get())))
            
        total = self.controller.calculate_total()
        self.tag_total.config(text=f"Total: ${total}")
        

    def reset_total(self):
        self.tag_total.config(text="Total: $0.00")
    
    def reset_cart(self):
        for row in self.treeview_cart.get_children():
            self.treeview_cart.delete(row)

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