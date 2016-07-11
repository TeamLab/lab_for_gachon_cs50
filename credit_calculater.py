def input_count():
    count_of_subject = int(input("과목의 수를 입력하시요. ex) 3 : "))
    return count_of_subject   

def calculate_value(count_of_subject):
    score_list = []
    credit_list = []
    sum_of_score = 0
    sum_of_credit = 0
    for count in range(count_of_subject):
        score,credit = input("학점과 학점크기를 입력하시요. ex) 4.0-3 : ").split("-")
        score_list.append(float(score))
        credit_list.append(int(credit))
    for num in range(len(score_list)):
        sum_of_score += score_list[num]*credit_list[num]
        sum_of_credit += credit_list[num]
    return sum_of_score/sum_of_credit

def main():
    count_of_subject = input_count()
    print("학점은 " + str(calculate_value(count_of_subject)))

main()



    
