from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import payment_form
from order_work.models import order
from django.conf import settings
import stripe


stripe_api_key = settings.STRIPE_SECRET


@login_required()
def get_payment(request):
    orders = order.objects.all()
    price = 10
    if request.method == "POST":
        form_payment = payment_form(request.POST)

        if form_payment.is_valid():
            purchase = form_payment.save(commit=False)
            purchase.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(price * 100),
                    currency="GBP",
                    description=request.user.email,
                    card=form_payment.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.error(request, "You have successfully paid!")
                print("success")

            else:
                messages.error(request, "Unable to take payment!")

        else:
            print(form_payment.errors)
            messages.error(
                request, "We were unable to take payment with that card!")

    else:
        form_payment = payment_form()

    return render(
        request, "../templates/payment.html", {'form_payment': form_payment, 'publishable': settings.STRIPE_PUBLISHABLE, 'orders': orders})
