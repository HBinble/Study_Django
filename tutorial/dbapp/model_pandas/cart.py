import pandas
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

### 주문내역 전체조회
def getCartList() :
    conn = getConnection()
    cursor = getCursor(conn)
    
    sql = """ SELECT * FROM cart """
    cursor.execute(sql)
    
    row = cursor.fetchall()
    
    dbClose(cursor, conn)
    
    return row
    
### 주문내역 상세조회 - 한건조회

# 한건 행에 대한 딕셔너리 만드는 함수 
def getDictType_FetchOne(col_name, row_one) :
    dict_row = {}
    
    for i in range(0, len(row_one), 1) :
        dict_row[col_name[i].lower()] = row_one[i] 
    return dict_row

def getCart(no, prod) : 
    conn = getConnection()
    cursor = getCursor(conn)
    
    sql = """ SELECT * FROM cart 
                WHERE cart_no = :cart_no
                AND cart_prod = :cart_prod """
    cursor.execute(sql,
                    cart_no=no,
                    cart_prod=prod)
    
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

# 주문내역 입력하기
def setCartInsert(id, prod, qty) :
    conn = getConnection()
    cursor = getCursor(conn)
    
    # 주문번호 생성을 위한 sql문 작성
    sql = """ SELECT DECODE(SUBSTR(MAX(cart_no),1,8),
                TO_CHAR(SYSDATE, 'YYYYMMDD'),
                MAX(cart_no)+1,
                TO_CHAR(SYSDATE, 'YYYYMMDD') || '00001') AS max_no
                FROM cart  """
    cursor.execute(sql)
    
    # 한건 조회
    max_no = cursor.fetchone()
    no = max_no[0]
    
    # 주문내역 입력을 위한 sql문 작성
    sql = """ INSERT INTO cart(cart_member, cart_no, cart_prod, cart_qty)
                    VALUES(:cart_member, :cart_no, :cart_prod, :cart_qty) """
    cursor.execute(sql,
                    cart_member = id,
                    cart_no = no,
                    cart_prod = prod,
                    cart_qty = qty)
    
    conn.commit()
    
    dbClose(cursor,conn)
    
    return "입력 성공..."