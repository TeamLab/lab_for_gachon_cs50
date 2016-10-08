# '''
# HELP function
# 수정하지 말것
def int_to_str(list):
    return [str(value) for value in list]

def str_to_int(list):
    return [int(value) for value in list]
# '''

def check_used_list_method(user_list):
    # '''
    # Input :
    #   - 사용자 입력값들의 리스트
    #   - 리스트 내의 모든 value는 string type
    #
    # Output :
    #   - 리스트 내의 모든 값이 정수라면 True
    #   - 사용자의 입력값이 없거나 문자 혹은 실수라면 False
    #
    # Examples :
    #   >>>import positive_smallest_number as psn
    #   >>>psn.check_used_list_method(['4', '10', '47', '10'])
    #   True
    #   >>>psn.check_used_list_method(['10', '935', '93', '-13'])
    #   Ture
    #   >>>psn.check_used_list_method([])
    #   False
    #   >>>psn.check_used_list_method(['a', '-1', '-77', '17'])
    #   False
    #   >>>psn.check_used_list_method(['-21', '-15', '36.6', '19'])
    #   False
    # '''
    # ===Modify codes below=================
    check_str = ','.join(user_list)
    check_str = check_str.replace(" ","")
    if len(check_str) == 0 :
        return False
    try:
        int_value_list = str_to_int(user_list)
        str_value_list = int_to_str(int_value_list)
        for count in range(len(str_value_list)):
            if len(str_value_list[count]) != len(user_list[count].strip()):
                return False
        return True
    except:
        return False


def define_plus_miunus_method(user_list):
    # '''
    # Input :
    #   - 사용자가 입력한 숫자들의 리스트
    #   - 리스트 내의 모든 value는 integer type
    #
    # Output :
    #   - 리스트 내의 모든 value가 양의 정수이면 True 아니면 False
    #
    # Examples :
    #   >>>import positive_smallest_number as psn
    #   >>>psn.define_plus_miunus_method([10, 10, 97, 47])
    #   True
    #   >>>psn.define_plus_miunus_method([7, 4, 12, -1])
    #   False
    # '''
    # ===Modify codes below=================


    plus_sign_value = 0
    for list_value in user_list:
        if list_value>=0:
            plus_sign_value += 1
    if plus_sign_value == len(user_list):
        return True
    return False

def make_smallest_number_of_minus(list):
    # '''
    # Input :
    #   - 모든 value가 integer type인 list
    #   - 리스트 내의 값중 한 개 이상의 값은 음수
    #
    # Output :
    #   - list
    #   - 리스트 내의 숫자들을 가장 작은 수를 만들기위한 순서대로 정렬
    #
    # Examples :
    #   >>>import positive_smallest_number as psn
    #   >>>psn.make_smallest_number_of_minus([10, 10, -97, -47])
    #   [-97, 47, 10, 10]
    #   >>>psn.make_smallest_number_of_minus([-10, -20, -30, -40])
    #   [-40, 30, 20, 10]
    #   >>>psn.make_smallest_number_of_minus([-7, 256, 22, 227])
    #   [-7, 256, 227, 22]
    # '''
    # ===Modify codes below=================

    list_2  = []
    for value in list:
        if value<0:
            list_2.append(abs(value))
    for big_len_list in range(len(list_2)):
        for small_len_list in range(len(list_2)-1-big_len_list):
            first_value = str(list[small_len_list])+str(list[small_len_list+1])
            second_value = str(list[small_len_list+1])+str(list[small_len_list])
            if(first_value>second_value):
                change_value=list_2[small_len_list]
                list_2[small_len_list]=list_2[small_len_list+1]
                list_2[small_len_list+1]=change_value

    smallest_value = -1*list_2[0]
    real_list = []
    for change in list:
        if smallest_value == change:
            continue
        else:
            real_list.append(abs(change))
    for big_len_list in range(len(real_list)):
        for small_len_list in range(len(real_list) - 1 - big_len_list):
            first_value = str(real_list[small_len_list]) + str(real_list[small_len_list + 1])
            second_value = str(real_list[small_len_list + 1]) + str(real_list[small_len_list])
            if (first_value < second_value):
                change_value = real_list[small_len_list]
                real_list[small_len_list] = real_list[small_len_list + 1]
                real_list[small_len_list + 1] = change_value
    real_list.insert(0, smallest_value)
    return real_list


def make_smallest_number_of_plus(list):
    # '''
    # Input :
    #   - 모든 value가 integer type인 list
    #   - 리스트 내의 모든 value는 양수
    #
    # Output :
    #   - list
    #   - 리스트 내의 숫자들을 가장 작은 수를 만들기위한 순서대로 정렬
    #
    # Examples :
    #   >>>import positive_smallest_number as psn
    #   >>>psn.make_smallest_number_of_plus([512, 51, 29, 77])
    #   [29, 512, 51, 77]
    #   >>>psn.make_smallest_number_of_plus([1, 7, 25, 91])
    #   [1, 25 ,7, 91]
    #
    # '''
    # ===Modify codes below=================

    for big_len_list in range(len(list)):
        for small_len_list in range(len(list)-1-big_len_list):
            first_value = str(list[small_len_list])+str(list[small_len_list+1])
            second_value = str(list[small_len_list+1])+str(list[small_len_list])
            if(first_value>second_value):
                change_value=list[small_len_list]
                list[small_len_list]=list[small_len_list+1]
                list[small_len_list+1]=change_value
    zero_count = list.count(0)
    for count in range(zero_count):
        list.remove(0)
    for zero in range(1,zero_count+1):
        list.insert(zero,0)

    return list

def merge_list_to_int(list):
    # '''
    # Input :
    #   - make_smallest_number_of_plus과 make_smallest_number_of_minus의 결과값
    #
    # Output :
    #   - 리스트 내의 값들을 순서대로 이어서 숫자로 반환
    #
    # Examples :
    #   >>>import positive_smallest_number as psn
    #   >>>psn.merge_list_to_int([-99, 61, 23, 10])
    #   -99612310
    #   >>>psn.merge_list_to_int([17, 78, 85, 99])
    #   17788599
    #  '''
    # ===Modify codes below=================
    list = int_to_str(list)
    str_value_str = "".join(list)
    int_value = int(str_value_str)

    return int_value


def main():
    print("가장 작은 수 만들기")
    print("============================")
    # ===Modify codes below=================
    user_input = input("숫자들을 입력하세요. ex)3,2,10,-1,0 :" ).split(",")
    if check_used_list_method(user_input) == True:
        user_input = str_to_int(user_input)
        if define_plus_miunus_method(user_input) == True:
            last_list = make_smallest_number_of_plus(user_input)
            print(merge_list_to_int(last_list))

        else:
            last_list = make_smallest_number_of_minus(user_input)
            print(last_list)
            print(merge_list_to_int(last_list))
    else:
        print("Wrong input again please")
    # ======================================
    print("===========================")
    print("프로그램이 종료 되었습니다.")

if __name__ == "__main__":
    main()
