is_yun_of_days = [31,29,31,30,31,30,31,31,30,31,30,31]
isnt_yun_of_days = [31,30,31,30,31,30,31,31,30,31,30,31]

def input_value():
    value = input("년도와 월을 입력하시요. ex) 2015-11 : ")
    return value.split("-")

def check_year(year):
    try:
        year = int(year)
        if year % 4 == 0 and year % 100 !=0 or year % 400 ==0:
            return is_yun_of_days
        else:
            return isnt_yun_of_days
    except:
        return False

def check_month(month):
    try:
        month = int(month)
        if month <= 12 and month >=1:
            return month-1
        else:
            return False
    except:
        return False
        

def main():
    year,month = input_value()
    check_year_value = check_year(year)
    check_month_value = check_month(month)
    if check_year_value == False or check_month_value == False:
        print(year+"-"+month+" 는 올바른 값이 아닙니다.")
    else:
        print(year+"-"+month+":"+str(check_year_value[check_month_value]))
    
        


main()
