import datetime
from paypal.standard.models import ST_PP_COMPLETED
from django.dispatch.dispatcher import receiver
from paypal.standard.ipn.signals import valid_ipn_received
from web.models import Profile
from django.contrib.auth.models import User
from soild import settings
@receiver(valid_ipn_received)
def show_me_the_money(sender, **kwargs):
    ipn_obj = sender
    print("######################################")
    print(ipn_obj)
    print(ipn_obj.receiver_id)
    print("################################")
    user_id = ipn_obj.invoice.split("-")[0]
    u = User.objects.get(id=user_id)
    try:
        Profile.objects.create(user=u,premium=1,due_date=datetime.datetime.date(datetime.datetime.now()+datetime.timedelta(days=30)))
    except:
        p = Profile.objects.get(user=u)
        p.premium = 1
        p.due_date = datetime.datetime.date(datetime.datetime.now()+datetime.timedelta(days=30))
        p.save()
    print("payment Done ")
    if ipn_obj.payment_status == ST_PP_COMPLETED:

        if ipn_obj.receiver_email != settings.BEMAIL:
            # Not a valid payment
            return

        # ALSO: for the same reason, you need to check the amount
        # received, `custom` etc. are all what you expect or what
        # is allowed.

        # Undertake some action depending upon `ipn_obj`.
        if ipn_obj.custom == "premium_plan":
            price = 222
        else:
            price = settings.AMOUNT

        if ipn_obj.mc_gross == price and ipn_obj.mc_currency == 'USD':
            print("correct pro")
    else:
        print("Something went wrong")

# valid_ipn_received.connect(show_me_the_money)
