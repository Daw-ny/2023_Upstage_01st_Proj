# crawling module
import requests
import json

# preprocessing module
import pickle
import random
import hgtk


# 두음법칙 적용
def dooeum_daneo(wword):
    doeum = hgtk.letter.decompose(wword)
    if doeum[0] == 'ㄹ' and doeum[1] in ['ㅣ', 'ㅑ', 'ㅕ', 'ㅛ', 'ㅠ', 'ㅒ', 'ㅖ']:
        startwords = [wword,
                    hgtk.letter.compose('ㄴ', doeum[1], doeum[2]),
                    hgtk.letter.compose('ㅇ', doeum[1], doeum[2])
        ]        
    
    elif doeum[0] == 'ㄹ':
        startwords = [wword,
                    hgtk.letter.compose('ㄴ', doeum[1], doeum[2])
        ]
    
    elif doeum[0] == 'ㄴ' and doeum[1] in ['ㅣ', 'ㅑ', 'ㅕ', 'ㅛ', 'ㅠ', 'ㅒ', 'ㅖ']:
        startwords = [wword,
                    hgtk.letter.compose('ㅇ', doeum[1], doeum[2])
        ]

    else:
        startwords = [wword]

    return startwords


# 단어 찾기 크롤링
def find_word(word, endword, duplicate_word_list):
    url = 'https://stdict.korean.go.kr/api/search.do'	
    word_set = set()

    # 두음법칙 단어 검사
    endwords = dooeum_daneo(endword)

    for j in endwords:    
        for i in range(1, 1001):
            params = {
                'key' : '5DFBEAF77F9965204623D6F5106C6336',
                'q' : j,
                'req_type' : 'json',
                'start' : i,
                'num' : 100,
                'advanced' : 'y',
                'method' : 'start',
                'type1' : 'word',
                'pos' : 1
            }

            res = requests.get(url, params = params)
            try:
                if res.status_code == 200:
                    data = json.loads(res.text)
                    items = data['channel']['item']

                    for item in items:
                        if len(item['word']) == 1:
                            continue

                        if item['word'] not in word_set:
                            word_set.add(item['word'].replace('-', ''))
                        
            except:
                break
    
    if word_set:
        crawling_word[endword] = list(word_set)

    if not word_set and word not in one_word:
        one_word[word] = 1
        return ""
    
    else:
        n = 1000
        while n > 0:
            comword = random.choice(list(word_set))
            if comword not in duplicate_word_list:
                break
            n -= 1
        else:
            comword = ""

        for i in word_set:
            if i not in word_hash:
                word_hash[i] = 1

        return comword


# 단어 검사
def validate_word(word, botword, duplicate_word_list, one_turn_word, turn):
    # 두음법칙 단어 검사
    startwords = dooeum_daneo(botword[-1])
    
    if turn > 1 and word[0] not in startwords:
        print("◎ 끝말 bot : 앞글자가 안맞습니다.")
        return -1
    
    if word in duplicate_word_list:
        print("◎ 끝말 bot : 이미 입력된 단어입니다.")
        return -1
    
    if turn == 1 and word in one_turn_word:
        print("◎ 끝말 bot : 첫턴 한방 안됩니다.")
        return -1
    
    elif turn > 1 and word in one_turn_word:
        return 1
    
    elif word in word_hash:
        return 0
    
    else:
        url = 'https://stdict.korean.go.kr/api/search.do'

        for i in startwords:
            daneo = i + word[1:]
            params = {
                'key' : '5DFBEAF77F9965204623D6F5106C6336',
                'q' : daneo,
                'req_type' : 'json',
                'start' : 1,
                'num' : 100,
                'advanced' : 'y',
                'type1' : 'word',
                'pos' : 1
            }

            res = requests.get(url, params = params)
            try:
                if res.status_code == 200:
                    data = json.loads(res.text)
                    if data:
                        return 0

            except:
                continue
        
        print("◎ 끝말 bot : 없는 단어입니다.")
        return -1


