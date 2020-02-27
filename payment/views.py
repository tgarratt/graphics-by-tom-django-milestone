from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import payment_form
from order_work.models import order
from order_work.forms import order_form
from django.conf import settings
import stripe


stripe.api_key = settings.STRIPE_SECRET


@login_required()
def get_payment(request):
    user_order = order.objects.order_by('order_date').last()
    payment_amount = user_order.order_total

    if request.method == "POST":
        form_payment = payment_form(request.POST)

        if form_payment.is_valid():
            price = payment_amount
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
                messages.success(request, "You have successfully paid!")
                user_order.paid = True
                user_order.save()
                return redirect(reverse("home"))

            else:
                messages.error(request, "Unable to take payment!")
                
        else:
            print(form_payment.errors)
            messages.error(
                request, "We were unable to take payment with that card!")

    else:
        form_payment = payment_form()

    return render(
        request, "../templates/payment.html", {'form_payment': form_payment, 'publishable': settings.STRIPE_PUBLISHABLE, 'payment_amount': payment_amount})
