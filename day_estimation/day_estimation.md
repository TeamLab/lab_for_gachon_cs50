Working_Lab #3- 일 추정기 (Day_estimation)
=======
Copyright 2016 © document created by TeamLab.Gachon@gmail.com

## Introduction
이번 Lab은 처음으로 list라는 개념과 main함수 코딩을 배운다. 언제까지 주먹으로 3월달이 31일일까지 있다는것을 확인할 것인가? 또한 2월달은 달력을 보고 알것 인가? 그래서 준비했다. 일추정기!! 재밌다. 처음이라 상당히 어렵게 느껴질 수도 있는데, 이 역시 시간이 지나가서 보면 쉬운 Lab 중 하나라는 생각이 들 것이다. 즐거운 마음으로 시작해보자.

## Day_estimation Overview
이번숙제를 알려면 윤년을 알아야 한다. 윤년이라 것은 2월달이 29일까지 있는 년을 말한다. 윤년의 조건을 알아야하는데 1) 4로 나누어 떨어지는 해는 윤년, 그 밖의 해는 평년으로 한다. 2) 4로 나누어 떨어지지만 100으로 나누어 떨어지는 해는 평년으로 한다. 3) 단, 400으로 나누어 떨어지는 해는 윤년으로 한다. 이런조건을 모두 만족하면 윤년이라고 한다. 윤년이 아닌 해는 2월달이 30일까지 있다. Help function으로 윤년일때와 아닐때의 일수를 리스트로 만들어 놨다. 수강생들은 그에 따라 년도의 윤년유무를 계산하고 그에 따른 리스트를 가지고 숫자를 가지고오면 된다.

본 프로그램은 다음과 같이 세 가지 규칙에 의해 실행된다.

1. 프로그램이 실행되어 사용자가 문자열 형태의 "2014-12"를 입력하는데 "-"를 기준으로 split이 가능해야 하며 모두 문자형 숫자여야 한다. 이밖에는 아무것도 들어올 수 없다.(예외사항을 말함)
2. 년도와 월의 숫자들이 유효하지 않은 숫자라면 "입력한 년도-월은 올바른 값이 아닙니다." 라는 문구를 띄어준다.
3. 모두 유효한 숫자라면 "년도-월:일수"라는 문구를 띄어준다.

로직 자체는 상당히 간단하고, 이미 배운 내용들로 충분히 구현할 수 있다. 하지만, 처음 해보는 리스트 숙제이기 때문에 상당히 어렵게 느껴질 것이다. 이번 Lab은 조금 자세히 설명하니 꼭 문서를 정독하길 바란다.

## 숙제 template 파일 다운로드
먼저 숙제 template 파일을 cs50 서버로부터 다운로드 받는다. 로그인 후 나타나는 `bash shell`에서 다음과 같은 명령을 입력하자.

```bash
python3.4 submit_assignment.py -get day_estimation
```  

입력되면 다운로드 안내 메세지와 함께 `day_estimation.py` 파일이 다운로드 된다.

## day_estimation.py 파일 Overview
`vim editor`로 `day_estimation.py`을 열어 전체적인 개요를 보자. `vi day_estimation.py`명령으로 파일을 열어보면 `main` 함수와 `input_year_month_value`, `check_year`,`check_month` 함수가 존재할 것이다. 본 Lab에서 수정 및 추가해야할 함수는 아래 네 가지이다.

함수           | 설명 
--------       | ---
input_year_month_value| "년도와 월을 입력하시요. ex) 2015-11 : "라는 문구를 띄워주고 값을 받는다. 값은 "년도-월"식으로 이것을 제외하고는 아무것도 받지 않는다.
check_year| 년도부분 문자형 숫자를 받아와 윤년계산법(수강자가 코딩)을 이용해 윤년이라면 is_yun_of_days를 아니라면 isnt_yun_of_days를 반환한다. 만약 0이하라면 False를 반환한다.
check_month| 월 부분 문자형 숫자를 받아와 1이상 12이하인지를 확인하고 사이에있다면 월-1 을 반환한다. 사이에없다면 False를 반환한다.
main| 사용자가 값을 입력받아 위에 조건들을 맞는 값을 화면에 출력하도록 한다.
각 함수별로 작성하는 방법을 살펴보자.

