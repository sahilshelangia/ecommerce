from django.shortcuts import render

# Create your views here.
STRIPE_PUB_KEY='pk_test_bqgqNT49zCYUihT73QvGiOhR00VNE9EgMB'
def payment_method_view(request):
	if request.method=='POST':
		print(request.POST)
	return render(request,'billing/payment-method.html',{"publish_key":STRIPE_PUB_KEY})