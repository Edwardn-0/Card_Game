# 덱 빌딩 카드게임, 각 카드들의 조합으로 가장 큰 데미지 만들기// 기술 카드, 데미지 곱셈 카드, 특별한 카드(변수)
import random as rd

Skill_card = [10,20,30,50,80,100]
Mix_card = [0.1, 0.3, 0.5, 2, 5, 10]
Special_card = []

scoreboard = {}
i = 0

play = True

def PlayCard(type):
    global num
    num = rd.randint(0, len(type)-1)
    choose_card = type[num]
    print(f'당신의 카드:  {choose_card}')

def Draw():
    global Chosen_Skill, Chosen_Mix
    print('-------------------------------')
    PlayCard(Skill_card)
    Chosen_Skill = num
    PlayCard(Mix_card)
    Chosen_Mix = num

while play:
    Draw()

    user = input('행동(드로, 리롤, 종료): ')

    if user == '드로':
        i += 1
        score = int(Skill_card[Chosen_Skill])*float(Mix_card[Chosen_Mix])
        print('점수: ', score)
        scoreboard[f'{i}번째 실행'] = score
    elif user == '리롤':
        continue
    elif user == '종료':
        play = False
    else:
        print('********다시 입력해주세요**********')

print('---------------------------------')
print(scoreboard)