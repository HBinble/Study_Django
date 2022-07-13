import re
from django.http import HttpResponse
from django.shortcuts import render

from .model_pandas import member as mem
from .model_pandas import cart
from .model_pandas import lprod 

# Create your views here.

def test(request) : 
    # templates 사용시 render 함수 사용
    return render(
        request,
        "oracleapp/test.html",
        {}
    )

# 회원 딕셔너리 전체 조회하기
def view_Member_List_dict(request) :
    
    df_list = mem.getMemberListDict()
    
    # return HttpResponse(df)
    context = {"df_list" : df_list}
        
    return render(
        request,
        "oracleapp/member/member_list_dict.html",
        context
    )

# 회원 전체 조회하기
def view_Member_List(request) :
    
    df = mem.getMemberList()
    
    # return HttpResponse(df)
    
    context = {"df" : df}
        
    return render(
        request,
        "oracleapp/member/member_list.html",
        context
    )
    
# 회원 상세조회하기
def view_Member(request) :
    
    mem_id = request.GET["mem_id"]
    
    df_dict = mem.getMember(mem_id)
    
    #context = {"df" : df}
    
    #return HttpResponse(df_dict)
    return render(
        request,
        "oracleapp/member/member.html",
        df_dict
    )

# 주문내역 전체조회    
def view_Cart_List(request) : 
    
    df = cart.getCartList()
    # return HttpResponse(df)
    context = {"df" : df}
    
    return render(
        request,
        "oracleapp/cart/cart_list.html",
        context
    )

def view_Cart_List_dict(request) : 
    
    df_list = cart.getCartListDict()
    # return HttpResponse(df)
    context = {"df_list" : df_list}
    
    return render(
        request,
        "oracleapp/cart/cart_list_dict.html",
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
        "oracleapp/cart/cart.html",
        df_dict
    )
    
# 주문내역 입력하기
def set_Cart_Insert(request) : 
    id = "e001"
    prod = "P102000001"
    qty = 17
    
    msg = cart.setCartInsert(id, prod, qty)
    
    return HttpResponse(msg)

# 주문내역 삭제하기
def set_Cart_Delete(request) : 
    
    cart_no = request.GET["cart_no"]
    cart_prod = request.GET["cart_prod"]
    
    msg = cart.setCartDelete(cart_no, cart_prod)
    
    return render(
        request,
        "oracleapp/cart/cart_delete.html",
        {"msg" : msg}
    )

# 주문내역 삭제하기
def view_Cart_Update(request) : 
    
    pcart_no = request.GET["cart_no"]
    pcart_prod = request.GET["cart_prod"]
    
    # msg = cart.setCartDelete(cart_no, cart_prod)
    
    context = {"pcart_no" : pcart_no, 
                "pcart_prod" : pcart_prod}
    
    return render(
        request,
        "oracleapp/cart/cart_update_form.html",
        context
    )


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
        "oracleapp/cart/testdict.html",
        context
    )
    
def view_Lprod_List(request) : 
    
    df_list = lprod.getLprodList()
    # return HttpResponse(df)
    context = {"df_list" : df_list}
    
    return render(
        request,
        "oracleapp/lprod/lprod_list.html",
        context
    )
    
def view_Lprod(request) : 
    
    lprod_gu = request.GET["lprod_gu"]
    
    df_dict = lprod.getLprod(lprod_gu)
    
    # context = {"df" : df}
    # return HttpResponse(df_dict)
    
    return render(
        request,
        "oracleapp/lprod/lprod.html",
        df_dict
    )