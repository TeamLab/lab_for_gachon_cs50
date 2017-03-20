def availabe_user_input(user_input):
    # """
    # Input:
    # 	- String Type의 숫자
    # Output:
    # 	- True, False와 같은 Boolean형
    # Examples(python shell):
    # 	>>> import x_queen as xq
    # 	>>> xq.availabe_user_input(3)
    #   False
    # 	>>> import x_queen as xq
    # 	>>> xq.availabe_user_input("gachon")
    #   False
    # 	>>> import x_queen as xq
    # 	>>> xq.availabe_user_input("3")
    #   True
    # """
    try:
        if user_input.isdigit() and int(user_input)>0:
            return True
        else:
            return False
    except:
        return False

def make_str_value_to_range(str_value):
    # """
    # Input:
    # 	- String Type의 숫자
    # Output:
    # 	- 정수형 자료가 들어간 리스트
    # Examples(python shell):
    # 	>>> import x_queen as xq
    # 	>>> xq.make_str_value_to_range("4")
    #   [0,1,2,3]
    # 	>>> import x_queen as xq
    # 	>>> xq.availabe_user_input("10")
    #   [0,1,2,3,4,5,6,7,8,9]
    # """
    int_range = range(int(str_value))
    list_int_range = list(int_range)
    return list_int_range

def merge_a_lot_of_case_of_user_input_row(user_input):
    # """
    # Input:
    # 	- 정수형 자료가 들어간 리스트
    #   -  make_str_value_to_range(변수) 함수의 결과값
    # Output:
    # 	- 정수형 자료가 들어간 이중리스트
    #   - 숫자들에 대한 모든 조합이 들어간 리스트
    # Examples(python shell):
    # 	>>> import x_queen as xq
    # 	>>> xq.merge_a_lot_of_case_of_user_input_row([0,1,2,3])
    #   [[0, 1, 2, 3], [0, 1, 3, 2], [0, 2, 1, 3], [0, 2, 3, 1], [0, 3, 1, 2], [0, 3, 2, 1], [1, 0, 2, 3], [1, 0, 3, 2], [1, 2, 0, 3], [1, 2, 3, 0]
    #   , [1, 3, 0, 2], [1, 3, 2, 0], [2, 0, 1, 3], [2, 0, 3, 1], [2, 1, 0, 3], [2, 1, 3, 0], [2, 3, 0, 1], [2, 3, 1, 0], [3, 0, 1, 2], [3, 0, 2, 1]
    #   , [3, 1, 0, 2], [3, 1, 2, 0], [3, 2, 0, 1], [3, 2, 1, 0]]
    # 	>>> xq.merge_a_lot_of_case_of_user_input_row([0,1,2])
    #   [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
    # 	>>> xq.merge_a_lot_of_case_of_user_input_row([1,2,4,7])
    #   [[1, 2, 4, 7], [1, 2, 7, 4], [1, 4, 2, 7], [1, 4, 7, 2], [1, 7, 2, 4], [1, 7, 4, 2], [2, 1, 4, 7], [2, 1, 7, 4]
    #   ,[2, 4, 1, 7], [2, 4, 7, 1], [2, 7, 1, 4], [2, 7, 4, 1], [4, 1, 2, 7], [4, 1, 7, 2], [4, 2, 1, 7], [4, 2, 7, 1]
    #   ,[4, 7, 1, 2], [4, 7, 2, 1], [7, 1, 2, 4], [7, 1, 4, 2], [7, 2, 1, 4], [7, 2, 4, 1], [7, 4, 1, 2], [7, 4, 2, 1]]
    # """
    if len(user_input) == 0:
        return []
    elif len(user_input) ==1:
        return [user_input]
    else:
        user_input = list(user_input)
        result = []
        for index in range(len(user_input)):
            first_value = user_input[index]
            next_value = user_input[:index] + user_input[index+1:]
            for next_v in merge_a_lot_of_case_of_user_input_row(next_value):
                result.append([first_value]+next_v)
        for index_1 in range(len(result)):
            for index_2 in range(len(result[0])):
                result[index_1][index_2]= int(result[index_1][index_2])
        return result

