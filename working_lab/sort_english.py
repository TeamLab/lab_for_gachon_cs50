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
    count_english_values = max(count_english.values())
    return count_english_values

def check_method(count_english_values,count_english):
    list_of_count = []
    for value in count_english.values():
        list_of_count.append(value)
    if list_of_count.count(count_english_values) == 1:
        return True
    else:
        return False

def delete_method(count_english_values,count_english):
    for i in list(count_english.keys()):
        if count_english.get(i,0) ==count_english_values:
           del count_english[i]
            
    return count_english

def equal_method(count_english_values,count_english):
    for key,value in zip(count_english.keys(),count_english.values()):
            if value == count_english_values:
                return key * value            

def unequal_method(count_english_values,count_english):
    result = ""
    primary_count = []
    primary_english = []
    doct_of_english = dict_of_english()
    change_keys_values = {}
    english_list = """ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
    for num in range(len(doct_of_english),0,-1):
        change_keys_values[num] = english_list[num-1]

    for sentence in count_english:
        primary_english.append(sentence)
        primary_count.append(doct_of_english[sentence])
    for min_value in range(len(primary_english)):
        min_values = min(primary_count)
        result = result + count_english_values * change_keys_values[min_values] 
        primary_english.remove(primary_english[primary_count.index(min_values)])
    
        primary_count.remove(min_values)
    return result
  
def main():
    result = ""
    input_source = input_english_value()
    count_english = count_element_method(input_source) 
    for i in set(count_english.values()):
        count_english_values = max_method(count_english)
        check_method_boolean = check_method(count_english_values,count_english)
        if check_method_boolean == True:
            result = result + equal_method(count_english_values,count_english)
            delete_method(count_english_values,count_english)
        elif check_method_boolean == False:
            result = result + unequal_method(count_english_values,count_english)
            delete_method(count_english_values,count_english)
    print(result)
    

















main()
