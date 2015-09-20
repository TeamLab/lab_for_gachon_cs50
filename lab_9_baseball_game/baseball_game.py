# -*- coding: utf-8 -*-

import random

def get_random_number():
    # Helper Function - ������ �� ��
    # 100���� 999���� ���� �����ϰ� ��ȯ��
    return random.randrange(100, 1000)


def is_digit(user_input_number):
    # '''
    # Input:
    #   - user_input_number : ���ڿ� ��
    # Output:
    #   - user_input_number�� ������ ��ȯ ������ ���� True,
    #     �׷��� ���� ���� False
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_digit("551")
    #   True
    #   >>> bg.is_digit("103943")
    #   True
    #   >>> bg.is_digit("472")
    #   True
    #   >>> bg.is_digit("1032.203")
    #   False
    #   >>> bg.is_digit("abc")
    #   False
    # '''
    # ===Modify codes below=============
    # ���ǿ� ���� ��ȯ�Ǿ�� �� ����� result ������ �Ҵ�
    result = None

    # ==================================
    return result



def is_between_100_and_999(user_input_number):
    # '''
    # Input:
    #   - user_input_number : ���ڿ� ��
    #                         �Էµ� ���� ���������� ���ڿ� ������ ����ȴ�.
    # Output:
    #   - user_input_number�� ������ ��ȯ�Ͽ� 100�̻� 1000�̸��� ��� True,
    #     �׷��� ���� ���� False
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_between_100_and_999("551")
    #   True
    #   >>> bg.is_between_100_and_999("103943")
    #   False
    #   >>> bg.is_between_100_and_999("472")
    #   True
    #   >>> bg.is_between_100_and_999("0")
    #   False
    # '''
    # ===Modify codes below=============
    # ���ǿ� ���� ��ȯ�Ǿ�� �� ����� result ������ �Ҵ�
    result = None

    # ==================================
    return result


def is_duplicated_number(three_digit):
    # '''
    # Input:
    #   - three_digit : ���ڿ��� �� ���ڸ� ���� ���� ��
    #                   ���ڿ��� �� ���ڸ� ���� �������� �Է��� ����ȴ�.
    # Output:
    #   - three_digit ������ ��ȯ�Ͽ��� ��� �ߺ��Ǵ� ���� ������ True,
    #     �׷��� ���� ���� False
    #   ex) 117 - False, 123 - True, 103 - True, 113 - False
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_duplicated_number("551")
    #   True
    #   >>> bg.is_duplicated_number("402")
    #   False
    #   >>> bg.is_duplicated_number("472")
    #   False
    #   >>> bg.is_duplicated_number("100")
    #   True
    # '''
    # ===Modify codes below=============
    # ���ǿ� ���� ��ȯ�Ǿ�� �� ����� result ������ �Ҵ�

    result = None
    # ==================================
    return result


def is_validated_number(user_input_number):
    # '''
    # Input:
    #   - user_input_number : ���ڿ� ��
    # Output:
    #   - user_input_number ���� �Ʒ� �����̸� True, �׷��� ������ False�� ��ȯ
    #        1) ������ ���ڿ��̸�, 2) 100�̻� 1000�̸��̸�, 3) �ߺ��Ǵ� ���ڰ� ���� ��� 
    #   ex) 117 - False, 123 - True, 103 - True, 113 - False
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_validated_number("amvd")
    #   False
    #   >>> bg.is_validated_number("402")
    #   True
    #   >>> bg.is_validated_number("472")
    #   True
    #   >>> bg.is_validated_number("100")
    #   False
    #   >>> bg.is_validated_number("1000")
    #   False
    # '''
    # ===Modify codes below=============
    # ���ǿ� ���� ��ȯ�Ǿ�� �� ����� result ������ �Ҵ�

    result = None
    # ==================================
    return result


def get_not_duplicated_three_digit_number():
    # '''
    # Input:
    #   - None : �Է°��� ����
    # Output:
    #   - �ߺ��Ǵ� ���ڰ� ���� 3�ڸ� ������
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   125
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   634
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   583
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   381
    # '''
    # ===Modify codes below=============
    # ���ǿ� ���� ��ȯ�Ǿ�� �� ����� result ������ �Ҵ�

    result = None
    # ==================================
    return result


