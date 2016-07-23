Working_Lab #2- 가중 학점계산기 (Credit_calculater)
=======
Copyright 2016 © document created by TeamLab.Gachon@gmail.com

## Introduction
이번랩은 나중에 유용하게 쓸 수 있는 lab이다. 네이버가 망해서 학점계산기를 쓸 수 없을때 이걸 쓰면 학점계산을 할 수 있다. 또한 네이버에서 학점계산하는 친구들을 보면서 피식한번해주고 이번숙제로 계산해주길 바란다.

## Credit_calculater Overview
이 숙제를 하기위해서는 일단 가중평균을 알아야한다. 가중평균이란 100원 짜리 배 2개와 200원 짜리 배 3개를 샀을 경우에, (100원x2개 + 200원x3개)/(2개+3개) = 140원 식으로 계산되는걸 말한다.(가격 및 개수 모두를 고려하여 평균함) 우리는 학점크기와 점수를 가지고 계산한다. (학점크기란 2학점, 3학점 점수란 4.5, 4.0, 3.5, 3.0, 2.5 를 말한다.)
본 프로그램은 다음과 같이 세 가지 규칙에 의해 실행된다.

1. 프로그램이 실행되어 사용자가 과목의 개수를 입력한 뒤 과목의 개수만큼 loop가 반복되면서 학점크기와 점수를 입력받는다. 입력받은 값들은 가중평균식(수강생이 할일)에 의해 평균이 구해지고 반환된다.
2. 평균으로 그 사람이 어떤사람인지 정해주고 그 결과를 프린트 해준다. (이해가 안되도 된다. 밑에서 자세히 설명한다.)
3. 초반 숙제이기 때문에 예외처리는 해주지 않는다.

로직 자체는 상당히 간단하고, 이미 배운 내용들로 충분히 구현할 수 있다. 하지만, 처음 해보는 Control 숙제이기 때문에 상당히 어렵게 느껴질 것이다. 이번 Lab은 조금 자세히 설명하니 꼭 문서를 정독하길 바란다.

## 숙제 template 파일 다운로드
먼저 숙제 template 파일을 cs50 서버로부터 다운로드 받는다. 로그인 후 나타나는 `bash shell`에서 다음과 같은 명령을 입력하자.

```bash
python3.4 submit_assignment.py -get credit_calculator
```  

입력되면 다운로드 안내 메세지와 함께 `credit_calculator.py` 파일이 다운로드 된다.

## credit_calculator.py 파일 Overview
`vim editor`로 `credit_calculator.py`을 열어 전체적인 개요를 보자. `vi credit_calculator.py`명령으로 파일을 열어보면 `main` 함수와 `input_count_of_subject`, `score_of_subject_and_size_of_subject`, `calculate_standard_score`, `level_of_score`함수가 존재할 것이다. 본 Lab에서 수정 및 추가해야할 함수는 아래 다섯 가지이다.

함수           | 설명 
--------       | ---
input_count_of_subject| 변수없는 함수인데 계산할 과목의 개수(문자형 정수값)를 입력받는다. 입력받을때 "과목의 수를 입력하시요. ex) 3 : "라는 문구를 띄어준다.
score_of_subject_and_size_of_subject| 학점크기와 점수를 입력받는 함수인데 입력받는 형식은 3-4.5
calculate_standard_score| (n-r) 자연수를 입력받아 해당 자연수의 Factorial 값을 계산하여 반환한다. 즉 4,2를 입력받으면 2을 반환한다.
level_of_score| 1번째 위치에 있는 자연수를 입력받아 해당 자연수의 Factorial 값을 계산하여 반환한다. 즉 3를 입력받으면 6을 반환한다.
main| 사용자가 값을 입력받아 Combination 값을 화면에 출력하도록 한다. 앞장 "Combination Calculator Overview"에 적힌 규칙에 따라 0을 입력하면 프로그램을 종료하고, 계산할 수 없는 값을 입력하면 다시 입력하도록 요청한다.

각 함수별로 작성하는 방법을 살펴보자.

