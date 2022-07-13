from django.http import HttpResponse
from django.shortcuts import render

from .model_pandas import cart
# Create your views here.

def test(request) : 
    return render (
        request,
        "dbapp/test.html",
        {}
    )
# 주문내역 전체조회    
def view_Cart_List(request) : 
    
    df = cart.getCartList()
    # return HttpResponse(df)
    context = {"df" : df}
    
    return render(
        request,
        "dbapp/cart/cart_list.html",
        context
    )

def view_Cart_List_dict(request) : 
    
    df_list = cart.getCartList()
    # return HttpResponse(df)
    context = {"df_list" : df_list}
    
    return render(
        request,
        "dbapp/cart/cart_list_dict.html",
        context
    )

# 주문내역 상세조회
def view_Cart(request) : 
    
    cart_no = request.GET["cart_no"]
    cart_prod = request.GET["cart_prod"]
    
    df_dict = cart.getCart(cart_no, cart_prod)
    
    # context = {"df" : df}
    # return HttpResponse(df_dict)
    
    return render(
        request,
        "dbapp/cart/cart.html",
        df_dict
    )
    
# 주문내역 입력하기
def view_set_Cart_Insert(request) : 
    id = "e001"
    prod = "P102000001"
    qty = 17
    
    msg = cart.setCartInsert(id, prod, qty)
    
    return HttpResponse(msg)

# def testDict(request) :
#     context = {"dt" :[(1,2,3),(4,5,6),(7,8,9),(10,11,12)]}
#     # context = {"no1":1, "no2":2, "no3":3, "no4":4, "no5":5}
#     # return HttpResponse(context)
#     return render(
#         request,
#         "dbapp/cart/testdict.html",
#         context
#     )
    
def testDict(request) :
    context = {"dt" :[{"no1":1, "no2":2, "no3":3},
                        {"no1":4, "no2":5, "no3":6}]}
    # return HttpResponse(context)
    return render(
        request,
        "dbapp/cart/testdict.html",
        context
    )