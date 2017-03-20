def think_positive_number(integer_str_value):
    # '''
    # Input :
    #   - 각각의 요소들이 문자형 정수형태의 list
    #
    # Output :
    #   - True 가 나오는 경우
    #       1. 숫자의 개수가  2일때
    #       2. 모든 숫자가 0 이상일때
    #   - False 가 나오는 경우
    #       1, 정수형이 아닌 문자열이 들어간 리스트
    #       2. 숫자의 개수가 2가 아닐때
    # Examples :
    #   >>>import individual_number_of_count as inoc
    #   >>>inoc.think_positive_number(['10', 'a'])
    #   False
    #   >>>inoc.error_check(['a', '7', '&'])
    #   False
    #   >>>inoc.error_check(['7', '10'])
    #   True
    #  '''
    try:
        # ===Modify codes below=================
        if len(integer_str_value) != 2  :
            return False
        count = 0
        for is_positive_number in integer_str_value:
            if int(is_positive_number) >= 0:
                count += 1
        if count ==len(integer_str_value):
            return True
        return False
        # ======================================
    except ValueError:
        return False

def make_range_list(list):
    # Input :
    #   - string type의 숫자 2개로 구성된 list를 받아옴
    #
    # Output :
    #   - [10, 20]
    #   - [7, 13]
    #
    # Examples :
    #   >>>import number_of_character as noc
    #   >>>noc.make_range_list(['10', '20'])
    #   [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    #   >>>noc.make_range_list(['7', '13'])
    #   [7, 8, 9, 10, 11, 12, 13]
    #
    # '''
    # ===Modify codes below=================
    range_list = []
    for index in range(len(list)):
        list[index]=int(list[index])

    for num in range(min(list), max(list) + 1):
        range_list.append(int(num))

    return range_list
    # ======================================

def make_number_list(range_list):
    # Input :
    #   - make_range_list함수의 결과값
    #
    # Output :
    #   - 범위내 숫자들의 모든 자릿수의 값들을 중복없이 리스트로 반환
    #
    # Examples :
    #   >>>import number_of_character as noc
    #   >>>noc.make_number_list([10, 20])
    #   [0, 1, 2]
    #   >>>noc.make_number_list([12, 13, 14, 15, 16])
    #   [1, 2, 3, 4, 5 ,6]
    #   >>>noc.make_number_list([7, 8, 9])
    #   [7, 8, 9]
    #
    # '''
    # ===Modify codes below=================
    number_list = []
    for num in range_list:
        for one_value_num in str(num):
            number_list.append(int(one_value_num))
    number_list=list(set(number_list))
    number_list.sort()
    return number_list
    # ======================================

def my_count(range_list, number_list):
    # '''
    # Input :
    #   - range_list : make_range_list함수의 결과값
    #   - number_list : make_number_list함수의 결과값
    #
    # Output :
    #     - 범위내 숫자들의 자릿수 숫자의 갯수 리스트
    #
    # Examples :
    #   >>>import number_of_character as noc
    #   >>>noc.my_count([10, 20], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    #   [2, 1, 1, 0, 0, 0, 0, 0, 0, 0]
    #   >>>noc.my_count([12, 14], [1, 2, 3, 4])
    #   [2, 1, 0, 1, 0, 0, 0, 0, 0, 0]
    #
    # '''
    # ===Modify codes below=================
    count_list = [0 for count in range(10)]

    for num in range_list:
        for one_value_num in str(num):
            count_list[number_list.index(int(one_value_num))] += 1
    return count_list
    # ======================================

def main():
    print("각 숫자의 개수 구하기")
    print("==========================")
    # ===Modify codes below=================
    while(True):
        user_input = input("숫자의 범위를 지정해주세요 ex)2,7 : ").upper()

        if user_input == "FINISH":
            break

        user_input = user_input.split(",")
        if user_input.upper() == "FINISH":
            break
        if think_positive_number(user_input) == True:
            for i in range(len(make_number_list(make_range_list(user_input)))):
                print(make_number_list(make_range_list(user_input))[i],my_count(make_range_list(user_input), make_number_list(make_range_list(user_input)))[i])
        else:
            print("다시 입력해주세요.")

     # ======================================
    print("==========================")
    print("프로그램이 종료 되었습니다.")

if __name__ == '__main__':
    main()