def make_target_of_coordinates(user_list):
    # """
    # Input:
    # 	- 정수형 자료가 들어간 이중리스트
    #   - merge_a_lot_of_case_of_user_input_row(변수) 함수의 결과값
    # Output:
    # 	- 정수형 자료가 들어간 삼중리스트
    #   - input으로 들어온 정보를 좌표로 만들어줘 반환
    # Examples(python shell):
    # 	>>> import x_queen as xq
    # 	>>> value_1 = [[0, 1, 2, 3], [0, 1, 3, 2], [0, 2, 1, 3], [0, 2, 3, 1], [0, 3, 1, 2], [0, 3, 2, 1], [1, 0, 2, 3]
    #   , [1, 0, 3, 2], [1, 2, 0, 3], [1, 2, 3, 0], [1, 3, 0, 2], [1, 3, 2, 0], [2, 0, 1, 3], [2, 0, 3, 1]
    #   , [2, 1, 0, 3], [2, 1, 3, 0], [2, 3, 0, 1], [2, 3, 1, 0], [3, 0, 1, 2], [3, 0, 2, 1], [3, 1, 0, 2], [3, 1, 2, 0]
    #   , [3, 2, 0, 1], [3, 2, 1, 0]]
    # 	>>> xq.make_target_of_coordinates(value_1)
    #   [[[0, 0], [1, 1], [2, 2], [3, 3]], [[0, 0], [1, 1], [2, 3], [3, 2]], [[0, 0], [1, 2], [2, 1], [3, 3]]
    #   , [[0, 0], [1, 2], [2, 3], [3, 1]], [[0, 0], [1, 3], [2, 1], [3, 2]], [[0, 0], [1, 3], [2, 2], [3, 1]]
    #   , [[0, 1], [1, 0], [2, 2], [3, 3]], [[0, 1], [1, 0], [2, 3], [3, 2]], [[0, 1], [1, 2], [2, 0], [3, 3]]
    #   , [[0, 1], [1, 2], [2, 3], [3, 0]], [[0, 1], [1, 3], [2, 0], [3, 2]], [[0, 1], [1, 3], [2, 2], [3, 0]]
    #   , [[0, 2], [1, 0], [2, 1], [3, 3]], [[0, 2], [1, 0], [2, 3], [3, 1]], [[0, 2], [1, 1], [2, 0], [3, 3]]
    #   , [[0, 2], [1, 1], [2, 3], [3, 0]], [[0, 2], [1, 3], [2, 0], [3, 1]], [[0, 2], [1, 3], [2, 1], [3, 0]]
    #   , [[0, 3], [1, 0], [2, 1], [3, 2]], [[0, 3], [1, 0], [2, 2], [3, 1]], [[0, 3], [1, 1], [2, 0], [3, 2]]
    #   , [[0, 3], [1, 1], [2, 2], [3, 0]], [[0, 3], [1, 2], [2, 0], [3, 1]], [[0, 3], [1, 2], [2, 1], [3, 0]]]
    #   >>> value_2 = [[1, 2, 4, 7], [1, 2, 7, 4], [1, 4, 2, 7], [1, 4, 7, 2], [1, 7, 2, 4], [1, 7, 4, 2], [2, 1, 4, 7]
    #   , [2, 1, 7, 4], [2, 4, 1, 7], [2, 4, 7, 1], [2, 7, 1, 4], [2, 7, 4, 1], [4, 1, 2, 7], [4, 1, 7, 2], [4, 2, 1, 7]
    #   , [4, 2, 7, 1], [4, 7, 1, 2], [4, 7, 2, 1], [7, 1, 2, 4], [7, 1, 4, 2], [7, 2, 1, 4], [7, 2, 4, 1], [7, 4, 1, 2]
    #   , [7, 4, 2, 1]]
    # 	>>> xq.make_target_of_coordinates(value_2)
    #   [[[0, 1], [1, 2], [2, 4], [3, 7]], [[0, 1], [1, 2], [2, 7], [3, 4]], [[0, 1], [1, 4], [2, 2], [3, 7]]
    #   , [[0, 1], [1, 4], [2, 7], [3, 2]], [[0, 1], [1, 7], [2, 2], [3, 4]], [[0, 1], [1, 7], [2, 4], [3, 2]]
    #   , [[0, 2], [1, 1], [2, 4], [3, 7]], [[0, 2], [1, 1], [2, 7], [3, 4]], [[0, 2], [1, 4], [2, 1], [3, 7]]
    #   , [[0, 2], [1, 4], [2, 7], [3, 1]], [[0, 2], [1, 7], [2, 1], [3, 4]], [[0, 2], [1, 7], [2, 4], [3, 1]]
    #   , [[0, 4], [1, 1], [2, 2], [3, 7]], [[0, 4], [1, 1], [2, 7], [3, 2]], [[0, 4], [1, 2], [2, 1], [3, 7]]
    #   , [[0, 4], [1, 2], [2, 7], [3, 1]], [[0, 4], [1, 7], [2, 1], [3, 2]], [[0, 4], [1, 7], [2, 2], [3, 1]]
    #   , [[0, 7], [1, 1], [2, 2], [3, 4]], [[0, 7], [1, 1], [2, 4], [3, 2]], [[0, 7], [1, 2], [2, 1], [3, 4]]
    #   , [[0, 7], [1, 2], [2, 4], [3, 1]], [[0, 7], [1, 4], [2, 1], [3, 2]], [[0, 7], [1, 4], [2, 2], [3, 1]]]
    # """
    total_list = []
    list_index = 0
    for case_one in user_list:
        total_list.append([])
        row_value = 0
        for case_one_value in case_one:
            total_list[list_index].append([row_value]+[case_one_value])
            row_value +=1
        list_index += 1
    return total_list

