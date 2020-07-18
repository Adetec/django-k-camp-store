from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string

def send_order_email(order, total_price):
    
    print(order.user.username)
    subject = f'Thank you {order.user.username} for choosing our products'
    message = render_to_string(
        'orders/order-email-details.html',
        {
            'order': order,
            'products': order.items.all(),
            'total_price': total_price
        }
    )

    order.user.email_user(subject, message)