## input_number_check 함수 수정하기
첫 번째 함수는 `input_number_check` 함수이다. 이미 template이 아래와 같이 작성되어 있다. 실제 코드에는 주석이 달려있지만, 설명을 위해 아래에는 생략했다.
```python
def is_positive_number(integer_str_value):
    # 주석생략
    try:
        # ===Modify codes below=============
        # 시작전 반드시 'pass'를 지울 것
        pass

        # ==================================
    except ValueError:
        return False
```
여러분이 수정해야할 영역은 `pass`라고 적힌 부분이다. 보면 `try ~ except ValueError` 라는 부분이 보이는데 현재는 알 필요가 없는 "Exception Handling" 구문이다. Lab 작성을 위해 기본 template을 제시했으니 신경쓰지 말길 바란다. 본 함수에서의 역할은 형변환이 불가능할 경우와 split을 못할 경우 무조건 False를 반환하게 하는 것이다. 예를 들어 `"12321"` 라고 입력된 문자열 값을 `12321.split(",")` 라고 시도할 경우 무조건 본 함수에서 False를 return 하게 한다. 또한  `"ab,cd"` 라고 입력된 문자열 값을 `ab,cd.split(",")` 한 다음 `['ab','cd']` 2개의 값이 크기 비교가 안되면 False를 return 하게 한다.(즉 정수형이 아니면 False)
본 함수의 기본 목적은 사용자가 입력한 값이 split이 가능한지 split을 한 다음 크기비교가 가능한지 보는 것이다. 본 함수는 `user_input`로 입력된다. `pass` 부분을 지우고 indentation에 맞춰서 `user_input`이 위에 조건에 부합하는지 확인하는 조건문을 `if`를 사용하여 작성해보기 바란다. 물론 사용자가 입력하는 값은 문자열이고 split 했을 때도 문자열이기 때문에 해당 값을 먼저 integer 값으로 변환해주어야 한다. 이미 알고 있겠지만 자연수라 함은 "1이상인 정수"를 의미한다. 
다시 정리하면 본 함수에서는 

1. 입력된 user_input이 '0' 이면 True를 반환한다.
2. ","기준으로 split을 해 두개의 변수에 할당이 불가능 하다면 False를 반환한다.
3. 두개의 값이 하나라도 자연수가 아니거나 0번째값이 1번째 값보다 작다면 False를 반환한다.

split한다음 두개의 변수에 할당이 불가능할 경우, `try ~ catch` 문에 의해 자동으로 `False`를 반환하니 신경쓰지 말자. 위의 목적에 맞게 코드를 작성해 보자.

## numerator_value_front_value_factorial 함수 작성하기
두 번째 함수는 `numerator_value_front_value_factorial` 이다. 본 함수는 `front` 라는 자연수 값을 입력받아, 해당 값의 factorial 값을 반환한다. 이미 자연수로 변환된 값만 입력받기 때문에 위 `input_number_check` 함수처럼 입력된 값에 대한 확인을 할 필요가 없다. 
Factorial 값을 구하기 위해서는 많은 방법이 있지만, for문을 활용하는 것이 가장 좋을 것으로 생각된다. for문을 사용하여 1부터 `front` 까지를 모두 곱하는 것이 가장 쉽다. 한가지 조심해야 하는 것은 integer_value을 사용하여 for문을 작성할 경우, 흔히 활용하는 `range(front)`구문을 쓰면 0부터 값이 시작되기 때문에 `range(1,front+1)`로 작성해줘야 한다. 물론 `range` 구문을 쓰는 것 말고도 factorial 값을 구할 수 있는 방법은 무궁무진하다. 수강자가 원하는 어떤 방법을 사용하든 입뎍된 `front`의 Factorial 값만 반환해주면 된다.

## denominator_value_front_minus_back_value_factorial 함수 작성하기
세 번째 함수는 `denominator_value_front_minus_back_value_factorial` 이다. 본 함수는 `front`, `back` 이라는 자연수 값을 입력받아, front-back 값의 factorial 값을 반환한다.

## numerator_value_front_value_factorial 함수 작성하기
네 번째 함수는 `numerator_value_front_value_factorial` 이다. 본 함수는 `back` 이라는 자연수 값을 입력받아, 해당 값의 factorial 값을 반환한다.

## main 함수 수정하기
마지막 함수는 `main`함수이다. `main`함수의 template는 아래와 같다.

```python
def main():
    check_user_input = 999
    # ===Modify codes below=============

    # ==================================
```