def check_row_culumn_extract_list(total_list):
    # """
    # Input:
    # 	- 좌표로 만들어진 정수형 자료가 들어간 삼중리스트
    #   - make_target_of_coordinates(변수) 함수의 결과값
    # Output:
    # 	- 한개의 리스트 안에서 반복되는 요소들이 사라진 이중리스트
    #     부가설명
    #        - input 으로 들어온 변수를 분석해보자면 이중리스트를 여러개가 모였는데 그 자체를 또 리스트로 감싸준 형태이다
    #           거기서 이중리스트는 한 경우의 케이스인데 예를 들어보겠다.
    #            1. [[0, 0], [1, 1], [2, 2], [3, 3]] 는 Output으로 나와야 하는 함수이다.
    #                 X O O O
    #                 O X O O
    #                 O O X O
    #                 O O O X
    #            2. [[0, 1], [1, 1], [2, 2], [3, 3]] 는 Output으로 나오면 안되는 함수이다.
    #                 X O X X
    #                 X O X X
    #                 X O X X
    #                 X O X X
    #      부가설명2
    #         - 이처럼 가로,세로에 한개의 체스판이 존재하는 케이스만 결과값으로 나오면 된다.
    #   - 리스트의 각각의 요소는 정수형
    # Examples(python shell):
    # 	>>> import x_queen as xq
    # 	>>> value_1 = [[[0, 0], [1, 1], [2, 2], [3, 3]], [[0, 0], [1, 1], [2, 3], [3, 2]], [[0, 0], [1, 2], [2, 1], [3, 3]]
    #   , [[0, 0], [1, 2], [2, 3], [3, 1]], [[0, 0], [1, 3], [2, 1], [3, 2]], [[0, 0], [1, 3], [2, 2], [3, 1]]
    #   , [[0, 1], [1, 0], [2, 2], [3, 3]], [[0, 1], [1, 0], [2, 3], [3, 2]], [[0, 1], [1, 2], [2, 0], [3, 3]]
    #   , [[0, 1], [1, 2], [2, 3], [3, 0]], [[0, 1], [1, 3], [2, 0], [3, 2]], [[0, 1], [1, 3], [2, 2], [3, 0]]
    #   , [[0, 2], [1, 0], [2, 1], [3, 3]], [[0, 2], [1, 0], [2, 3], [3, 1]], [[0, 2], [1, 1], [2, 0], [3, 3]]
    #   , [[0, 2], [1, 1], [2, 3], [3, 0]], [[0, 2], [1, 3], [2, 0], [3, 1]], [[0, 2], [1, 3], [2, 1], [3, 0]]
    #   , [[0, 3], [1, 0], [2, 1], [3, 2]], [[0, 3], [1, 0], [2, 2], [3, 1]], [[0, 3], [1, 1], [2, 0], [3, 2]]
    #   , [[0, 3], [1, 1], [2, 2], [3, 0]], [[0, 3], [1, 2], [2, 0], [3, 1]], [[0, 3], [1, 2], [2, 1], [3, 0]]]
    # 	>>> xq.check_row_culumn_extract_list(value_1)
    #   [[0, 1, 2, 3], [0, 1, 3, 2], [0, 2, 1, 3], [0, 2, 3, 1], [0, 3, 1, 2], [0, 3, 2, 1], [1, 0, 2, 3]
    #   , [1, 0, 3, 2], [1, 2, 0, 3], [1, 2, 3, 0], [1, 3, 0, 2], [1, 3, 2, 0], [2, 0, 1, 3], [2, 0, 3, 1]
    #   , [2, 1, 0, 3], [2, 1, 3, 0], [2, 3, 0, 1], [2, 3, 1, 0], [3, 0, 1, 2], [3, 0, 2, 1], [3, 1, 0, 2], [3, 1, 2, 0]
    #   , [3, 2, 0, 1], [3, 2, 1, 0]]
    #   >>> value_2 = [[[0, 1], [1, 2], [2, 4], [3, 7]], [[0, 1], [1, 2], [2, 7], [3, 4]], [[0, 1], [1, 4], [2, 2], [3, 7]]
    #   , [[0, 1], [1, 4], [2, 7], [3, 2]], [[0, 1], [1, 7], [2, 2], [3, 4]], [[0, 1], [1, 7], [2, 4], [3, 2]]
    #   , [[0, 2], [1, 1], [2, 4], [3, 7]], [[0, 2], [1, 1], [2, 7], [3, 4]], [[0, 2], [1, 4], [2, 1], [3, 7]]
    #   , [[0, 2], [1, 4], [2, 7], [3, 1]], [[0, 2], [1, 7], [2, 1], [3, 4]], [[0, 2], [1, 7], [2, 4], [3, 1]]
    #   , [[0, 4], [1, 1], [2, 2], [3, 7]], [[0, 4], [1, 1], [2, 7], [3, 2]], [[0, 4], [1, 2], [2, 1], [3, 7]]
    #   , [[0, 4], [1, 2], [2, 7], [3, 1]], [[0, 4], [1, 7], [2, 1], [3, 2]], [[0, 4], [1, 7], [2, 2], [3, 1]]
    #   , [[0, 7], [1, 1], [2, 2], [3, 4]], [[0, 7], [1, 1], [2, 4], [3, 2]], [[0, 7], [1, 2], [2, 1], [3, 4]]
    #   , [[0, 7], [1, 2], [2, 4], [3, 1]], [[0, 7], [1, 4], [2, 1], [3, 2]], [[0, 7], [1, 4], [2, 2], [3, 1]]]
    # 	>>> xq.check_row_culumn_extract_list(value_2)
    #   [[1, 2, 4, 7], [1, 2, 7, 4], [1, 4, 2, 7], [1, 4, 7, 2], [1, 7, 2, 4], [1, 7, 4, 2], [2, 1, 4, 7]
    #   , [2, 1, 7, 4], [2, 4, 1, 7], [2, 4, 7, 1], [2, 7, 1, 4], [2, 7, 4, 1], [4, 1, 2, 7], [4, 1, 7, 2], [4, 2, 1, 7]
    #   , [4, 2, 7, 1], [4, 7, 1, 2], [4, 7, 2, 1], [7, 1, 2, 4], [7, 1, 4, 2], [7, 2, 1, 4], [7, 2, 4, 1], [7, 4, 1, 2]
    #   , [7, 4, 2, 1]]
    # """
    result_row = []
    result_column = []
    return_result = []
    for index_1 in range(len(total_list)):
        check_result_row = []
        check_result_column = []
        for index_2 in range(len(total_list[0])):
            check_result_row.append(total_list[index_1][index_2][0])
            check_result_column.append(total_list[index_1][index_2][1])
        if len(set(check_result_row)) == len(total_list[0]) and len(set(check_result_column)) == len(total_list[0]):
            result_row += check_result_row
            result_column += check_result_column
    two_mention_index = 0
    for result_column_index in range(len(result_column)):
        if result_column_index == 0:
            return_result.append([])
            return_result[two_mention_index].append(result_column[result_column_index])
        elif result_column_index % len(total_list[0]) ==0:
            two_mention_index += 1
            return_result.append([])
            return_result[two_mention_index].append(result_column[result_column_index])
        else:
            return_result[two_mention_index].append(result_column[result_column_index])
    return return_result