## input_number_check 함수 수정하기
첫 번째 함수는 `input_year_month_value` 함수이다.

숙제 파일을 열어보면 알겠지만 이 함수는 변수가 없다. 그래서 직접 함수에서 값을 입력 받아야한다. 입력받는법은 구글에 물어보면 나보다 설명을 더 잘해준다. ex) 파이썬 사용자 입력
또한 입력받을 때 "년도와 월을 입력하시요. ex) 2015-11 : "라는 문구를 띄워줘야 한다. 구글에 검색해라. ex) 파이썬 사용자 입력 프롬프트
숙제가 아직 초반이기때문에 내가 봐주겠다. 숫자-숫자 형식만 넣으면 된다. 다른 예외사항은 생각하지 않아도 된다. 후반으로 갈수록 이 자비가 얼마나 큰거 였는지 알 수 있다. 
그리고 반환하는 값은 ["숫자","숫자"]식이다. 검색해라 ex) 파이썬 문자열 자르기

## check_year 함수 작성하기
두 번째 함수는 `check_year` 이다. 본 함수는 `year` 라는 문자형 정수값을 입력받아, 윤년일때는 is_yun_of_days를 아닐때는 isnt_yun_of_days를 year가 0보다 작을때는 False를 반환한다.
윤년계산법
1) 4로 나누어 떨어지는 해는 윤년, 그 밖의 해는 평년으로 한다. 
2) 4로 나누어 떨어지지만 100으로 나누어 떨어지는 해는 평년으로 한다. 
3) 단, 400으로 나누어 떨어지는 해는 윤년으로 한다.

## check_month 함수 작성하기
세 번째 함수는 `check_month` 이다. 본 함수는 `month` 라는 문자형 정수값을 입력받아, 1이상 12이하일때는 month-1을, 나머지 경우는 False를 반환한다.

## main 함수 수정하기
마지막 함수는 `main`함수이다. 

참고로 본 Lab에서 설명하는 방법은 많은 구현 방법 중 하나일 뿐이다. 스스로 구현하는 방법이 있다면 그 방법대로 하면 된다. 아래 설명은 구현에 대한 대략적인 설명이다. 
input_number_check함수로 값을 입력받은 다음 0번째 값은 check_year함수의 변수로 들어가 결과값을 받고 1번째 값은 check_month함수의 변수로 들어가 결과값을 받는다. 

check_year, check_month 둘중의 하나만 False라도 "year-month 은 올바른 값이 아닙니다." 라는 문구를 띄워준다.
두 함수가 다 True라면 "year-month: 숫자" 라는 문구를 띄워주는데 리스트의 인덱스는 0부터 시작이기 때문에 1을 빼줘야한다. 하지만 우리는 이미 앞에 함수에서 1을 빼준값을 반환했다.
그렇다면 할 수 있다. 

## 결과 출력하기 
실제 코드가 다 작성되어 `python3.4 day_estimation.py` 아래와 같이 결과를 볼 수 있을 것이다. 당연히 입력 부분은 수강자가 직접 입력을 해주어야 프로그램 진행된다.

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
python3.4 submit_assignment.py -submit day_estimation.py
```  
제대로 작성했다면 아래와 같은 메세지가 뜰 것이다.
```bash
-------------------- | ---------- | --------------------
       Function Name |    Passed? |             Feedback
-------------------- | ---------- | --------------------
 input_year_month_value  |       PASS |             Good Job
 check_year          |       PASS |             Good Job
 check_month         |       PASS |             Good Job
 main                |       PASS |             Good Job
-------------------- | ---------- | --------------------
```  

## Next Work
축하한다. 여러분은 처음으로 메인함수를 작성했다. 여러분은 리스트와 여러가지 함수를 가지고 숙제를 했는데 잊지 않길 바란다. 종강할때까지 나온다. 어렵게 느껴졌을 지도 모르겠지만, 정말 쉬운 숙제였다. 믿어라. 다음 주는 더한 재미를 보게 될 것이다.  

> **Human knowledge belongs to the world** - from movie 'Password' -

## Footnotes


[1]: https://ko.wikipedia.org/wiki/%EA%B3%84%EC%8A%B9
