def input_number_check(user_input):
    # '''
    # Input :
    #   -문자열형태의 값
    #   -4,2와 같이 숫자,숫자 형태의 값
    # Output :
    #   -각 조건의 맞게 True, False, 리스트형태로 반환할 것
    #    각 조건은 홈페이지 참조
    # Examples :
    #   >>> import c_p as cp
    #   >>> cp.input_number_check(4,2)
    #   ['4', '2']
    #   >>> cp.input_number_check(0)
    #   True
    #   >>> cp.input_number_check(-1,2)
    #   False
    #   >>> cp.input_number_check(gachon)
    #   False
    #   >>> cp.input_number_check(123,gachon)
    #   False
    # '''
    if user_input == '0':
        return True
    try:
        front,back = user_input.split(",")
        front = int(front)
        back = int(back)
        if front<0 or back<0:
            return False
        elif front >= back:
            return [front,back]
        else:
            return False

    except:
        return False

def numerator_value_front_value_factorial(front):
    # '''
    # Input :
    #   -input_number()의 첫번째 값(숫자형태의 문자열 값) 
    # Output :
    #   -input값의 팩토리얼 값
    # Examples : 
    #   >>> import c_p as cp
    #   >>> cp.numerator_value_front_value_factorial(3)
    #   6
    #   >>> cp.numerator_value_front_value_factorial(5)
    #   120
    # '''
    top = 1
    for num in range(1,int(front)+1):
        top = top * num
    return top

def denominator_value_front_minus_back_value_factorial(front,back):
    # '''
    # Input :
    #   -input_number()의 결과값(첫번째 값과 두번쨰 값)
    #   -숫자형태의 문자열 값   
    # Output :
    #   -첫번째값 - 두번째값의 팩토리얼 값
    # Examples : 
    #   >>> import c_p as cp
    #   >>> cp.denominator_value_front_minus_back_value_factorial(4,2)
    #   2
    #   >>> cp.denominator_value_front_minus_back_value_factorial(7,3)
    #   24
    # '''
    value = int(front) - int(back)
    top = 1
    for num in range(1,int(value)+1):
        top = top * num
    return top

def denominator_value_back_value_factorial(back):
    # '''
    # Input :
    #   -input_number()의 첫번째 값(숫자형태의 문자열 값) 
    # Output :
    #   -input값의 팩토리얼 값
    # Examples : 
    #   >>> import c_p as cp
    #   >>> cp.denominator_value_back_value_factorial(4)
    #   24
    #   >>> cp.denominator_value_back_value_factorial(5)
    #   120
    # '''
    top = 1
    for num in range(1,int(back)+1):
        top = top * num
    return top

def main():
    check_user_input = 999

    while(check_user_input != True):
        user_input = input("숫자들을 입력하세요. ex) 4C2 >> 4,2 : 4,2")
        check_user_input = input_number_check(user_input)
        if check_user_input == False:
            print("Input again, Please")
        elif check_user_input==True:
            print("Thank you for using this program")
            break
        else:
            numerator_value = numerator_value_front_value_factorial(check_user_input[0])
            denominator_value_front_minus_back = denominator_value_front_minus_back_value_factorial(check_user_input[0],check_user_input[1])
            denominator_value_back_value = denominator_value_back_value_factorial(check_user_input[1])
            print(numerator_value/denominator_value_front_minus_back/denominator_value_back_value)

if __name__ == "__main__":
    main()
    
