def create_even_number_method(number):
    # '''
    # Input :
    #   -1이상의 정수형 숫자
    # Output :
    #   -숫자의 길이가 짝수인 숫자들중 가운대를 기준으로 뒤집었을 때 똑같은 숫자
    #   -숫자의 길이가 짝수다. ex) 21, 4856   >> len("21") = 2   len("4856") = 4
    #   -가운대를 기준으로 뒤집었을 때 똑같은 숫자다. ex) 22, 4224, 5555
    #    1. 22를 가운대를 기준으로 나눠서(2,2) 한숫자를 뒤집었을때 똑같다.
    #    2. 4224 가운대를 기준으로 나눠서(42,24) 한숫자를 뒤집었을때(42,42) 똑같다.
    #    3. 12344321 가운대를 기준으로 나눠서(1234,4321) 한숫자를 뒤집었을때(1234,1234) 똑같다.
    #   - 위의 조건을 만족하는 숫자들을 1차원 리스트 형태로 반환
    # Examples :
    #   >>>import reverse_before_after_same_number as rbasn
    #   >>>rbasn.create_even_number_method(9)
    #   []
    #   >>>rbasn.create_even_number_method(15)
    #   [11]
    #   >>>rbasn.create_even_number_method(100)
    #   [11, 22, 33, 44, 55, 66, 77, 88, 99]
    #   >>>rbasn.create_even_number_method(1001)
    #   [11, 22, 33, 44, 55, 66, 77, 88, 99, 1001]
    # '''
    even_number_list = []
    for num in range(1,number+1):
        len_of_number_remain = len(str(num))%2
        len_of_number_share = len(str(num))//2
        if len_of_number_remain == 0:
            count_method = 0
            for ct in range(0,len_of_number_share):
                if str(num)[ct]== str(num)[-1-ct]:
                    count_method += 1
                if count_method == len_of_number_share:
                    even_number_list.append(num)

    return even_number_list


def create_odd_number_method(number):
    # '''
    # Input :
    #   -1이상의 정수형 숫자
    # Output :
    #   -숫자의 길이가 홀수인 숫자들중 가운대를 기준으로 뒤집었을 때 똑같은 숫자
    #   -숫자의 길이가 짝수다. ex) 3, 211, 12345    >> len("3") = 1   len("211") = 3 len("12345") = 5
    #   -가운대 숫자를 기준으로 뒤집었을 때 똑같은 숫자다. ex) 212, 42324, 55255
    #    1. 212를 가운대 숫자(1)를 기준으로 나눠서(2,2) 한숫자를 뒤집었을때 똑같다.
    #    2. 42324 가운대 숫자(1)를 기준으로 나눠서(42,24) 한숫자를 뒤집었을때(42,42) 똑같다.
    #    3. 123454321 가운대 숫자(5)를 기준으로 나눠서(1234,4321) 한숫자를 뒤집었을때(1234,1234) 똑같다.
    #   - 위의 조건을 만족하는 숫자들을 1차원 리스트 형태로 반환
    # Examples :
    #   >>>import reverse_before_after_same_number as rbasn
    #   >>>rbasn.create_odd_number_method(9)
    #   [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #   >>>rbasn.create_odd_number_method(15)
    #   [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #   >>>rbasn.create_odd_number_method(100)
    #   [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #   >>>rbasn.create_odd_number_method(500)
    #   [1, 2, 3, 4, 5, 6, 7, 8, 9, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191, 202, 212, 222, 232, 242, 252, 262\
    #   ,272, 282, 292, 303, 313, 323, 333, 343, 353, 363, 373, 383, 393, 404, 414, 424, 434, 444, 454, 464, 474, 484\
    #   , 494]
    # '''
    odd_number_list = []
    for num in range(1,number+1):
        len_of_number_remain = len(str(num))%2
        len_of_number_share = len(str(num))//2
        if len_of_number_remain == 1:
            if len_of_number_share == 0 :
                len_of_number_share = 1
            count_method = 0
            for ct in range(0,len_of_number_share):
                if str(num)[ct]==str(num)[-1-ct]:
                    count_method += 1
                if count_method == len_of_number_share:
                    odd_number_list.append(num)
    return odd_number_list

def merge_sort_list_method(list_1, list_2):
    # '''
    # Input :
    #   -숫자가 들어간 리스트 2개
    # Output :
    #   -2개의 리스트가 합쳐져 작은 숫자부터 ~ 큰 숫자까지 정렬된 값
    # Examples :
    #   >>>import reverse_before_after_same_number as rbasn
    #   >>>list_1 = [4, 2, 1, -1, 2, 3, 4]
    #   >>>list_2 = [-100, -12, -15, 0, 1]
    #   >>>rbasn.merge_sort_list_method(list_1, list_2)
    #   [-100, -15, -12, -1, 0, 1, 1, 2, 2, 3, 4, 4]
    #   >>>list_1 = [1, 0, 1, 1, 0, 0, 1]
    #   >>>list_2 = [-1, -1, -1, 1, 1]
    #   >>>rbasn.merge_sort_list_method(list_1, list_2)
    #   [-1, -1, -1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
    #  '''
    merge_list = list_1 + list_2
    merge_list.sort()

    return merge_list

def main():
    while(True):
        user_input = input("원하는 번째를 입력하세요. : ")
        if user_input == "OUT":
            print("Thanks for this program")
            break
        number = int(input("원하는 숫자의 크기를 입력하세요. : "))

        if number <= 0 or int(user_input) <= 0:
            print("Wrong input")
            continue
        list_1 = create_even_number_method(number)
        list_2 = create_odd_number_method(number)
        merge_list= merge_sort_list_method(list_1,list_2)
        if int(user_input)-1>=len(merge_list):
            print("범위가 존재하지 않습니다.")
        else:
            print(merge_list[int(user_input)-1])


if  __name__ == "__main__":
    main()