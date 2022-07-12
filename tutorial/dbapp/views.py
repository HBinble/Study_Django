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

# 주문내역 상세조회
def view_Cart(request) : 
    df_dict = cart.getCart("2005040100001","P101000001")
    
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