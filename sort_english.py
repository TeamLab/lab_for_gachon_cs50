def input_value():
    value = input("영어를 입력해주세요. ex) CCBBAAA : ").upper()
    return value

def dict_of_english():
    english_dict = {}
    english_list = """ABCDEFGHIJKLMNOPQRSTUVWXYZ"""
    for num in range(len(english_list),0,-1):
        english_dict[english_list[num-1]] = num
    return english_dict

def count_method(value):
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
    input_source = input_value()
    count_english = count_method(input_source) 
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
