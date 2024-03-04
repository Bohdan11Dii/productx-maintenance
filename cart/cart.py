from catalog.models import Order, Product


class Cart:
    def __init__(self, request) -> None:
        self.session = request.session
        # Get request
        self.request = request
        
        cart = self.session.get("session_key")
        
        
        
        
        if "session_key" not in request.session:
            cart = self.session["session_key"] = {}
            
            
        self.cart = cart
        
    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)
        
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {"price": str(product.price)}
            self.cart[product_id] = int(product_qty)
        self.session.modified = True
  
    
    def cart_total(self):
		# Get product IDS
        product_ids = self.cart.keys()
        # lookup those keys in our products database model
        products = Product.objects.filter(id__in=product_ids)
        # Get quantities
        quantities = self.cart
        # Start counting at 0
        total = 0
        

        for key, value in quantities.items():
            # Convert key string into into so we can do math
            key = int(key)
            for product in products:
                if product.id == key:
                    # if product.is_sale:
                        # total = total + (product.sale_price * value)
                    # else:
                        total = total + (product.price * value)
                        


        return total
        
    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        
        return products
    
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

		# Get cart
        ourcart = self.cart
		# Update Dictionary/cart
        ourcart[product_id] = product_qty

        self.session.modified = True

        thing = self.cart
        return thing
    
    def delete(self, product):
        product_id = str(product)
        # Delete from dictionary/cart
        if product_id in self.cart:
            del self.cart[product_id]

        self.session.modified = True
        
        
    def get_cart_items(self):
        # Отримати список ID продуктів з кошика
        product_ids = self.cart.keys()
        # Отримати об'єкти продуктів з бази даних за їхніми ID
        products = Product.objects.filter(id__in=product_ids)
        # Створити рядок, що представляє кошик у форматі "Назва продукту - Кількість"
        cart_items = []
        for product in products:
            quantity = self.cart[str(product.id)]
            cart_items.append(f"Назва продукту: {product.name} - кількість: {quantity}")
        # Повернути рядок, що представляє кошик
        return ", ".join(cart_items)

    def clear(self):
        self.session.pop("session_key", None)