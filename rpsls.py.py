#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�
���ڣ�
"""
import random
def name_to_number(name): 
    if name=='ʯͷ':
        player_choice_number=0
        return player_choice_number
    elif name=='ʷ����':
        player_choice_number=1
        return player_choice_number
    elif name=='ֽ':
        player_choice_number=2
        return player_choice_number
    elif name=='����':
        player_choice_number=3
        return player_choice_number
    else:
        player_choice_number=4
        return player_choice_number
def number_to_name(number):
    if number==0:
        number='ʯͷ'
        return number
    elif number==1:
        number='ʷ����'
        return number
    elif number==2:
        number='ֽ'
        return number
    elif number==3:
        number='����'
        return number
    else:
        number='����'
        return number
def rpsls(player_choice):
    player_choice_number=name_to_number(player_choice)
    comp_number=random.randint(0,4)
    jisuanji=number_to_name(comp_number)
    print('�������ѡ����%s'%(jisuanji))
    if comp_number==player_choice_number:
        print('���ͼ��������һ���أ�')
    elif player_choice_number==0:
        if comp_number==3 or comp_number==4:
            print('��Ӯ��')
        else:
            print('������')
    elif player_choice_number==1:
        if comp_number==0 or comp_number==4:
            print('��Ӯ��')
        else:
            print('������')
    elif player_choice_number==2:
        if comp_number==0 or comp_number==1:
            print('��Ӯ��')
        else:
            print('������')
    elif player_choice_number==3:
        if comp_number==1 or comp_number2:
            print('��Ӯ��')
        else:
            print('������')
    else:
        if comp_number==2 or comp_number==3:
            print('��Ӯ��')
        else:
            print('������')
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
player_choice=input()
rpsls(player_choice)