def check_cross_extract_list(total_list):
    # """
    # Input:
    # 	- 좌표로 만들어진 정수형 자료가 들어간 삼중리스트
    #   - make_target_of_coordinates(변수) 함수의 결과값
    # Output:
    # 	- 한개의 리스트 안에서 반복되는 요소들이 사라진 이중리스트
    #     부가설명
    #        - input 으로 들어온 변수를 분석해보자면 이중리스트를 여러개가 모였는데 그 자체를 또 리스트로 감싸준 형태이다
    #           거기서 이중리스트는 한 경우의 케이스인데 예를 들어보겠다.
    #            1. [[0, 1], [1, 3], [2, 0], [3, 2]] 는 Output으로 나와야 하는 함수이다.
    #                 O X O O
    #                 O O O X
    #                 X O O O
    #                 O O X O
    #            2.  [[0, 0], [1, 0], [2, 0], [3, 0]] 는 Output으로 나와야 하는 함수이다.
    #                 X O O O
    #                 X O O O
    #                 X O O O
    #                 X O O O
    #            3.  [[0, 0], [1, 1], [2, 2], [3, 3]] 는 Output으로 나오면 안되는 함수이다.
    #                 X O O O
    #                 O X O O
    #                 O O X O
    #                 O O O X
    #      부가설명2
    #         - 이처럼 왼쪽, 오른쪽 대각선에 한개의 체스판이 존재하는 케이스만 결과값으로 나오면 된다.
    # Examples(python shell):
    # 	>>> import x_queen as xq
    # 	>>> value_1 = [[[0, 0], [1, 1], [2, 2], [3, 3]], [[0, 0], [1, 1], [2, 3], [3, 2]], [[0, 0], [1, 2], [2, 1], [3, 3]]
    #   , [[0, 0], [1, 2], [2, 3], [3, 1]], [[0, 0], [1, 3], [2, 1], [3, 2]], [[0, 0], [1, 3], [2, 2], [3, 1]]
    #   , [[0, 1], [1, 0], [2, 2], [3, 3]], [[0, 1], [1, 0], [2, 3], [3, 2]], [[0, 1], [1, 2], [2, 0], [3, 3]]
    #   , [[0, 1], [1, 2], [2, 3], [3, 0]], [[0, 1], [1, 3], [2, 0], [3, 2]], [[0, 1], [1, 3], [2, 2], [3, 0]]
    #   , [[0, 2], [1, 0], [2, 1], [3, 3]], [[0, 2], [1, 0], [2, 3], [3, 1]], [[0, 2], [1, 1], [2, 0], [3, 3]]
    #   , [[0, 2], [1, 1], [2, 3], [3, 0]], [[0, 2], [1, 3], [2, 0], [3, 1]], [[0, 2], [1, 3], [2, 1], [3, 0]]
    #   , [[0, 3], [1, 0], [2, 1], [3, 2]], [[0, 3], [1, 0], [2, 2], [3, 1]], [[0, 3], [1, 1], [2, 0], [3, 2]]
    #   , [[0, 3], [1, 1], [2, 2], [3, 0]], [[0, 3], [1, 2], [2, 0], [3, 1]], [[0, 3], [1, 2], [2, 1], [3, 0]]]
    # 	>>> xq.check_cross_extract_list(value_1)
    #   [[1, 3, 0, 2], [2, 0, 3, 1]]
    #   >>> value_2 = [[[0, 1], [1, 2], [2, 4], [3, 7]], [[0, 1], [1, 2], [2, 7], [3, 4]], [[0, 1], [1, 4], [2, 2], [3, 7]]
    #   , [[0, 1], [1, 4], [2, 7], [3, 2]], [[0, 1], [1, 7], [2, 2], [3, 4]], [[0, 1], [1, 7], [2, 4], [3, 2]]
    #   , [[0, 2], [1, 1], [2, 4], [3, 7]], [[0, 2], [1, 1], [2, 7], [3, 4]], [[0, 2], [1, 4], [2, 1], [3, 7]]
    #   , [[0, 2], [1, 4], [2, 7], [3, 1]], [[0, 2], [1, 7], [2, 1], [3, 4]], [[0, 2], [1, 7], [2, 4], [3, 1]]
    #   , [[0, 4], [1, 1], [2, 2], [3, 7]], [[0, 4], [1, 1], [2, 7], [3, 2]], [[0, 4], [1, 2], [2, 1], [3, 7]]
    #   , [[0, 4], [1, 2], [2, 7], [3, 1]], [[0, 4], [1, 7], [2, 1], [3, 2]], [[0, 4], [1, 7], [2, 2], [3, 1]]
    #   , [[0, 7], [1, 1], [2, 2], [3, 4]], [[0, 7], [1, 1], [2, 4], [3, 2]], [[0, 7], [1, 2], [2, 1], [3, 4]]
    #   , [[0, 7], [1, 2], [2, 4], [3, 1]], [[0, 7], [1, 4], [2, 1], [3, 2]], [[0, 7], [1, 4], [2, 2], [3, 1]]]
    # 	>>> xq.check_cross_extract_list(value_2)
    #   [[1, 4, 2, 7], [1, 7, 4, 2], [2, 4, 1, 7], [2, 4, 7, 1], [2, 7, 1, 4], [4, 1, 7, 2], [7, 1, 4, 2], [7, 2, 4, 1]]
    # """
    return_result = []
    for index in range(len(total_list)):
        result_list_row = []
        result_list_column = []
        for case_one in total_list[index]:
            result_list_row.append(case_one[0])
            result_list_column.append(case_one[1])
        row_count = 0
        column_count = 1
        true_count = 0
        change_row_count_value = 0
        loop = int(len(result_list_row) * (len(result_list_row) - 1) / 2)
        for i in range(loop):
            if abs(result_list_row[row_count] - result_list_row[column_count]) != abs(result_list_column[row_count] - result_list_column[column_count]):
                true_count += 1
            if column_count == len(result_list_row) - 1:
                change_row_count_value += 1
                row_count = change_row_count_value
                column_count = row_count
            column_count += 1

        if true_count == loop:
            return_result.append(result_list_column)
    return return_result

