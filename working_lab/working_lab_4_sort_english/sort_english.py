def input_english_value():
    # '''
    # Input : 
    #   -변수로써 받지 않고 input함수 사용하여 받을 것
    #   -대소문자 구분없는 알파벳
    # Output :
    #   -대문자 알파벳
    # Examples :
    #   >>>import sort_english as se
    #   >>>se.input_english_value()
    #   영어를 입력해주세요. ex) CCBBAAA : 
    #   영어를 입력해주세요. ex) CCBBAAA : ccbbaaa
    #   CCBBAAA
    #   영어를 입력해주세요. ex) CCBBAAA : 
    #   영어를 입력해주세요. ex) CCBBAAA : SQsdq
    #   SQSDQ
    #   영어를 입력해주세요. ex) CCBBAAA : 
    #   영어를 입력해주세요. ex) CCBBAAA : 123D12S
    #   123D12S
    # '''
    user_value = input("영어를 입력해주세요. ex) CCBBAAA : ").upper()
    return user_value

def dict_of_english():
    # '''
    # Input : 
    #   -없음
    # Output :
    #   -알파벳의 우선순위를 구분할 수 있는 딕셔너리
    #   -알파벳은 영어대문자만 가능   
    #   -알파벳 value 값은 구분만 할수 있으면 됨   
    # Examples :
    #   >>>import sort_english as se
    #   >>>se.dict_of_english()
    #   {'C': 3, 'R': 18, 'W': 23, 'T': 20, 'U': 21, 'Q': 17, 'K': 11, 'Z': 26, 'S': 19, 'V': 22, 'L': 12, 'A': 1, 'Y': 25, 'N': 14, 'H': 8, 'M': 13, 'E': 5, 'O': 15, 'B': 2, 'G': 7, 'P': 16, 'F': 6, 'J': 10, 'I': 9, 'D': 4, 'X': 24}
    # 원한다면 다른숫자 넣어줘도됨
    # '''
    english_dict = {}
    english_list = """ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
    for num in range(len(english_list),0,-1):
        english_dict[english_list[num-1]] = num
    return english_dict

def count_element_method(value):
    # '''
    # Input : 
    #   -input_english_value()의 결과값
    #   -영어는 대문자만 있고 나머지는 상관없는 값
    # Output :
    #   -input값의 각각의 요소들의 개수를 계산하여 딕셔너리 형태의 결과 값
    #   -대문자영어를 제외한 나머지 값들은 삭제됨
    # Examples :
    #   >>>import sort_english as se
    #   >>>se.count_element_method("CCAD21D")
    #   {'C': 2, 'A': 1, 'D':2}
    #   >>>se.count_element_method("QWSASXFQ")
    #   {'W': 2, 'Q': 2, 'F':1, 'A': 1, 'S': 2}
    #   >>>se.count_element_method("")
    #   {}
    #   >>>se.count_element_method("123456")
    #   {}
    # '''
    count_english  = {}

    a = dict_of_english()
    a = a.keys()
    for i in a:
        if value.count(i) == 0:
            continue
        else:
            count_english[i]=value.count(i)
    return count_english

def max_method(count_english):
    # '''
    # Input : 
    #   -count_element_method(variable)의 결과값
    #   -dict형태의 값
    # Output :
    #   -dict형태의 value값들 중에서 제일 큰값
    #   -정수형태의 값
    # Examples :
    #   >>>import sort_english as se
    #   >>>se.max_method({'C': 2, 'A': 1, 'D':2})
    #   2
    #   >>>se.max_method({'W': 3, 'Q': 4, 'F':1, 'A': 1, 'S': 2})
    #   4
    # '''
    count_english_values = max(count_english.values())
    return count_english_values

def check_method(count_english_values,count_english):
    # '''
    # Input : 
    #   -count_english_values: max_method()의 결과값, 자연수
    #   -count_english: count_element_method()의 결과값, 딕트 값
    # Output :
    #   -boolean형으로 나와야 하며 나오는 조건은
    #       1. True
    #           1) count_english_values에 해당하는 자연수가 count_english에 value가 1개이다.
    #       2. False
    #           1) count_english_values에 해당하는 자연수가 count_english에 value가 2개 이상있다.
    # Examples :
    #   >>>import sort_english as se
    #   >>>se.check_method(4, {'W': 2, 'Q': 2, 'F':1, 'A': 4, 'S': 2})
    #   True
    #   >>>se.check_method(2, count_element_method("CCAD21D"))
    #   {'W': 2, 'Q': 2, 'F':1, 'A': 1, 'S': 2}
    #   >>>se.count_element_method("")
    #   False
    # '''
    list_of_count = []
    for value in count_english.values():
        list_of_count.append(value)
    if list_of_count.count(count_english_values) == 1:
        return True
    else:
        return False

def delete_method(count_english_values,count_english):
    # '''
    # Input : 
    #   -count_english_values: max_method()의 결과값, 자연수
    #   -count_english: count_element_method()의 결과값, 딕트 값
    # Output :
    #   -count_english에서 value값이 count_english_values인것을 삭제하고 반환함
    # Examples :
    #   >>>import sort_english as se
    #   >>>se.count_element_method(4, {'W': 2, 'Q': 2, 'F':1, 'A': 4, 'S': 2})
    #   {'W': 2, 'Q': 2, 'S': 2, 'F': 1}
    #   >>>se.count_element_method(2, count_element_method("CCAD21D"))
    #   {'W': 2, 'Q': 2, 'F':1, 'A': 1, 'S': 2}
    # '''
    for i in list(count_english.keys()):
        if count_english.get(i,0) ==count_english_values:
           del count_english[i]

    return count_english

def equal_method(count_english_values,count_english):
    # '''
    # Input : 
    #   -count_english_values: max_method()의 결과값, 자연수
    #   -count_english: count_element_method()의 결과값, 딕트 값
    # Output :
    #   -input값의 count_english에 value값들중에 count_english_values인 key값을 찾아 count_english_values*key 값을 반환해준다.
    # Examples :
    #   >>>import sort_english as se
    #   >>>se.equal_method(4, {'W': 2, 'Q': 4, 'S': 2, 'F': 1})
    #   QQQQ
    #   >>>se.equal_method(3, {'W': 3, 'F': 1})
    #   WWW
    # '''
    for key,value in zip(count_english.keys(),count_english.values()):
            if value == count_english_values:
                return key * value            

def unequal_method(count_english_values,count_english):
    # '''
    # Input : 
    #   -count_english_values: max_method()의 결과값, 자연수
    #   -count_english: count_element_method()의 결과값, 딕트 값
    # Output :
    #   -input값의 count_english에 value값들중에 count_english_values인 key값을 찾아 count_english_values*key 값을 반환해준다.    # Examples :
    #   >>>import sort_english as se
    #   >>>se.unequal_method(4, {'D': 4, 'B': 4, 'A': 4, 'C': 4})
    #   AAAABBBBCCCCDDDD
    #   >>>se.unequal_method(2, {'D': 2, 'B': 2, 'A': 1, 'C': 1})
    #   BBDD
    # '''
    result = ""
    primary_count = []
    primary_english = []
    doct_of_english = dict_of_english()
    change_keys_values = {}
    english_list = """ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
    for num in range(len(doct_of_english),0,-1):
        change_keys_values[num] = english_list[num-1]

    for sentence in count_english.keys():
        if count_english[sentence]==count_english_values:
            primary_english.append(sentence)
            primary_count.append(doct_of_english[sentence])

    for min_value in range(len(primary_english)):
        min_values = min(primary_count)
        result = result + count_english_values * change_keys_values[min_values] 
        primary_english.remove(primary_english[primary_count.index(min_values)])
    
        primary_count.remove(min_values)
    return result
  
def main():
    user_input = 999
    print("Hello world")
    while(user_input != '0'):
        result = ""
        user_input = input_english_value()
        count_english = count_element_method(user_input)
        for loop in set(count_english.values()):
            count_english_values = max_method(count_english)
            check_method_boolean = check_method(count_english_values,count_english)
            if check_method_boolean == True:
                result = result + equal_method(count_english_values,count_english)
                delete_method(count_english_values,count_english)
            elif check_method_boolean == False:
                result = result + unequal_method(count_english_values,count_english)
                delete_method(count_english_values,count_english)
        if len(result) == 0 and user_input != '0':
            print("Wrong input again")
        print(result)
    print("Thank you for use this program")


















main()
