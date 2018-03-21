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
    result= None

    return result
    # ======================================

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
    result = None

    return result
    # ======================================


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
    result = None

    return result
    # ======================================


def main():

    print("본 프로그램은 10진수를 n진수로 변환해주는 프로그램입니다.")
    print("======================================================")
    # ===Modify codes below=================


    # ======================================
    print("======================================================")
    print("프로그램이 종료 되었습니다.")

if __name__ == '__main__':
    main()
