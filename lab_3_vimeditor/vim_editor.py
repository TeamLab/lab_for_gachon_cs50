#-*- coding: utf-8 -*-

# ============ 절대 수정하지 말 것 =============
example_1 = "Gachon University. CS50 Class"
example_2 = "ACE!! We Are Ace"
example_3 = """
Yesterday, all my troubles seemed so far away
Now it looks as though they're here to stay
oh, I believe in yesterday

Suddenly, I'm not half the man I used to be
There's a shadow hanging over me
Oh, yesterday came suddenly.
"""
# ============================================== 

# 단어 지우기 연습하기
def delete_word():

    # Input:
    #   - None
    # Output:
    #   - 수정된 example_1 string
    # Examples:
    #   >>> import vim_editor as ve    
    #   >>> ve.delete_word()
    #   Gachon University. Class
    # ===Modify codes below=============


    # ==================================

    return example_1

# 단어 바꾸기
def change_word():
    # Input:
    #   - None
    # Output:
    #   - 수정된 example_2 string
    # Examples:
    #   >>> import vim_editor as ve    
    #   >>> ve.change_word()
    #   Gachon!! We Are Gachon
    # ===Modify codes below=============

    # ==================================

    return example_2

# 다섯줄 지우기
def delete_five_lines():
    # Input:
    #   - None
    # Output:
    #   - 수정된 example_3 string
    # Examples:
    #   >>> import vim_editor as ve    
    #   >>> ve.delete_five_lines()
    #   Oh, yesterday came suddenly.
    # ===Modify codes below=============

    # ==================================

    return example_3

# Yesterday => Today로 바꾸기
def change_word_2():
    # Input:
    #   - None
    # Output:
    #   - 수정된 example_3 string
    # Examples:
    #   >>> import vim_editor as ve    
    #   >>> ve.change_word_2()
    #   
    #   Today, all my troubles seemed so far away
    #   Now it looks as though they're here to stay
    #   oh, I believe in Today
    #
    #   Suddenly, I'm not half the man I used to be
    #   There's a shadow hanging over me
    #   Oh, Today came suddenly.
    # ===Modify codes below=============

    # ==================================
    return example_3

# Check Method
def check_initial_values():
    return [example_1, example_2, example_3]

def main():
    print (delete_word()) # Expected result: Gachon University. Class
    print (delete_word()== "Gachon University. Class") # Expected result: True

    print (change_word()) # Gachon!! We Are Gachon
    print (change_word()== "Gachon!! We Are Gachon") # Expected result: True

    print (delete_five_lines()) # Oh, yesterday came suddenly.
    print (delete_five_lines()=="Oh, yesterday came suddenly.") # Expected result: True

    print (check_initial_values())
    # ['Gachon University. CS50 Class', 'ACE!! We Are Ace', "\nYesterday, all my troubles seemed so far away\nNow it looks as though they're here to stay\noh, I believe in yesterday\n\nSuddenly, I'm not half the man I used to be\nThere's a shadow hanging over me\nOh, yesterday came suddenly.\n"]


if __name__ == "__main__":
    main()