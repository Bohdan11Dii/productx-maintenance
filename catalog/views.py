from django.shortcuts import render
from django.db import transaction

from cart.cart import Cart
from .models import Product, Category, Order
from django.views import generic
from django.urls import reverse_lazy
from catalog.forms import OrderForm
import telebot


TELEGRAM_API_TOKEN = "7053950173:AAG-tqkU-0iMbIbbBIVuR74d0EX5bKDcKx4"
TELEGRAM_CHAT_ID = "321811367"


class CategoryListView(generic.ListView):
    model = Category
    # context_object_name = "category"

class CategoryDetailView(generic.DetailView):
    model = Category
    
    
class ProductListView(generic.ListView):
    model = Product
    queryset = Product.objects.select_related("category")
    paginate_by = 10


class ProductDetailView(generic.DetailView):
    model = Product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        context['quantity_range'] = range(1, product.quantity + 1)
        
        
        return context


class OrderCreateView(generic.CreateView):
    model = Order
    form_class = OrderForm
    success_url = reverse_lazy("catalog:product-list")
    
    def form_valid(self, form):
        # Створити об'єкт форми, але ще не зберігати його у базі даних
        self.object = form.save(commit=False)
        # Отримати кошик
        cart = Cart(self.request)
        # Отримати рядок кошика та зберегти його у поле order_cart об'єкта Order
        self.object.order_cart = cart.get_cart_items()
        # Отримати ціну кошика та зберегти його у поле total_amount об'єкта Order
        self.object.total_amount = cart.cart_total()
        # Зберегти об'єкт Order у базу даних
        self.object.save()
        # Очистити кошик
        cart.clear()
        
        self.send_order_to_telegram(self.object)
        # Опціонально: очистити інформацію про кошик у сеансі
        return super().form_valid(form)

    def send_order_to_telegram(self, order):
        bot = telebot.TeleBot(TELEGRAM_API_TOKEN)
        message = f"Нове замовлення!\n\n{order.order_cart}\nЗагальна вартість: {order.total_amount}\n\nДеталі користувача:\n{order.first_name} {order.last_name}\nТелефон: {order.phone}\nВідділення: {order.department}"
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)