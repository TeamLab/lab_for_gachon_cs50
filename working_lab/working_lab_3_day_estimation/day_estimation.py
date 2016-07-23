# '''
# HELP function
# 수정하지 말것 
is_yun_of_days = [31,29,31,30,31,30,31,31,30,31,30,31]
isnt_yun_of_days = [31,30,31,30,31,30,31,31,30,31,30,31]
# '''

def input_year_month_value():
    # '''
    # Input : 
    #   -변수로써 받지 않고 input함수 사용하여 받을 것
    #   -input값은 -을 기준으로 양옆으로 숫자형태의 문자열 값을 넣을 것
    # Output : 
    #   - "-"을 기준으로 크기가 2인 리스트 값
    # Example :
    #   >>> import day_estimation as de
    #   >>> de.input_year_month_value()
    #   년도와 월을 입력하시요. ex) 2015-11 :
    #   년도와 월을 입력하시요. ex) 2015-11 : 2015-11
    #   ['2015','11']
    #   >>> de.input_year_month_value()
    #   년도와 월을 입력하시요. ex) 2015-11 :
    #   년도와 월을 입력하시요. ex) 2015-11 : 2012-3
    #   ['2015','3']
    # '''
    value = input("년도와 월을 입력하시요. ex) 2015-11 : ")
    return value.split("-")

def check_year(year):
    # '''
    # Input : 
    #   -input_year_month_value() 결과값의 첫번째 값
    #   -문자형 숫자
    # Output : 
    #   - 윤년이라면 is_yun_of_days 윤년이 아니라면 isnt_yun_of_days 이 나올 것 
    #   - 정수변환이 안된다면 False가 나올 것
    # Example :
    #   >>> import day_estimation as de
    #   >>> de.check_year(2014)
    #   [31,30,31,30,31,30,31,31,30,31,30,31]
    #   >>> de.check_year(2015)
    #   [31,30,31,30,31,30,31,31,30,31,30,31]
    #   >>> de.check_year(2016)
    #   [31,29,31,30,31,30,31,31,30,31,30,31]
    #   >>> de.check_year(gachon)
    #   False
    # '''
    try:
        year = int(year)
        if year % 4 == 0 and year % 100 !=0 or year % 400 ==0:
            return is_yun_of_days
        else:
            return isnt_yun_of_days
    except:
        return False

def check_month(month):
    # '''
    # Input : 
    #   -input_year_month_value() 결과값의 두번째 값
    #   -문자형 숫자
    # Output : 
    #   - 숫자크기가 1이상 12이하이면 input-1가 결과값으로 나올 것
    #   - 숫자크기가 위에 상황에 맞지 않는다면 False가 나올 것
    #   - 정수변환이 안된다면 False가 나올 것
    # Example :
    #   >>> import day_estimation as de
    #   >>> de.check_month(13)
    #   False
    #   >>> de.check_month(12)
    #   11
    #   >>> de.check_month(1)
    #   0
    #   >>> de.check_month(gachon)
    #   False
    # '''
    try:
        month = int(month)
        if month <= 12 and month >=1:
            return month-1
        else:
            return False
    except:
        return False
        

def main():
    year,month = input_year_month_value()
    check_year_value = check_year(year)
    check_month_value = check_month(month)
    if check_year_value == False or check_month_value == False:
        print(year+"-"+month+" 는 올바른 값이 아닙니다.")
    else:
        print(year+"-"+month+":"+str(check_year_value[check_month_value]))
    
        