def play_word_relay():
    print("◎ 끝말 bot : 끝말잇기를 시작합니다.")
    print("◎ 끝말 bot : 시작하고자 하는 단어를 입력해주세요.")
    chance = 3
    result = "Lose"
    used_word_list = []
    turn = 1
    botword = "꿹루껠"

    while chance > 0:
        print(f"→ {turn}번째 차례 기회 {chance}번")
        word = input("→ 입력 단어 : ")

        # 단어검증 1. 단어의 길이가 2글자 이상인가?
        if len(word) < 2:
            print("◎ 끝말 bot : 단어는 2글자 이상이어야 합니다.")
            chance -= 1
            continue
        
        # 단어검증 해주는 함수
        num = validate_word(word, botword, used_word_list, one_word, turn)

        # 통과 했으니 중복되지 않게 대입
        used_word_list.append(word)

        if num == 0:
            endword = word[-1]
            if endword in crawling_word:
                cw = crawling_word[endword]
                botword = random.choice(cw)

            else:
                botword = find_word(word, endword, used_word_list)

            if botword == "":
                result = "Win"
                break
            print("◎ 끝말 bot : ", botword)
            used_word_list.append(botword)
            chance = 3
            turn += 1
        
        elif num == 1:
            print("◎ 끝말 bot : 입력할 수 있는 단어가 없습니다.")
            chance = -3
            result = "Win"

        else:
            print("◎ 끝말 bot : 규칙에 맞는 단어를 입력해주세요.")
            chance -= 1

    return result


def replay():
    print("◎ 끝말 bot : 다시 시작하시겠습니까?")
    print("◎ 끝말 bot : 다시 하려면 Y 또는 y를 입력해주세요.")


if __name__ == "__main__":
    print('''
=============파이썬 끝말잇기===============
사전 데이터 제공: 국립국어원 표준국어대사전

- - - 게임 방법 - - -
가장 처음 단어를 제시하면 끝말잇기가 시작됩니다

- - - 게임 규칙 - - -
01. 사전에 등재된 명사여야 합니다
02. 적어도 단어의 길이가 두 글자 이상이어야 합니다
03. 이미 사용한 단어를 다시 사용할 수 없습니다
04. 두음법칙 적용 가능합니다 (ex. 리-> 니)
05. 첫턴 한방단어는 불가능합니다.
06. 게임당 경고 3회시 패배입니다.
07. Y/y를 입력하면 끝말잇기가 시작되며 N/n을 입력하면 끝말잇기가 종료됩니다.
08. 첫 턴에 단어를 인식하지 못할 수 있습니다.
09. 입력한 이후 오래걸리는 경우가 있습니다. 이 경우 크롤링을 하느라 시간이 걸리므로 잠시 기다리시면 정상작동 됩니다.
10. 오류 발생시 잠시 기다렸다가 다시 실행하시면 됩니다.
==========================================\n
''')
    print("◎ 끝말 bot : 끝말잇기를 시작하겠습니까?")
    count = 0
    while count < 4:
        answer = input("→ 내 대답 : ")
        if answer == "Y" or answer == "y":
            # load data
            with open('.\personal_project\word.pickle', 'rb') as fr:
                word_hash = pickle.load(fr)

            with open('.\personal_project\oneturn.pickle', 'rb') as fr:
                one_word = pickle.load(fr)

            with open('.\personal_project\crawling_word.pickle', 'rb') as fr:
                crawling_word = pickle.load(fr)

            res = play_word_relay()
            if res == "Lose":
                print("◎ 끝말 bot : 저의 승리입니다.\n")
            
            else:
                print("◎ 끝말 bot : 당신의 승리입니다.\n")
            
            # save data
            with open('.\personal_project\word.pickle','wb') as fw:
                pickle.dump(word_hash, fw)

            with open('.\personal_project\oneturn.pickle','wb') as fw:
                pickle.dump(one_word, fw)
            
            with open('.\personal_project\crawling_word.pickle','wb') as fw:
                pickle.dump(crawling_word, fw)

            replay()
            count = 0 

        elif answer == "N" or answer == "n":
            print("◎ 끝말 bot : 끝말잇기를 종료합니다.")
            break

        else:
            count += 1
            if count < 4:
                print("◎ 끝말 bot : 안내문을 읽고 다시 시도해 주세요.\n")
            

    if count == 4:
        print("◎ 끝말 bot : 나가실게요.")

    else:
        print("◎ 끝말 bot : 이용해주셔서 감사합니다.")