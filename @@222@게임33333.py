# 1. 게임 설명
 
print('안녕하세요 @@게임 입니다')
print('게임을 시작하려면 시작 금액을 설정해주세요')
print('이 게임은 총 3가지의 라운드로 구성되어 있습니다')
print('게임 최종 성공시 시작 금액의 5배를 받을 수 있습니다')
print('매 라운드마다 실패시 게임에서 탈락됩니다')
print('그럼 지금부터 게임을 시작하겠습니다')
print()

money = int(input('시작 금액(만 단위)을 입력해주세요>>'))
print('게임을 시작합니다')
print()

# 2. 게임 시작
import random
print('동전을 던집니다!')
coin = ['앞', '뒤']
luckynum = random.choice(coin)
user = input('동전의 앞뒤를 맞춰주세요>>')

if user == luckynum:
    print('정답입니다! 2라운드로 넘어갑니다')
    print()

    import random
    goal = ['왼쪽', '중앙', '오른쪽']
    luckynum = random.choice(goal)
    user = input('골을 어느 방향(왼쪽, 오른쪽, 중앙)으로 넣으시나요?>>')
    if user != luckynum:
        print('골을 넣으셨습니다! 3라운드로 넘어갑니다')
        print()

        import random
        
        BRnum = 0
        user = 0
        luckynum = 0

        while True:
            print('1~3 사이의 숫자를 입력하세요>>')
            user = int(input())
            BRnum += user
            if BRnum >= 31:
                print('실패하셨습니다! 게임 탈락입니다')
                break
            print('총합', BRnum)
            luckynum = random.randint(1,3)
            print('컴퓨터 숫자',luckynum)
            BRnum += luckynum
            if BRnum >= 31:
                 print('게임에 성공하셨습니다')
                 print('최종금액', money*5, '만원 입니다')
                 break
            print('총합', BRnum)
            print()
      

    else:
        print('2단계에서 실패하셨습니다! 게임 탈락입니다')
      
else:
     print('1단계에서 실패하셨습니다! 게임 탈락입니다')
     
    
