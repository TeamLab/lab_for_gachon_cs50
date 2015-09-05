Lab #1 - .vimrc 세팅하기
=======
Copyright 2015 © document created by TeamLab.Gachon@gmail.com

## Introduction
처음 vim editor를 실행시키면 화면 아래 그림과 같이 밋밋하다. 프로그래밍을 하게 되면 에러 메세지를 찾기위한 "코드 줄 번호", 코드 정리를 위한 "indentation", 예약어 구분을 위한 "색깔 표시" 등 다양한 부가 기능이 필요하다. 이를 위해 첫 번째 Lab Assignment에서는 **CS50 서버 계정에서 개인별로 .vimrc을 설정**하는 것을 실습한다.  

![.vimrc 설정이 안되어 있는 vi editor](https://raw.githubusercontent.com/TeamLab/lab_for_gachon_cs50/master/lab_1_vimrc/vim_without_vimrc.png)


## .vimrc 설정 명령어

vim editor의 설정을 바꾸기 위해서는 사용자의 Home directory <sup id="homedirctory">[1](#f1)</sup>에서 **.vimrc<sup id="vimrc">[2](#f2)</sup> 파일** 생성한 후, 설정을 위한 예약어<sup id="reserved_word">[3](#f3)</sup>를 입력한다. vim 설정을 위한 주요 예약어는 아래와 같다 ([Outsider's Dev Story][1] 발췌후 수정).

예약어                   | 의미 
--------                 | ---
set autoindent           | 자동 들여쓰기
set smartindent          | 스마트한 들여쓰기
set nobackup             | 백업 파일을 안만듬
set ruler                | 화면 우측 하단에 현재 커서의 위치(줄,칸) 표시
set shiftwidth=4         | 자동 들여쓰기 4칸, 4를 조절하여 사용 가능
set number               | 행번호 표시, set nu 도 가능
set fileencoding=utf-8   | 파일저장 인코딩을 utf-8로 변경 
set tenc=utf-8           | 터미널 인코딩을 utf-8로 변경
set expandtab            | 탭대신 스페이스
set hlsearch             | 검색어 강조, set hls 도 가능
set ignorecase           | 검색시 대소문자 무시, set ic 도 가능
set tabstop=4            | 탭을 4칸으로
syntax on                |  구문강조 사용
filetype indent on       |  파일 종류에 따른 구문강조
set history=1000         |  vi 편집기록 기억갯수 .viminfo에 기록

> **Note:** 
> 설정을 위한 예약어는 매우 다양하고 많기 때문에 모든 것을 기억할 필요는 없다. 필요할 때 마다 구글에서 "vimrc 설정", "vimrc 행번호" 등으로 검색을 실시할 것으로 권장한다.  

## .vimrc 생성

.vimrc 파일을 만들기 위해서는 아래와 같이 **"vi ~/.vimrc"**<sup id="mark">[4](#f4)</sup> 명령을 cs50서버에 로그인 후 입력한다. 

```bash
LOGIN_ID@cs50:~$ vi ~/.vimrc
``` 

접속후 처음 설정하는 경우라면 아래와 같이 아무런 내용이 표시되지 않는 검은 화면만 뜰 것이다.

![.vimrc를 처음 설정할 때, .vimrc 파일 내용](https://raw.githubusercontent.com/TeamLab/lab_for_gachon_cs50/master/lab_1_vimrc/first_vimrc.png)

.vimrc 파일에는 아래 code와 같은 내용을 입력한다. 입력을 위해서는 먼저 편집기 화면이 나오면 <kbd>esc</kbd>을 누르고 알파벳 <kbd>i</kbd> 키를 누르면 입력이 된다. 입력중 지우고 싶은 내용이 나오면 다시 <kbd>esc</kbd>을 누르고 방향키를 사용하여 지우고 싶은 내용 위치로 이동하여 <kbd>x</kbd> 버튼을 누르면 된다. 모든 입력이 끝나면 <kbd>esc</kbd>을 누르고 <kbd>:wq</kbd>을 누르고, <kbd>enter</kbd>를 입력하면 저장과 동시에 vim 에디터가 종료된다.

```bash
set autoindent              " 자동 들여쓰기
set smartindent             " 스마트한 들여쓰기
set shiftwidth=4            " 자동 들여쓰기 4칸, 4를 조절하여 사용 가능
set number                  " 행번호 표시, set nu 도 가능
set fileencoding=utf-8      " 파일저장 인코딩을 utf-8로 변경 
set tenc=utf-8              " 터미널 인코딩을 utf-8로 변경
set expandtab               " 탭대신 스페이스
set tabstop=4               " 탭을 4칸으로
syntax on                   " 구문강조 사용
filetype indent on          " 파일 종류에 따른 구문강조
set history=1000            " vi 편집기록 기억갯수 .viminfo에 기록
``` 

## 설정 확인

설정 확인을 위해서 아래와 같은 명령을 입력하여 예제 코드인 "yesterday_test.py"<sup id="py_file">[5](#f5)</sup> 파일을 다운로드 한다. 아래의 명령중 wget은 리눅스에서 파일을 다운로드 받는 명령이고 뒤에 url은 해당 파일의 위치이다. 

```bash
wget https://raw.githubusercontent.com/TeamLab/lab_for_gachon_cs50/master/lab_1_vimrc/yesterday_test.py
``` 

다운로드가 완료되면, 아래 명령으로 해당 파일의 내용을 확인한다.

```bash
vi yesterday_test.py
``` 

![.vimrc를 처음 설정할 때, .vimrc 파일 내용](https://raw.githubusercontent.com/TeamLab/lab_for_gachon_cs50/master/lab_1_vimrc/yesterday_test_vi.png)

위와 같이 코드의 색깔이 다르고, 왼쪽 줄에 숫자가 붙으며, 하단의 파일명과 커서의 위치 등이 제대로 나타난다면 성공적으로 설정 한 것이다. <kbd>esc</kbd> 누른 후 <kbd>:q</kbd>+<kbd>enter</kbd> 를 눌러 vi 에디터를 종료한다.

해당 파이썬 파일을 실행하기 위해서는 아래와 같이 입력한다.

```bash
python3.4 yesterday_test.py
``` 

그 결과는 아래와 같이 출력될 것이다.
```bash
Hello World

        Yesterday, all my troubles seemed so far away
        Now it looks as though they're here to stay
        oh, I believe in yesterday

        Read more: Beatles - Yesterday Lyrics | MetroLyrics
``` 

## Next Work
이상 첫 번째 실습을 완료했다. 본 실습에서는 vi 에디터를 사용하기 위한 설정 파일인 .vimrc 파일을 생성하고 필요한 설정 정보를 추가하였다. 또한 예제 파이썬 파일을 wget 명령으로 다운로드하여 실제로 실행시켜 보았다. 다음 실습에서는 숙제 제출을 위한 **"submit_assignment.py"**을 실습하고 실제 숙제 파일을 제출해 보도록 한다. 

> **Human knowledge belongs to the world** - from movie 'Password' -

## Footnotes
<b id="f1">1</b>: 리눅스 서버에 처음 로그인 했을 때 사용하는 디렉토리. 일반적으로 root 유저가 아닌 경우에는 home directory에서만 작업이 가능하다. 윈도우에서는 "내 문서" 또는 라이브러리가 이에 해당된다.[↩](#homedirctory)

<b id="f2">2</b>: 일반적으로 리눅스에서 rc는 "run commands"를 의미하며, 해당 프로그램의 설정 파일로 활용된다.[↩](#vimrc)

<b id="f3">3</b>: 프로그램을 실행하기 위해 약속된 단어들. 예를 들면, 윈도우 console에서는 dir 이라고 치면 파일 목록이 나타난다.[↩](#reserved_word)

<b id="f4">4</b>: vi는 vi 편집기를 실행시키는 명령어, ~/ 는 사용자의 home direcoty를 의미하며 .vimrc 는 편집할 파일 이름이다. 즉 ~/.vimrc 는 사용자  home direcoty의 .vimrc 파일을 vi 편집기로 편집하도록 vi를 실행하라 라는 의미이다.[↩](#mark)

<b id="f5">5</b>: 파이썬으로 작성된 프로그램 파일은 확장자가 "py" 로 끝난다. [↩](#py_file)


[1]: http://blog.outsider.ne.kr/518