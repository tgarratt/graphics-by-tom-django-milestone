from django.shortcuts import render
from django.contrib import messages
from .forms import purchase_form, payment_form
from .models import purchase_line_item
from order_work.forms import order_form
from django.conf import settings
import stripe


stripe_api_key = settings.STRIPE_SECRET


def get_payment(request):
    if request.method == "POST":
        form_purchase = purchase_form(request.POST)
        form_payment = payment_form(request.POST)

        if form_purchase.is_valid() and form_payment.is_valid():
            purchase = form_payment.save(commit=False)
            request_date = timezone.now()
            purchase.save

            line_item = purchase_line_item(
                buy = buy, 
                work = work
            )
            line_item.save()

            try:
                user = stripe.Charge.create(
                    amount = int(total * 100),
                    currency = "GBP",
                    description = request.user.email,
                    card = form_payment.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.error(request, "You have successfully paid!")
                console.log("success")

            else:
                 messages.error(request, "Unable to take payment!")

        else:
            print(form_payment.errors)
            messages.error(request, "We were unable to take payment with that card!")

    else:
        form_purchase = purchase_form()
        form_payment = payment_form()   

    return render(  
        request, "../templates/payment.html", {'form_purchase': form_purchase, 'form_payment': form_payment, 'publishable': stripe_api_key})

