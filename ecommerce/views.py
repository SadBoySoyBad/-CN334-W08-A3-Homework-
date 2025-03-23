from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.
def ecommerce_index_view(request):
 '''This function render index page of ecommerce views'''
 return HttpResponse('Welcome to 6510742247 Kittipon Tongtrakul views!')
# Mock Data สำหรับ "/user/username"
users = {
    "kittipon": {
        "email": "Kittipon.ton@dome.tu.ac.th",
        "username": "Kittipon",
        "date":"1/1/2025"
    }
}

# Mock Data สำหรับ "/product/all"
products = [
    {"id": 1, "car": "porsche 911", "price": 9999999999},
    {"id": 2, "car": "porsche tycan", "price": 88888888},
    {"id": 3, "car": "rolls-royce phantom", "price": 89829849849}
]

# Mock Data สำหรับ "/comment/byProductId/[id]"
comments = {
    1: [
        {"comment_id": 1, "content": "The Porsche 911 is a legendary, high-performance sports car known for its iconic design, rear-engine layout, and a history of continuous evolution, now in its eighth generation."},
    ],
    2: [
        {"comment_id": 2, "content": "The Porsche Taycan is an all-electric sports car that offers a blend of Porsche's iconic performance and luxury with a zero-emission powertrain, available in sedan, Cross Turismo, and Sport Turismo body styles."}
    ],
    3: [
        {"comment_id": 3, "content": "The Rolls-Royce Phantom is a full-sized, ultra-luxury saloon known for its opulent interior, smooth ride, and powerful, yet quiet, performance, epitomizing luxury and elegance with bespoke customization options."}
    ],

}

# View สำหรับ "/user/[username]"
def get_user(request, username):
    if username in users:
        return JsonResponse(users[username])
    else:
        return JsonResponse({"error": "User not found"}, status=404)

# View สำหรับ "/product/all"
def get_all_products(request):
    return JsonResponse({"products": products})

# View สำหรับ "/product/byId/[id]"
def get_product_by_id(request, id):
    product = next((item for item in products if item["id"] == id), None)
    if product:
        return JsonResponse(product)
    else:
        return JsonResponse({"error": "Product not found"}, status=404)

# View สำหรับ "/comment/byProductId/[id]"
def get_comments_by_product(request, id):
    if id in comments:
        return JsonResponse({"comments": comments[id]})
    else:
        return JsonResponse({"error": "Comments not found"}, status=404)

# View สำหรับ "/summarize"
def summarize(request):
    total_products = len(products)
    total_price = sum(product["price"] for product in products)
    return JsonResponse({
        "total_products": total_products,
        "total_price": total_price
    })