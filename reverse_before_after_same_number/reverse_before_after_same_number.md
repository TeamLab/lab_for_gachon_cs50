Working_Lab #5- Reverse before after same number  (Reverse_before_after_same_number)
====================================================================================
Copyright 2016 © document created by TeamLab.Gachon@gmail.com

## Introduction
재밌었지? 이번 건 더 재밌어요~  이번 과제는 숫자들의 중간을 기준으로 반대칭으로 숫자가 같은 숫자들을 만들어 내가 원하는 위치에 있는 숫자들을 반환해주는 함수이다.

- 424,11,1001,125999521 과 같이 가운데를 기준으로 반대칭을 했을때 같은 숫자들을 리스트로 반환
- 숫자는 1이상 n이하로 만드는데 n은 우리가 원하는 값을 맘대로 넣을 수 있다. 단 n은 자연수

어떻게 할지 걱정될 수 도 있지만, 꽤 많은 힌트와 함께 여러분들을 바른 길로 인도해주는 함수를 제시할 것이다. 너무 걱정말고 시작해보자

## Reverse before after same number Overview

- 사용자가 숫자 대신 문자를 입력했을 경우는 생각하지 않는다.
- 사용자가 자연수가 아닌 값을 넣었을 때 에러메세지를 나타내줘야 하는데 이건 main함수에서 해준다.
- 종료조건은 "OUT"을 입력했을 경우인데 밑에서 자세히 설명한다.

또한 우리는 숫자를 생성할때 숫자의 자릿수가 홀수, 짝수 일때를 나눠서 만드는데 밑에와 같다. 

- 숫자를 받아서 숫자의 길이가 짝수인 경우와 홀수인 경우 함수가 따로 있다. 
- 숫자들은 길이가 다르기 때문에 겹칠 수 없다.

## 숙제 template 파일 다운로드
먼저 숙제 template 파일을 cs50 서버로 부터 다운로드 받는다. 로그인 후 나타나는 `bash shell`에서 다음과 같은 명령을 입력하자.

```bash
python3.4 submit_assignment.py -get reverse_before_after_same_number
```  

입력되면 다운로드 안내 메세지와 함께 `reverse_before_after_same_number.py` 파일이 다운로드 된다.

## baseball_game.py 파일 Overview
`vim editor`로 `reverse_before_after_same_number.py`을 열어 전체적인 개요를 보자. `vi reverse_before_after_same_number.py`명령으로 파일을 열어보면 `main` 함수와 여러개의 함수들이 존재할 것이다. 각 함수들은 여러분께서 직접 작성해서 제출해야 하는 함수이고, `main` 함수는 실제 baseball game을 실행하는 함수이다. 각 함수의 구현 내용은 아래와 같다.

함수           | 설명 
--------       | ---  
create_even_number_method    | 자연수 값을 입력받아 1부터 자연수까지 자릿수가 짝수인경우에 뒤집었을 때 똑같은 숫자들을 리스트로 반환해주는 함수
create_odd_number_method  | 자연수 값을 입력받아 1부터 자연수까지 자릿수가 홀수인경우에 뒤집었을 때 똑같은 숫자들을 리스트로 반환해주는 함수 
merge_sort_list_method | 2개의 리스트를 받아 하나의 리스트로 합쳐주고 숫자크기를 오름차순으로 배열해 반환해주는 함수


## main 함수 수정하기 
위의 함수도 상당히 어렵지만 본 Lab의 가장 어려운 숙제는 바로 `main`함수를 수정하는 일이다.
한 가지 유의할 점은 사용자의 입력을 받을 때 `print` 문을 쓴 다음 `input`문을 쓰지 말고 `input` 문만 사용하여 입력을 받아야 한다. 예를 들면 `user_input = input('Input guess number : ')` 형태로 작성되어야 한다. 이 또한 강의자의 개발 능력 한계니 이해해주면 좋겠다.
메인함수에서는 위와 같이 user_input = input("원하는 번째를 입력하세요. : "), number = int(input("원하는 숫자의 크기를 입력하세요. : "))를 통해 변수 2개로 함수를 작성한다. 첫번째 변수는 원하는 위치, 두번째 함수는 위의설명에 있는데 n을 의미한다. 
다만 첫번째 변수에서 0보다 큰 숫자여야한다. 0번째 숫자는 없기 때문이다. 또한 두번째 변수도 0보다 커야 한다. n은 자연수여야하기떄문이다. 만약 둘중하나라도 0보다 작다면 "Wrong input"을 찍어주고 다시실행한다. 또한 생성한 숫자들의 개수가 첫번째 변수보다 작거나 같을 경우 "범위가 존재하지 않습니다."
를 찍어주고 다시 실행한다. 왜냐하면 [1,2,3]의 네번째나 세번째는 없기 때문이다. 세번째가 이해가안된다면 list index부분을 다시공부하자.
각 개별 함수를 목적에 맞게 잘 수정한 후, 개별 함수들을 잘 활용하여 `main` 함수를 작성하기 바란다. 

## 숙제 제출하기
모든 함수를 다 수정했다면, 아래와 같이 제출하자
```bash
 python3.4 submit_assignment.py -submit baseball_game.py
```  
제대로 작성했다면 아래와 같은 메세지가 뜰 것이다.
```python
---------------------------------------- | ------------- | --------------------
             Function Name              |    Passed? |      Feedback
---------------------------------------- | ------------- | --------------------
create_even_number_method  |       PASS   |     Good Job
create_odd_number_method    |       PASS   |     Good Job
merge_sort_list_method            |       PASS   |     Good Job
               main                            |        PASS  |     Good Job
---------------------------------------- | -------------  | --------------------
```  
아마도 정말로 감격 스러운 순간일 것이다. 고생했다. 

## Next Work
이제 여러분은 프로그래밍을 위한 거대한 한발을 내딛었다고 생각한다. 이때까지는 A,B, C를 부르거나 기껏해야 "How are you? Fine thank you, and you" 정도를 읊었다면 이제 프로그래밍으로 쉬운 어린이 "팝송" 한곡 부른 정도라고나 할까? 여러분들은 충분히 잘했다. 오늘 자기전에 맥주한잔을 마시면서 자신이 무한한 가능성이 있는 존재임을 깨닫기 바란다. 여기까지 와줘서 고맙다. 

> **Human knowledge belongs to the world** - from movie 'Password' -

## Footnotes

