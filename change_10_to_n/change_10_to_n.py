def is_positive_number(integer_str_value):
    # '''
    # Input :
    #   -  사용자가 입력한 모든 형태의 문자열
    #
    # Output :
    #   - True: 입력값이 정수일 경우
    #   - False: 그 외의 경우(실수, 특수문자 등)
    #
    # Examples :
    #   >>>import change_decimal_to_n as cdn
    #   >>>cdn.is_positive_number('10')
    #   True
    #   >>>cdn.is_positive_number('a')
    #   False
    #   >>>cdn.is_positive_number('#')
    #   False
    # '''
    # ===Modify codes below=================
    try:
        pass

    except ValueError:
        return False

def convert_decimal_to_n(decimal_number, n):
    # '''
    # Input :
    #   - decimal_number : 자연수
    #   - n : 2이상의 자연수
    #
    # Output :
    #   - 10(2) -> 1010
    #   - 100(3) -> 10201
    #
    # Examples :
    #   >>>import change_decimal_to_n as cdn
    #   >>>cdn.convert_decimal_to_n(10, 2)
    #   1010
    #   >>>cdn.convert_decimal_to_n(100, 3)
    #   10201
    #
    # '''
    # ===Modify codes below=================
<<<<<<< HEAD
    convert_number = []

    while decimal_number !=0:
        convert_number.append(divmod(decimal_number,n)[1])
        decimal_number = divmod(decimal_number,n)[0]
    convert_number.reverse()
    result=""
    for num in convert_number:
        result += str(num)
    if result =="":
        result = "0"
    return result
=======
    result= None

    return result
    # ======================================
>>>>>>> 59499bb17a47df1a42f63028e991f16323902b4c

def is_yes(one_more_input):
    # '''
    # Input:
    #   - one_more_input : 문자열값으로 사용자가 입력하는 문자
    #
    # Output:
    #   - 입력한 값이 대소문자 구분없이 "Y" 또는 "YES"일 경우 True,
    #     그렇지 않을 경우 False를 반환함
    #
    # Examples:
    #   >>>import change_decimal_to_n as cdn
    #   >>> cdn.is_yes("Y")
    #   True
    #   >>> cdn.is_yes("y")
    #   True
    #   >>> cdn.is_yes("Yes")
    #   True
    #   >>> cdn.is_yes("YES")
    #   True
    #   >>> cdn.is_yes("abc")
    #   False
    #   >>> cdn.is_yes("213")
    #   False
    #   >>> cdn.is_yes("4562")
    #   False
    # '''
    # ===Modify codes below=================
<<<<<<< HEAD
    if (one_more_input.upper() == "Y" or one_more_input.upper() == "YES"):
        return True
    else:
        return False
=======
    result = None

    return result
    # ======================================

>>>>>>> 59499bb17a47df1a42f63028e991f16323902b4c

def is_no(one_more_input):
    # '''
    # Input:
    #   - one_more_input : 문자열값으로 사용자가 입력하는 문자
    #
    # Output:
    #   - 입력한 값이 대소문자 구분없이 "N" 또는 "NO"일 경우 True,
    #     그렇지 않을 경우 False를 반환함
    #
    # Examples:
    #   >>>import change_decimal_to_n as cdn
    #   >>> cdn.is_no("Y")
    #   False
    #   >>> cdn.is_no("b")
    #   False
    #   >>> cdn.is_no("n")
    #   True
    #   >>> cdn.is_no("NO")
    #   True
    #   >>> cdn.is_no("nO")
    #   True
    #   >>> cdn.is_no("1234")
    #   False
    #   >>> cdn.is_no("yes")
    #   False
    # '''
    # ===Modify codes below=================
<<<<<<< HEAD
    if (one_more_input.upper() == "N" or one_more_input.upper() == "NO"):
        return True
    else:
        return False
=======
    result = None

    return result
    # ======================================
>>>>>>> 59499bb17a47df1a42f63028e991f16323902b4c


def main():

    print("본 프로그램은 10진수를 n진수로 변환해주는 프로그램입니다.")
    print("======================================================")
    # ===Modify codes below=================
<<<<<<< HEAD
    while (True):
        while (True):
            raw_decimal = input("변환하고 싶은 숫자를 입력해 주세요 : ")
            raw_number = input("몇 진수로 변환할 것 입니까? : ")
            if is_positive_number(raw_decimal) == True and is_positive_number(raw_number) == True:
                decimal = int(raw_decimal)
                number = int(raw_number)
                if number <= 1:
                    print("다시 입력해주세요.")
                    continue
                else:
                    print(convert_decimal_to_n(decimal, number))
                    break
            else:
                print("다시 입력해주세요.")
                continue
        while(True):
            b = input("다시 하겠습니까?(Y/N) ")
            if (is_yes(b) == False and is_no(b) == False):
                print("다시 입력해주세요.")
                continue
            else:
                break
        if is_yes(b) == True:
            continue
        else:
            break
=======


>>>>>>> 59499bb17a47df1a42f63028e991f16323902b4c
    # ======================================
    print("======================================================")
    print("프로그램이 종료 되었습니다.")

if __name__ == '__main__':
    main()