def same_list_extract_two_list(row_culumn_extract_list,cross_extract_list):
    # """
    # Input:
    # 	- row_culumn_extract_list : 정수형 타입이 들어간 이중리스트
    # 	- cross_extract_list : 정수형 타입이 들어간 이중리스트
    # Output:
    # 	- row_culumn_extract_list, cross_extract_list 두개의 변수중에서 공통되는 리스트를 반환
    # Examples(python shell):
    # 	>>> import x_queen as xq
    # 	>>> range_user_input = xq.make_str_value_to_range(4)
    # 	>>> case_user_input = xq.merge_a_lot_of_case_of_user_input_row(range_user_input)
    # 	>>> coordinates_of_user_input = xq.make_target_of_coordinates(case_user_input)
    # 	>>> row_culumn_extract_list = xq.check_row_culumn_extract_list(coordinates_of_user_input)
    # 	>>> cross_extract_list = xq.check_cross_extract_list(coordinates_of_user_input)
    # 	>>> xq.same_list_extract_two_list(row_culumn_extract_list, cross_extract_list)
    #   [[1, 3, 0, 2], [2, 0, 3, 1]]
    # 	>>> range_user_input = xq.make_str_value_to_range(8)
    # 	>>> case_user_input = xq.merge_a_lot_of_case_of_user_input_row(range_user_input)
    # 	>>> coordinates_of_user_input = xq.make_target_of_coordinates(case_user_input)
    # 	>>> row_culumn_extract_list = xq.check_row_culumn_extract_list(coordinates_of_user_input)
    # 	>>> cross_extract_list = xq.check_cross_extract_list(coordinates_of_user_input)
    # 	>>> xq.same_list_extract_two_list(row_culumn_extract_list, cross_extract_list)
    #   [[0, 4, 7, 5, 2, 6, 1, 3], [0, 5, 7, 2, 6, 3, 1, 4], [0, 6, 3, 5, 7, 1, 4, 2], [0, 6, 4, 7, 1, 3, 5, 2]
    #   , [1, 3, 5, 7, 2, 0, 6, 4], [1, 4, 6, 0, 2, 7, 5, 3], [1, 4, 6, 3, 0, 7, 5, 2], [1, 5, 0, 6, 3, 7, 2, 4]
    #   , [1, 5, 7, 2, 0, 3, 6, 4], [1, 6, 2, 5, 7, 4, 0, 3], [1, 6, 4, 7, 0, 3, 5, 2], [1, 7, 5, 0, 2, 4, 6, 3]
    #   , [2, 0, 6, 4, 7, 1, 3, 5], [2, 4, 1, 7, 0, 6, 3, 5], [2, 4, 1, 7, 5, 3, 6, 0], [2, 4, 6, 0, 3, 1, 7, 5]
    #   , [2, 4, 7, 3, 0, 6, 1, 5], [2, 5, 1, 4, 7, 0, 6, 3], [2, 5, 1, 6, 0, 3, 7, 4], [2, 5, 1, 6, 4, 0, 7, 3]
    #   , [2, 5, 3, 0, 7, 4, 6, 1], [2, 5, 3, 1, 7, 4, 6, 0], [2, 5, 7, 0, 3, 6, 4, 1], [2, 5, 7, 0, 4, 6, 1, 3]
    #   , [2, 5, 7, 1, 3, 0, 6, 4], [2, 6, 1, 7, 4, 0, 3, 5], [2, 6, 1, 7, 5, 3, 0, 4], [2, 7, 3, 6, 0, 5, 1, 4]
    #   , [3, 0, 4, 7, 1, 6, 2, 5], [3, 0, 4, 7, 5, 2, 6, 1], [3, 1, 4, 7, 5, 0, 2, 6], [3, 1, 6, 2, 5, 7, 0, 4]
    #   , [3, 1, 6, 2, 5, 7, 4, 0], [3, 1, 6, 4, 0, 7, 5, 2], [3, 1, 7, 4, 6, 0, 2, 5], [3, 1, 7, 5, 0, 2, 4, 6]
    #   , [3, 5, 0, 4, 1, 7, 2, 6], [3, 5, 7, 1, 6, 0, 2, 4], [3, 5, 7, 2, 0, 6, 4, 1], [3, 6, 0, 7, 4, 1, 5, 2]
    #   , [3, 6, 2, 7, 1, 4, 0, 5], [3, 6, 4, 1, 5, 0, 2, 7], [3, 6, 4, 2, 0, 5, 7, 1], [3, 7, 0, 2, 5, 1, 6, 4]
    #   , [3, 7, 0, 4, 6, 1, 5, 2], [3, 7, 4, 2, 0, 6, 1, 5], [4, 0, 3, 5, 7, 1, 6, 2], [4, 0, 7, 3, 1, 6, 2, 5]
    #   , [4, 0, 7, 5, 2, 6, 1, 3], [4, 1, 3, 5, 7, 2, 0, 6], [4, 1, 3, 6, 2, 7, 5, 0], [4, 1, 5, 0, 6, 3, 7, 2]
    #   , [4, 1, 7, 0, 3, 6, 2, 5], [4, 2, 0, 5, 7, 1, 3, 6], [4, 2, 0, 6, 1, 7, 5, 3], [4, 2, 7, 3, 6, 0, 5, 1]
    #   , [4, 6, 0, 2, 7, 5, 3, 1], [4, 6, 0, 3, 1, 7, 5, 2], [4, 6, 1, 3, 7, 0, 2, 5], [4, 6, 1, 5, 2, 0, 3, 7]
    #   , [4, 6, 1, 5, 2, 0, 7, 3], [4, 6, 3, 0, 2, 7, 5, 1], [4, 7, 3, 0, 2, 5, 1, 6], [4, 7, 3, 0, 6, 1, 5, 2]
    #   , [5, 0, 4, 1, 7, 2, 6, 3], [5, 1, 6, 0, 2, 4, 7, 3], [5, 1, 6, 0, 3, 7, 4, 2], [5, 2, 0, 6, 4, 7, 1, 3]
    #   , [5, 2, 0, 7, 3, 1, 6, 4], [5, 2, 0, 7, 4, 1, 3, 6], [5, 2, 4, 6, 0, 3, 1, 7], [5, 2, 4, 7, 0, 3, 1, 6]
    #   , [5, 2, 6, 1, 3, 7, 0, 4], [5, 2, 6, 1, 7, 4, 0, 3], [5, 2, 6, 3, 0, 7, 1, 4], [5, 3, 0, 4, 7, 1, 6, 2]
    #   , [5, 3, 1, 7, 4, 6, 0, 2], [5, 3, 6, 0, 2, 4, 1, 7], [5, 3, 6, 0, 7, 1, 4, 2], [5, 7, 1, 3, 0, 6, 4, 2]
    #   , [6, 0, 2, 7, 5, 3, 1, 4], [6, 1, 3, 0, 7, 4, 2, 5], [6, 1, 5, 2, 0, 3, 7, 4], [6, 2, 0, 5, 7, 4, 1, 3]
    #   , [6, 2, 7, 1, 4, 0, 5, 3], [6, 3, 1, 4, 7, 0, 2, 5], [6, 3, 1, 7, 5, 0, 2, 4], [6, 4, 2, 0, 5, 7, 1, 3]
    #   , [7, 1, 3, 0, 6, 4, 2, 5], [7, 1, 4, 2, 0, 6, 3, 5], [7, 2, 0, 5, 1, 4, 6, 3], [7, 3, 0, 2, 5, 1, 6, 4]]
    # """
    same_list = []
    for row_culumn in row_culumn_extract_list:
        for cross in cross_extract_list:
            if row_culumn==cross:
                same_list.append(cross)
    return same_list

def main():

    user_input  =  input("원하는 체스판의 크기를 입력해주세요. : ")
    range_user_input = make_str_value_to_range(user_input)
    case_user_input = merge_a_lot_of_case_of_user_input_row(range_user_input)
    coordinates_of_user_input = make_target_of_coordinates(case_user_input)
    row_culumn_extract_list = check_row_culumn_extract_list(coordinates_of_user_input)
    cross_extract_list = check_cross_extract_list(coordinates_of_user_input)
    same_list = same_list_extract_two_list(row_culumn_extract_list,cross_extract_list)
    count = 1
    for index in range(len(same_list)):
        print('Solution ' + str(count)+': '+ str(same_list[index])+ '\n')
        for value in same_list[index]:
            print(" O "*value+" X "+" O "*(int(user_input)-value-1))
        print('\n')
        count +=1

if __name__=="__main__":
    main()