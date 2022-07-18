from django.shortcuts import render

from django.http import HttpResponse

from secondapp.models import Course
from .model_pandas import lprod 
# 페이지 처리 라이브러리
from django.core.paginator import Paginator


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
        "secondapp/lprod/lprod_list.html",
        context        
    )


# lprod
def view_Lprod(request) : 
    df_dict = lprod.getLprod("P101")
    
    # context = {"df" : df}
    # return HttpResponse(df_dict)
    
    return render(
        request,
        "secondapp/lprod/lprod.html",
        df_dict
    )
    
def view_Lprod_List_Page(request) :
    
    # 페이지 처리 시작 >>>>>
        
    try :
        now_page = request.GET.get("page")
        now_page = int(now_page)
        
    except :
        now_page = 1
    # 페이지 처리 끝 <<<<<<
        
    # 모델조회    
    df_list = lprod.getLprodList()
    
    # 페이지 처리 시작 >>>>>
    # - 첫번째 값 : 모델 조회한 데이터
    # - 두번째 값 : 한페이지에 보여줄 행의 갯수
    p = Paginator(df_list, 3)
    
    # 사용할 데이터 추출
    info = p.get_page(now_page)
    
    # 시작 페이지 번호
    start_page = (now_page - 1) // 10 * 10 + 1
    # 마지막 페이지 번호
    end_page = start_page + 9
    
    # p.num_pages : 전체 페이지 수
    # end_page    : 계산에 의한 페이지 수(10 단위 계산) 
    # 전체 페이지 수보다 크다면, 
    # 전체 페이지 수로 변경
    if end_page > p.num_pages :
        end_page = p.num_pages
    
    # 이전 페이지 가기
    is_prev = False
    # 다음 페이지 가기
    is_next = False
    
    # 이전/다음 체크하기
    if start_page > 1 :
        is_prev = True
    
    if end_page < p.num_pages :
        is_next = True
    
    # 페이지 처리 끝 <<<<<
    
    # page_control/cart_list_page.html
    # context = {"df_list" : df_list}
    context = {"info" : info,
                "page_range" : range(start_page, end_page + 1),
                "is_prev" : is_prev,
                "is_next" : is_next,
                "start_page" : start_page,
                "end_page" : end_page}
    
    return render(
        request,
        "secondapp/page_control/lprod_list_page.html",
        context
    )