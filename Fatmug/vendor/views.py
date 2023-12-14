import math
from django.shortcuts import render
from .models import vendorModel,PurchaseOrder,PerformanceRecord
from .forms import VendorAddForm
from django.db.models import Q

# Create your views here.
def Home(request):
    page="home"
    vendor = vendorModel.objects.all()
    context={"page":page,"vendor":vendor}
    return render(request,"vendor/home.html", context)

def trackVendor(request,pk):
    page="trackvendor"
    vendor = vendorModel.objects.get(id=pk)
    context={"page":page,"vendor":vendor}
    return render(request,"vendor/home.html", context)

def allPo(request):
    page="allPO"
    PO = PurchaseOrder.objects.all()
    search_query =''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    searchedPO = PurchaseOrder.objects.distinct().filter(Q(po_number__icontains = search_query) | Q(vendor__name__icontains = search_query))    
    context={"page":page,"PO":PO,"searchedPO":searchedPO,"search_query":search_query}
    return render(request,"vendor/home.html", context)

def allVendor(request,pk):
    vendor = vendorModel.objects.get(id=pk)
    completed_PO = PurchaseOrder.objects.filter(status = "completed",vendor=vendor)
    pending_PO = PurchaseOrder.objects.filter(status = "pending",vendor=vendor)
    cancelled_PO = PurchaseOrder.objects.filter(status = "canceled",vendor=vendor)
    all_PO = PurchaseOrder.objects.filter(vendor=vendor) 
    fulfillement_rate = (completed_PO.count()/all_PO.count())*100 if all_PO.count()>0 else 0
    context={"vendor":vendor,"cpo":completed_PO,"ppo":pending_PO,"capo":cancelled_PO,"allpo":all_PO,"fulfillement_rate":fulfillement_rate}
    return render(request,"vendor/allvendor.html", context)

def addVendor(request):
    page="addvendor"
    vendor = vendorModel.objects.all()
    form = VendorAddForm()
    context={"page":page,"form":form,"vendor":vendor}
    return render(request,"vendor/home.html", context)



def vendorPerformace(request,pk):
    vendor = vendorModel.objects.get(id=pk)
    completed_PO = PurchaseOrder.objects.filter(status = "completed",vendor=vendor)
    pending_PO = PurchaseOrder.objects.filter(status = "pending",vendor=vendor)
    cancelled_PO = PurchaseOrder.objects.filter(status = "canceled",vendor=vendor)
    all_PO = PurchaseOrder.objects.filter(vendor=vendor) 
    fulfillement_rate = (completed_PO.count()/all_PO.count())*100 if all_PO.count()>0 else 0
    on_time_delivery = PurchaseOrder.objects.filter(delivered_before_delivery_date=1,vendor=vendor)
    on_time_delivery_rate =(on_time_delivery.count()/all_PO.count())*100 if all_PO.count()>0 else 0
    late_delivery = all_PO.count()-on_time_delivery.count()
    acknowledgment_dates = PurchaseOrder.objects.filter(vendor=vendor)
    issue_dates = PurchaseOrder.objects.filter(vendor=vendor)
    days_list = []
    for art in acknowledgment_dates:
        acknowledgment_dates = art.acknowledgment_date
        issue_dates = art.issue_date
        days = abs(issue_dates-acknowledgment_dates).days
        days_list.append(days)
  
    # quality average rating
    q_avg_list = []
    average_response_time = math.ceil(sum(days_list)/len(days_list)if len(days_list) > 0 else 0)
    quality_avg = PurchaseOrder.objects.filter(vendor = vendor)
    
    for quality_avg in quality_avg:
        q_avg_list.append(quality_avg.quality_rating)
    
    quality_avg_rating = sum(q_avg_list)/(len(q_avg_list)) if len(q_avg_list) >0 else 0 
        
        
    page="vendorperformance"
    context={"page":page,"vendor":vendor,"cpo":completed_PO,"ppo":pending_PO,"capo":cancelled_PO,"allpo":all_PO,"fulfillement_rate":fulfillement_rate,"otd":on_time_delivery,"otdr":on_time_delivery_rate,"late_delivery":late_delivery,"average_response_time":average_response_time,"quality_avg_rating":quality_avg_rating}
    return render(request,"vendor/home.html", context)
    