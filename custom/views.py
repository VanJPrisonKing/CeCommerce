from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse
# from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Order

def index(request):
    latest_order_list = Order.objects.order_by("-pub_date")[:5]
    # output = ", ".join([q.order_text for q in latest_order_list])
    # return HttpResponse(output)
    # template = loader.get_template("custom/index.html")
    context = {
        "latest_order_list": latest_order_list,
    }
    # return HttpResponse(template.render(context, request))
    return render(request, "custom/index.html", context)

def detail(request, order_id):
    # return HttpResponse("You're looking at order %s." % order_id)
    # try:
    #     order = Order.objects.get(pk=order_id)
    # except Order.DoesNotExist:
    #     raise Http404("Order does not exist")
    order = get_object_or_404(Order, pk=order_id)
    return render(request, "custom/detail.html", {"order": order})