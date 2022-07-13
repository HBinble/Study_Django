import pandas as pd
import cx_Oracle 

# DB 연결
def getConnection() : 
    dsn = cx_Oracle.makedsn("localhost", 1521, "orcl")
    
    conn = cx_Oracle.connect("busan_06", "dbdb", dsn)
    
    return conn

def getCursor(conn) :
    cursor = conn.cursor()
    return cursor

def dbClose(cursor, conn) : 
    cursor.close()
    conn.close()
    

##### <실제 사용하는 함수> #####

### getLprodList()
# 여러건 행에 대한 리스트 + 딕셔너리 만드는 함수
def getDictType_FetchAll(col_name, row) :
    list_row = []
    for tup in row :
        dict_row = {}
        
        for i in range(0, len(tup), 1) :
            dict_row[col_name[i].lower()] = tup[i]
            
        list_row.append(dict_row)
    return list_row

### 딕셔너리 주문내역 전체조회
def getLprodList() :
    conn = getConnection()
    cursor = getCursor(conn)
    
    sql = """ SELECT * FROM lprod """
    cursor.execute(sql)
    
    row = cursor.fetchall()
    
    # 컬럼명 조회하기
    colname = cursor.description
    col = []
    for i in colname :
        col.append(i[0])
    
    # 딕셔너리로 데이터 구성하기..
    row_list = getDictType_FetchAll(col, row)
    
    dbClose(cursor, conn)
    
    return row_list


### getLprod()

# 한건 행에 대한 딕셔너리 만드는 함수 
def getDictType_FetchOne(col_name, row_one) :
    dict_row = {}
    
    for i in range(0, len(row_one), 1) :
        dict_row[col_name[i].lower()] = row_one[i] 
    return dict_row

### 주문내역 상세조회 - 한건조회
def getLprod(gu) : 
    conn = getConnection()
    cursor = getCursor(conn)
    
    sql = """ SELECT * FROM lprod 
                WHERE lprod_gu = :lprod_gu """
    cursor.execute(sql,
                    lprod_gu=gu)
    
    # 한건 조회
    row = cursor.fetchone()
    
    # 컬럼명 조회하기
    colname = cursor.description
    col = []
    for i in colname :
        col.append(i[0])
    
    # 딕셔너리로 데이터 구성하기..
    dict_row = getDictType_FetchOne(col, row)
    
    dbClose(cursor,conn)
    
    return dict_row