참고로 본 Lab에서 설명하는 방법은 많은 구현 방법 중 하나일 뿐이다. 스스로 구현하는 방법이 있다면 그 방법대로 하면 된다. 아래 설명은 구현에 대한 대략적인 설명이다. loop문이나 if문에 대해 이해가 없이 시작하면 이해가 불가능하다. 설명을 이해한 후 스스로 코드를 작성해 보기 바란다. 
`main`함수의 시작은 `check_user_input = 999`이다. `check_user_input`은 사용자가 입력한 값을 할당받는 변수이다. 만약 `check_user_input`이 필요없다고 생각되면 지워도 전혀 문제가 없다. `check_user_input = 999`인 이유는 while문에 진입하기 위해서다. 아래 설명에도 나오지만 본 lab에서는 while문에 종료조건은 `check_user_input`이 True인 경우이다. 제일 처음 시작을 위해 `check_user_input`에 `999`를 할당하였다.
이미 설명이 된 부분이지만, Loop 구문에서 종료를 해야하는 횟수가 정해져 있지 않다면 `while` 문을 쓰는 것이 좋다. 여기에선 "사용자가 0을 입력하면 종료" 라는 조건이 있는 `while(check_user_input is not True):` 이라는 구문으로 시작하면 좋을 것이다. 
`while`문을 실행한 후 처음 할 일은 사용자에게 입력을 받는 것이다. 입력을 받을 때는 `input("Input a positive number : ")` 문을 사용하면 되고, 입력된 값은 `user_input` 변수에 할당한다. 
다음으로 입력된 값이 factorial 값을 계산할 수 있는지 확인하기 위해 if문과 `input_number_check` 함수를 사용한다. `if input_number_check(user_input):` 와 같이 쓰면 입력된 값이 '0'일 때는 `True`를, 계산이 안될 경우는 `False`를 반환하고 나머지경우에 계산을 수행한다.`(#이해가 안가요. 분기를 수행한다가 무슨뜻인지 모르겠습니다.)` 

- 반환된 값이 `True`일 경우 프로그램을 종료한다. 또한 `Thank you for using this program`라는 문자열을 반드시 화면에 출력해주자.
- 반환된 값이 `False`일 경우, `Input again, Please` 이라는 문자열을 출력해주자.
- 나머지 경우는 계산된 값을 출력한후 user_input을 다시 물어보자.
위의 설명은 상당히 복잡하다. 여러분들이 `if`, `while` 문에 대해서 기본적인 이해가 부족하다면 실제로 구현하기 어려울 것이다. 반드시 강의자료를 복습하고 실제 구현을 해보길 바란다.

## 결과 출력하기 
실제 코드가 다 작성되어 `python3.4 factorial_calculator.py` 아래와 같이 결과를 볼 수 있을 것이다. 당연히 입력 부분은 수강자가 직접 입력을 해주어야 프로그램 진행된다.

```bash
Input a positive number : 10
3628800
Input a positive number : 3
6
Input a positive number : 5
120
Input a positive number : abc
Input again, Please
Input a positive number : ls
Input again, Please
Input a positive number : 32.3
Input again, Please
Input a positive number : 0
Thank you for using this program
```

## 숙제 제출하기
모든 함수를 다 수정했다면, 아래와 같이 제출하자
```bash
python3.4 submit_assignment.py -submit factorial_calculator.py
```  
제대로 작성했다면 아래와 같은 메세지가 뜰 것이다.
```bash
-------------------- | ---------- | --------------------
       Function Name |    Passed? |             Feedback
-------------------- | ---------- | --------------------
 input_number_check  |       PASS |             Good Job
 numerator_value_front_value_factorial |       PASS |             Good Job
 denominator_value_front_minus_back_value_factorial |       PASS |             Good Job
 denominator_value_back_value_factorial |       PASS |             Good Job
                main |       PASS |             Good Job
-------------------- | ---------- | --------------------
```  

## Next Work
축하한다. 여러분은 처음으로 프로그램처럼 돌아가는 프로그램을 만들었다. 여러분이 사용하는 웹 브라우저, 엑셀, 파워포인트 등 모든 프로그램에는 본 Lab에서 나오는 `while`, `if`, `for`문들이 사용된다. 어렵게 느껴졌을 지도 모르겠지만, 정말 쉬운 숙제였다. 믿어라. 다음 주는 지옥을 보게 될 것이다.  

> **Human knowledge belongs to the world** - from movie 'Password' -

## Footnotes


[1]: https://ko.wikipedia.org/wiki/%EA%B3%84%EC%8A%B9
