# from django.http import JsonResponse
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializers import VendorSerializer,POSerializer
from vendor.models import vendorModel, PerformanceRecord, PurchaseOrder


@api_view(["GET"])
def getRoutes(request):
    routes = [
        {"POST":"/api/create-vendor"},#
        {"GET":"/api/vendors"},#
        {"GET":"/api/vendor/id"},#
        {"PUT":"api/edit-vendor/6/"}, #
        {"DELETE":"/api/delete-vendor/id"}, #
        {"POST":"/api/create-po"}, #
        {"GET":"/api/allpo"}, #
        {"GET":"/api/singlepo/id"}, #
        {"PUT":"/api/edit-po/id"}, #
        {"DELETE":"/api/delete-po/id"},
        {"GET":"/api/performance-metrics/id"},
    ]
    return Response(routes)

@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def getVendors(request):
    print("USER",request.user)
    vendors = vendorModel.objects.all()
    serializer = VendorSerializer(vendors, many=True) #serializer data into JSON data
    return Response(serializer.data)




# single vendors
@api_view(["GET"])
def getVendor(request,pk):
    vendors = vendorModel.objects.get(id=pk)
    serializer = VendorSerializer(vendors, many=False) #serializer data into JSON data
    return Response(serializer.data)


@api_view(["POST"])
def createVendor(request):
    if request.method == "POST":
        data =request.data
        vendor=  vendorModel.objects.create(
            name= data['name'],
            contact_details = data['contact_details'],
            address = data['address'],
            on_time_delivery_rate=data['on_time_delivery_rate'],
            quality_rating_avg=data['quality_rating_avg'],
            average_response_time=data["average_response_time"]
        )
        vendor.save()
    serializer = VendorSerializer(vendor, many=False) #serializer data into JSON data
    return Response(serializer.data)


@api_view(["PUT"])
def editVendor(request, pk):
    try:
        vendor = vendorModel.objects.get(id=pk)
    except vendorModel.DoesNotExist:
        return Response({"error": "Vendor not found"})

    data = request.data
    serializer = VendorSerializer(vendor, data=data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(["DELETE"])
def deleteVendor(request, pk):
    try:
        vendor = vendorModel.objects.get(id=pk)
    except vendorModel.DoesNotExist:
        return Response({"error": "Vendor not found"})

    vendor.delete()
    return Response({"message": "Vendor deleted successfully"})

# ==================== Purchase Orders =======================

@api_view(["GET"])
# @permission_classes([IsAuthenticated])
def getPO(request):
    po = PurchaseOrder.objects.all()
    serializer = POSerializer(po, many=True) #serializer data into JSON data
    return Response(serializer.data)

@api_view(["GET"])
def getSinglePO(request,pk):
    po = PurchaseOrder.objects.get(id=pk)
    serializer = POSerializer(po, many=False) #serializer data into JSON data
    return Response(serializer.data)

@api_view(["PUT"])
def editPO(request, pk):
    try:
        po = PurchaseOrder.objects.get(id=pk)
    except PurchaseOrder.DoesNotExist:
        return Response({"error": "Vendor not found"})

    data = request.data
    serializer = POSerializer(po, data=data)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(["POST"])
def createPO(request):
    if request.method == "POST":
        data = request.data
        # Assuming 'vendor_id' is provided in the request data to associate the PurchaseOrder with a vendor
        vendor_id = data.get('vendor')
        
        try:
            # Assuming your vendor model is named 'Vendor' and has a ForeignKey relationship with PurchaseOrder
            vendor = vendorModel.objects.get(id=vendor_id)
        except vendorModel.DoesNotExist:
            return Response({"error": "Vendor not found"})

        po = PurchaseOrder.objects.create(
            vendor=vendor,
            po_number=data["po_number"],
            order_date=data['order_date'],
            delivery_date=data['delivery_date'],
            estimated_delivery_date=data['estimated_delivery_date'],
            delivered_before_delivery_date=data['delivered_before_delivery_date'],
            items=data['items'],
            quantity=data["quantity"],
            status=data["status"],
            quality_rating=data["quality_rating"],
            issue_date=data["issue_date"],
            acknowledgment_date=data["acknowledgment_date"]
        )

        serializer = POSerializer(po, many=False)
        return Response(serializer.data)
    
    return Response({"error": "Invalid request method"})

@api_view(["DELETE"])
def deletePO(request, pk):
    try:
        po = PurchaseOrder.objects.get(id=pk)
    except PurchaseOrder.DoesNotExist:
        return Response({"error": "po not found"})

    po.delete()
    return Response({"message": "po deleted successfully"})

# performace metrics 
@api_view(["GET"])
def getPerformanceMetrics(request,pk):
    vendors = vendorModel.objects.get(id=pk)
    serializer = VendorSerializer(vendors, many=False) #serializer data into JSON data
    return Response(serializer.data)
