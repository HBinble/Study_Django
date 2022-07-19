from django.http import HttpResponse
from django.shortcuts import render

from .model import survey


def view_Test(request) : 
    return render(
        request,
        "chi2app/test.html",
        {"msg" : "ok"}
    )
    
def view_DB_Test(request) : 
    
    df = survey.getDBTest()
    context = {"msg" : df}
    
    return render(
        request,
        "chi2app/test.html",
        context
    )
# survey 테이블 생성하기
def createTable(request) :
    survey.createTableSurvey()
    
    return HttpResponse("Create OK....")

# 설문 데이터 입력 테이스
def set_Survey_Insert_test(request) :
    pgender = "여"
    page = 20
    pco_survey = "스타벅스"
    
    survey.setSurveyInsert(pgender, page, pco_survey)
    
    return HttpResponse("Insert OK")

# 설문 전체 조회하기
def view_Survey_List(request) :
    df = survey.getSurveyList()
    
    #return HttpResponse(df.to_html())
    context = {"df" : df.to_html()}
    
    return render(
        request,
        "chi2app/list.html",
        context
    )
    
# 설문 참여하기 페이지 view
def view_Survey(request) :
    return render(
        request,
        "chi2app/survey.html",
        {}
    )

# 설문 데이터 입력 
def set_Survey_Insert(request) :
    
    pgender    = request.POST.get("gender")
    page       = request.POST.get("age")
    pco_survey = request.POST.get("co_survey")
    
    rs = survey.setSurveyInsert(pgender, page, pco_survey)
    
    msg = ""
    if rs == "OK" : 
        msg = """<script>
                    alert("입력 되었습니다!")
                    location.href="/chi2/list/"
                </script>"""
                
    return HttpResponse(msg)