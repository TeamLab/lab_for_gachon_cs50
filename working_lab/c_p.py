def input_number():
    # '''
    # Input :
    #   -변수로써 받지 않고 input함수 사용하여 받을 것
    #   -4C2를 하고싶으면 4,2로 입력할 것   
    # Output :
    #   -리스트형태로 반환할 것 
    # Examples : 
    #   >>> import c_p as cp
    #   >>> cp.input_number()
    #   숫자들을 입력하세요. ex) 4C2 >> 4,2 :
    #   숫자들을 입력하세요. ex) 4C2 >> 4,2 : 4,2
    #   ['4', '2']
    #   >>> cp.input_number()
    #   숫자들을 입력하세요. ex) 4C2 >> 4,2 :
    #   숫자들을 입력하세요. ex) 4C2 >> 4,2 : 4;2
    #   error
    # '''
    front,back = input("숫자들을 입력하세요. ex) 4C2 >> 4,2 : ").split(",")
    return [front,back]

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
    
    number_list = input_number()
    numerator_value = numerator_value_front_value_factorial(number_list[0])
    denominator_value_front_minus_back = denominator_value_front_minus_back_value_factorial(number_list[0],number_list[1])
    denominator_value_back_value = denominator_value_back_value_factorial(number_list[1])
    print(numerator_value/denominator_value_front_minus_back/denominator_value_back_value)
    
if __name__ == "__main__":
    main()
    
