from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import razorpay
from.models import cafe
from django.views.decorators.csrf import csrf_exempt
def home(request):
    if request.method=="POST":
        name=request.POST.get("name")
        amount=int(request.POST.get("amount"))*100
        client=razorpay.Client(auth=("rzp_test_mQc43e2zpXpjW2","bQ8mw8ajxqSBnqJMLZKMeXU5"))
        payment=client.order.create({'amount':amount,'currency':'INR','payment_capture' :'1' })
        
        Cafe=cafe(name=name,amount=amount,payment_id=payment['id'])
        Cafe.save()
        return render(request,"index.html",{'payment' :payment})
    return render(request,"index.html")

@csrf_exempt
def success(request):
    if request.method == "POST": 
        a =  (request.POST)
        order_id = ""
        for key , val in a.items():
            if key == "razorpay_order_id":
                order_id = val
                break
    
        user = cafe.objects.filter(payment_id = order_id).first()
        user.paid = True
        user.save()
        

    return render(request, "success.html")
# Create your views here.
