from django.http import HttpResponse
from django.shortcuts import render

from .model_pandas import member as mem

# Create your views here.

def test(request) : 
    # templates 사용시 render 함수 사용
    return render(
        request,
        "oracleapp/test.html",
        {}
    )
    
# 회원 전체 조회하기
def view_Member_List(request) :
    
    df = mem.getMemberList()
    
    # return HttpResponse(df)
    
    context = {"df" : df}
        
    return render(
        request,
        "oracleapp/member_list.html",
        context
    )
    
# 회원 상세조회하기
def view_Member(request) :
    df_dict = mem.getMember("a001")
    
    #context = {"df" : df}
    
    #return HttpResponse(df_dict)
    return render(
        request,
        "oracleapp/member.html",
        df_dict
    )