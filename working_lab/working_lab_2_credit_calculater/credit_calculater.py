def input_count_of_subject():
    # '''
    # Input :
    #   -변수로써 받지 않고 input함수 사용하여 받을 것
    #   -input값은 숫자형태의 문자열 값을 넣을 것
    # Output :
    #   -input값의 정수값
    # Example :
    #   >>> import credit_calculator as cc
    #   >>> cc.input_count_of_subject()
    #   과목의 수를 입력하시요. ex) 3 :
    #   과목의 수를 입력하시요. ex) 3 : 4
    #   4
    #   >>> cc.input_count_of_subject()
    #   과목의 수를 입력하시요. ex) 3 :
    #   과목의 수를 입력하시요. ex) 3 : 6
    #   6
    # '''

    count_of_subject = int(input("과목의 수를 입력하시요. ex) 3 : "))
    return count_of_subject   

def score_of_subject_and_size_of_subject():
    # '''
    # Input :
    #   -변수로써 받지 않고 input함수 사용하여 받을 것
    #   -3학점짜리 과목을 4.5의 점수를 받았으면 4.5-3 으로 입력할 것   
    # Output :
    #   -리스트형태로 반환할 것 
    # Examples : 
    #   >>> import credit_calculator as cc
    #   >>> cc.score_of_subject_and_size_of_subject()
    #   학점과 학점크기를 입력하시오. ex) 4.0-3 :
    #   학점과 학점크기를 입력하시오. ex) 4.0-3 : 4.0-3
    #   ['4.0', '3']
    #   >>> cc.score_of_subject_and_size_of_subject()
    #   학점과 학점크기를 입력하시오. ex) 4.0-3 :
    #   학점과 학점크기를 입력하시오. ex) 4.0-3 : 4.0,3
    #   error
    # '''

    score,credit = input("학점과 학점크기를 입력하시요. ex) 4.0-3 : ").split("-")
    return [score,credit]

def calculate_standard_score(count_of_subject):
    # '''
    # Input :
    #   -input_count_of_subject()함수의 결과값(정수값)
    #   -for문을 사용하여 루프마다 score_of_subject_and_size_of_subject() 함수를 통하여 학점과 학점크기가 입력될 것
    # Output :
    #   -input값을 통하여 분모,분자 값을 계산한다음 분모/분자 값을 리턴할것(실수형 숫자)
    # Examples : 
    #   >>> import credit_calculator as cc
    #   >>> cc.calculate_standard_score(3)
    #   학점과 학점크기를 입력하시오. ex) 4.0-3 :
    #   학점과 학점크기를 입력하시오. ex) 4.0-3 : 4.5-3
    #   학점과 학점크기를 입력하시오. ex) 4.0-3 :
    #   학점과 학점크기를 입력하시오. ex) 4.0-3 : 4.0-3
    #   학점과 학점크기를 입력하시오. ex) 4.0-3 :
    #   학점과 학점크기를 입력하시오. ex) 4.0-3 : 3.5-3
    #   3.0
    sum_of_denominator_value = 0
    sum_of_numerator_value = 0
    for count in range(count_of_subject):
        number_list = score_of_subject_and_size_of_subject()
        sum_of_denominator_value += float(number_list[0])*int(number_list[1])
        sum_of_numerator_value += float(number_list[0])
    return sum_of_denominator_value/sum_of_numerator_value

def level_of_score(average_score):
    # '''
    # Input :
    #   -calculate_standard_score함수의 결과값(실수값)
    # Output :
    #   -input값의 크기에 따라 4.5이상 "우등생", 4.0이상 4.5미만 "준우등생", 3.5이상 4.0미만 "정상인", 3.0이상 3.5미만 "준정상인", 나머지 "노력부족" 이라는 문자열 값
    # Examples : 
    #   >>> import credit_calculator as cc
    #   >>> cc.level_of_score(4.0)
    #   준우등생
    #   >>> cc.level_of_score(4.1)
    #   준우등생
    #   >>> cc.level_of_score(4.5)
    #   우등생
    #   >>> cc.level_of_score(3.0)
    #   준정상인
    #   >>> cc.level_of_score(2.0)
    #   노력부족
    # ''' 
    sum_of_denominator_value = 0
    if average_score >=4.5:
        result = "우등생"
    elif average_score >= 4.0:
        result = "준우등생"

    elif average_score >= 3.5:
        result = "정상인"

    elif average_score >= 3.0:
        result = "준정상인"
    
    else:
        result = "노력부족"
    return result
    

def main():
    
    count_of_subject = input_count_of_subject()
    average_score = calculate_standard_score(count_of_subject)
    print(level_of_score(average_score))






    
