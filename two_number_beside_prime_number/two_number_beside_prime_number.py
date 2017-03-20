def change_type_str_to_int_of_list(list_value):
    # '''
    # Input :
    #   - string type의 list를 받아옴
    #
    # Output :
    #   - integer type의 list
    #   - interger type으로 변환 불가능한 요소가 있을 경우 Error
    #
    # Examples :
    #   >>>import count_prime_number as cpn
    #   >>>cpn.change_type_str_to_int_of_list(['1', '3', '10'])
    #   [1, 3, 10]
    #   >>>cpn.change_type_str_to_int_of_list(['a', '7', '&'])
    #   Error
    #
    # '''
    # ===Modify codes below=================

    num_list = []
    for component in list_value:
        if component.isdigit():
            num_list.append(int(component))
    return num_list

def number_check(number_list):
    # '''
    # Input :
    #   - change_type_str_to_int_of_list함수의 결과값
    #
    # Output :
    #   - 입력된 리스트의 범위 내에서 2이상의 모든 수를 리스트로 반환
    #
    # Examples :
    #   >>>import count_prime_number as cpn
    #   >>>cpn.number_check([1, 20])
    #   [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    #   >>>cpn.number_check([10, 5])
    #   [5, 6, 7, 8, 9, 10]
    #
    # '''
    # ===Modify codes below=================

    false_list = []
    checked_list = []
    for num in range(min(number_list), max(number_list) + 1):

        if num >= 2:
            checked_list.append(num)

        else:
            false_list.append(num)

    return checked_list


def is_prime_number(checked_list):
    # '''
    # Input :
    #   - number_check함수의 결과값
    #
    # Output :
    #   - 입력 값 중 소수만을 리스트로 반환
    #
    # Examples :
    #   >>>import count_prime_number as cpn
    #   >>>cpn.is_prime_number([2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    #   [2, 3, 5, 7, 11, 13, 17, 19]
    #   >>>cpn.is_prime_number([12,13,14,15,16,17,18,19,20])
    #   [13, 17, 19]
    #
    # '''
    # ===Modify codes below=================

    prime_number_list = []
    for num in checked_list:
        count = 0
        for div in range(1, num):
            if num % div == 0:
                count += 1
        if count == 1:
            prime_number_list.append(num)

    return prime_number_list





def main():
    print("소수의 개수 구하기")
    print("=========================")
    # ===Modify codes below=================
    input_number = input("숫자의 범위를 지정해주세요. ex) 숫자,숫자 : ").split(",")
    number_list = change_type_str_to_int_of_list(input_number)
    if len(number_list) == 0 or len(number_list) == 1:
        print('잘못된 값입니다')
    else:
        checked_list = number_check(number_list)
        if len(is_prime_number(checked_list)) == 0 :
            print('범위 내에 소수가 없습니다.')
        else:
            print(len(is_prime_number(checked_list)),"개", ",", is_prime_number(checked_list))
    # ======================================
    print("=========================")
    print("프로그램이 종료되었습니다.")

if __name__ == '__main__':
    main()