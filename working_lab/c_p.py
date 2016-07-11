def input_mode():
    value = input("하고 싶은 기능을 입력하세요. ex) C,P : ").upper()
    if value == "C":
        return True
    elif value == "P":
        return False
 
def input_number():
    front,back = input("숫자들을 입력하세요. ex) 4C2 >> 4,2 : ").split(",")
    return [front,back]

def combination_method(number_list):
    front,back = number_list
    top = 1
    low = 1
    for num in range(int(back)):
        top =top * (int(front) - num)
        low =low* (low + num)
    return top/low

def pambination_method(number_list):
    front,back = number_list
    top = 1
    for num in range(int(back)):
        top = top *(int(front) - num)
    return top

def main():
    type_of_program = input_mode()
    number_list = input_number()

    if type_of_program == True:
        print(combination_method(number_list))
    elif type_of_program == False:
        print(pambination_method(number_list))

if __name__ == "__main__":
    main()
    
