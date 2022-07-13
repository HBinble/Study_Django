from django.shortcuts import render

from django.http import HttpResponse

from secondapp.models import Course
from .model_pandas import lprod 

def main(request) :
    return HttpResponse("<p>Secondapp Main 함수 호출</p>")

# 데이터 입력
def insert(request) :
    # 1
    Course.objects.create(name='데이터 분석', cnt=30)
    # 2
    c = Course(name='데이터 수집', cnt=20)
    c.save()
    # 3
    Course(name='웹개발', cnt=25).save()
    
    Course.objects.create(name='인공지능', cnt=20)
    
    return HttpResponse("입력완료")
    
    
# 전체 조회
def show(request) : 
    data = Course.objects.all()
    
    msg = ""
    for dt in data :
        msg += dt.name + " " + str(dt.cnt) + "<br>"
    
    return HttpResponse(msg)

def oneshow(request) :
    onedata = Course.objects.get(pk=1)
    return HttpResponse(onedata.name + " " + str(onedata.cnt))

def show2(request) :
    data = Course.objects.all()
    return render(
        request,
        "secondapp/show2.html",
        {"data" : data}
    )
    
def oneshow2(request) :
    onedata = Course.objects.get(pk=1)
    return render(
        request,
        "secondapp/oneshow2.html",
        {"onedata" : onedata}
    )
    
    

### lpord 함수

#lprod_list
def view_Lprod_List(request) : 
    df_list = lprod.getLprodList()
    
    context = {"df_list" : df_list}
    
    return render(
        request,
        "html/lprod_list.html",
        context        
    )


# lprod
def view_Lprod(request) : 
    df_dict = lprod.getLprod("P101")
    
    # context = {"df" : df}
    # return HttpResponse(df_dict)
    
    return render(
        request,
        "html/lprod.html",
        df_dict
    )