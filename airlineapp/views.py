from django.shortcuts import render

FLIGHT_SERVICE_URL = "http://localhost:8001"
NOTIFICATION_SERVICE_URL = "http://localhost:8002"
def addflights(request):
    return render(request, 'addflights.html')

def searchflights(request):
    return render(request, 'searchflights.html')

def notify_new_customer(request):
    send_email.delay('Welcome!', 'Thank you for joining our service', ['customer@example.com'])
    return JsonResponse({'status': 'Notification sent'})

@csrf_exempt
def add_flight(request):
    response = requests.post(f"{FLIGHT_SERVICE_URL}/v1/flights/add/", data=request.POST)
    return JsonResponse(response.json())

def search_flight(request):
    response = requests.get(f"{FLIGHT_SERVICE_URL}/v1/flights/search/", params=request.GET)
    return JsonResponse(response.json())

@csrf_exempt
def buy_ticket(request):
    response = requests.post(f"{FLIGHT_SERVICE_URL}/v1/flights/buy/", data=request.POST)
    return JsonResponse(response.json())

@csrf_exempt
def add_miles(request):
    response = requests.post(f"{NOTIFICATION_SERVICE_URL}/v1/notify/", data=request.POST)
    return JsonResponse(response.json())