def get_strikes_or_ball(user_input_number, random_number):
    # '''
    # Input:
    #   - user_input_number : ���ڿ������� ����ڰ� �Է��ϴ� ���ڸ� ����
    #   - random_number : ���ڿ������� ��ǻ�Ͱ� �ڵ����� ������ ����
    # Output:
    #   - [strikes, ball] : ��Ģ�� ���� ������ ���� strikes�� ball�� ��ȯ��
    #   ��ȯ ��Ģ�� �Ʒ��� ����
    #   - ����ڰ� �Է��� ���ڿ� ��ǻ�Ͱ� ������ ������
    #     �� ���ڿ� �ڸ����� ��� ��ġ�ϸ� 1 Strike
    #   - �ڸ����� �ٸ��� �Է��� �� ���ڰ� �����ϸ� 1 Ball
    #   - ���ڸ� ���ڸ� ��Ȯ�� �Է��ϸ� 3 Strike
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.get_strikes_or_ball("123", "472")
    #   [0, 1]
    #   >>> bg.get_strikes_or_ball("547", "472")
    #   [0, 2]
    #   >>> bg.get_strikes_or_ball("247", "472")
    #   [0, 3]
    #   >>> bg.get_strikes_or_ball("742", "472")
    #   [1, 2]
    #   >>> bg.get_strikes_or_ball("472", "472")
    #   [3, 0]
    # '''
    # ===Modify codes below=============
    # ���ǿ� ���� ��ȯ�Ǿ�� �� ����� result ������ �Ҵ�

    result = None
    # ==================================
    return result


def is_yes(one_more_input):
    # '''
    # Input:
    #   - one_more_input : ���ڿ������� ����ڰ� �Է��ϴ� ����
    # Output:
    #   - �Է��� ���� ��ҹ��� ���о��� "Y" �Ǵ� "YES"�� ��� True,
    #     �׷��� ���� ��� False�� ��ȯ��
    # Examples:
    #   >>> import baseball_game as bg
    # >>> bg.is_yes("Y")
    # True
    # >>> bg.is_yes("y")
    # True
    # >>> bg.is_yes("Yes")
    # True
    # >>> bg.is_yes("YES")
    # True
    # >>> bg.is_yes("abc")
    # False
    # >>> bg.is_yes("213")
    # False
    # >>> bg.is_yes("4562")
    # False
    # '''
    # ===Modify codes below=============
    # ���ǿ� ���� ��ȯ�Ǿ�� �� ����� result ������ �Ҵ�

    result = None
    # ==================================
    return result


def is_no(one_more_input):
    # '''
    # Input:
    #   - one_more_input : ���ڿ������� ����ڰ� �Է��ϴ� ����
    # Output:
    #   - �Է��� ���� ��ҹ��� ���о��� "N" �Ǵ� "NO"�� ��� True,
    #     �׷��� ���� ��� False�� ��ȯ��
    # Examples:
    #   >>> import baseball_game as bg
    # >>> bg.is_no("Y")
    # False
    # >>> bg.is_no("b")
    # False
    # >>> bg.is_no("n")
    # True
    # >>> bg.is_no("NO")
    # True
    # >>> bg.is_no("nO")
    # True
    # >>> bg.is_no("1234")
    # False
    # >>> bg.is_no("yes")
    # False
    # '''
    # ===Modify codes below=============
    # ���ǿ� ���� ��ȯ�Ǿ�� �� ����� result ������ �Ҵ�

    result = None
    # ==================================
    return result


def main():
    print("Play Baseball")
    user_input = 999
    random_number = str(get_not_duplicated_three_digit_number())
    print("Random Number is : ", random_number)
    # ===Modify codes below=============
    # ���� �ڵ带 �����Ͽ� �����ο� ������ ������


    # ==================================
    print("Thank you for using this program")
    print("End of the Game")

if __name__ == "__main__":
    main()
