Lab #- 가장 작은 수 만들기 (positive_smallest_number)
=============================================
Copyright 2016 © document created by TeamLab.Gachon@gmail.com

## Introduction
이번 과제는 어렵게 느껴질 것이다. 이미 포기할 순 없다. 해보자.


## 숙제 template 파일 다운로드
먼저 숙제 template 파일을 cs50 서버로 부터 다운로드 받는다. 로그인 후 나타나는 bash shell에서 다음과 같은 명령을 입력하자.
```bash
python3.4 submit_assignment.py -get positive_smallest_number
```  
`positive_smallest_number.py` 파일이 다운로드 될 것이다. 받자 마자 실험 차원에서 코드를 실행해보자. `python3.4 positive_smallest_number.py`를 입력하면 된다. 이제 다들 코드를 어떻게 실행하는 지는 알 것이다.  실행하면 아마 아래와 같은 에러 메세지가 뜰 것이다. 


## number_of_character.py 파일 Overview

`vim editor`로 `positive_smallest_number.py`을 열어 전체적인 개요를 보자. `vi positive_smallest_number.py`명령으로 파일을 열어보면 main 함수와 여러개의 함수들이 존재할 것이다. 각 함수들은 여러분께서 직접 작성해서 제출해야 하는 함수이고, main 함수는 실제 positive_smallest_number을 실행하는 함수이다. 각 함수의 구현 내용은 아래와 같다
 수강생이 할일은 크게 두 가지다. 하나는 프로그램 수행을 위해 5개의 함수를 작성하는 것이고, 두 번째는 main 함수에 작성된 5개의 함수를 사용해서 가장 작은 수를 구해 보는 것이다.
 
 
## check_used_list_method 함수 수정하기
첫번째 함수는 사용자 입력 값의 유효여부를 판단하는 함수이다. 이미 비숫한 함수를 change_decimal_to_n에서 작성해보았기 때문에 어렵지 않을 수도 있다. 아래 내용을 참고하여 check_used_list_method 함수를 작성하자.

내용           | 구성 
--------       | ---
함수명      | check_used_list_method
input 변수  | list
Process     | 사용자의 입력값이 정수인지를 판별
output 값   | True, False


## define_plus_miunus_method 함수 수정하기
두 번째 함수는 유효하다고 판별된 사용자의 입력값 중 음의 정수의 포함 여부를 판별하는 함수이다. 아래 내용을 참고하여 define_plus_miunus_method 함수를 작성하자.

내용           | 구성 
--------       | ---
함수명      | define_plus_miunus_method
input 변수  | list
Process     | 입력값 중 음의 정수포함 여부 판별
output 값   | True, False


## make_smallest_number_of_minus 함수 수정하기
이번 함수는 사용자의 입력 값 중 음의 정수가 있을 경우 사용하는 함수이다. 함수의 내용은 아래와 같다.

내용           | 구성 
--------       | ---
함수명      | make_smallest_number_of_minus
input 변수  | list
Process     | 리스트 내의 숫자들을 가장 작은 수를 만들기위한 순서대로 재정렬해준다.
output 값   | list


## make_smallest_number_of_plus 함수 수정하기
이번 함수는 세번째 함수와는 반대로 입력 값이 모두 양의 정수일 경우 사용하는 함수이다. 함수의 내용은 아래와 같다.

내용           | 구성 
--------       | ---
함수명      | make_smallest_number_of_plus
input 변수  | list
Process     | 리스트 내의 숫자들을 가장 작은 수를 만들기위한 순서대로 재정렬해준다.
output 값   | list


## merge_list_to_int 함수 수정하기
마지막 함수다. 이번 함수는 3번째와 4번째 함수의 결과값으로 나온 리스트의 value들을 합쳐 하나의 숫자로 바꿔주는 함수이다. 함수의 내용은 아래와 같다

내용           | 구성 
--------       | ---
함수명      | merge_list_to_int
input 변수  | list
Process     | 입력된 리스트의 value들을 하나의 숫자로 바꿔준다.
output 값   | 정수


## main 함수 수정하기
이제 마지막이다. main함수에서 해야할 것은 각 함수들을 잘 사용하여 입력값에 따른 가장 작은 수가 나올 수 있게 만들어 주는 것이다. 이를 위해서는 main 함수의 수정이 필요하다. main함수에 # ===Modify codes below================= 아랫 부분에 다음의 지시사항에 따라 코드를 작성해주기 바란다.
 
1. `input`이라는 built-in 함수를 이용하여 '숫자들을 입력하세요. ex)3,2,10,-1,0 :' 문자열이 나오고 그 후 숫자를 입력받는다.
2. 사용자로부터 입력받은 값이 유효하면 결과값을 출력 
3. 사용자의 입력값이 유효하지 않다면 'Wrong Input'를 출력해준다.

어떻게 보면 이 함수가 가장 간단한 함수이다. 위의 5개 함수를 호출하고 오타없이 입력만 해주면된다.


## 테스트 및 제출
두 함수를 모두 작성했다면 실행을 해보자. `bash shell`에서 `python3.4 positive_smallest_number.py` 명령어로 실행을 하면된다. 정확히 작성되었다면 아래와 같이 결과를 볼 수 있을 것이다.
```bash
가장 작은 수 만들기
============================
숫자들을 입력하세요. ex)3,2,10,-1,0 : 20, 77,773, 12
122077377
===========================
프로그램이 종료 되었습니다.
```


## 숙제 제출하기
모든 함수를 다 수정했다면 아래와 같이 제출하자
```bash
python3.4 submit_assignment.py -submit positive_smallest_number.py
```

제대로 작성했다면 아래와 같은 메세지가 뜰 것이다.

```bash
-------------------- | ---------- | --------------------
       Function Name |    Passed? |             Feedback
-------------------- | ---------- | --------------------
check_used_list_method|       PASS |             Good Job
define_plus_miunus_method|       PASS |             Good Job
make_smallest_number_of_minus|       PASS |             Good Job
make_smallest_number_of_plus|       PASS |             Good Job
   merge_list_to_int |       PASS |             Good Job
                main |       PASS |             Good Job
                   
-------------------- | ---------- | --------------------
```


## Next Work
느끼겠지만, 더 이상의 친절함은 없다. 점점 스스로 혼자 헤쳐나가야 한다. 많은 에러 메세지와 사투를 벌여야 하고, 왠지 모르지만 안되는 이유를 찾아야 한다. 이젠 구글에 익숙해 지길 바란다. 구글 검색이야 말로 최고의 프로그래머가 되는 지름길이다. 마지막 lab 으로 가자!

> **Human knowledge belongs to the world** - from movie 'Password' -


## Footnotes
