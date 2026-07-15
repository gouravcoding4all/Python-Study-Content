"""
python Basics operators ,Datatypes
Python Built-in functions
Conditional statements
-if ,else,for,while etc
collections
-List , Tuple, Set,Dictionary

TIC_TAC_TOE GAME

"""
li=[1,2,3,4,5,6,7,8,9,]
wins=[(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
player='X'
flag=0
count=0
while True:
    print("\n\tTic-Tac-Toe")
    print(f"\n\t{li[0]} | {li[1]} | {li[2]}")
    print("\t----------------------")
    print(f"\n\t{li[3]} | {li[4]} | {li[5]}")
    print("\t----------------------")
    print(f"\n\t{li[6]} | {li[7]} | {li[8]}")
    if flag==1:
        break
    if count==9:
        print("\n\t Match Tie")
        break
    ch=int(input(f"\n player {player} Turns: "))
    if ch in li:
        li[ch-1]=player
        count=count+1
        for a,b,c in wins:
            if li[a]==li[b]==li[c]:
                print(f"\t\n\tplayer {player} WIN")
                flag =1
        if player=='X':
            player='0'
        else:
            player='X'
    else:
        print("\n\tno cheating..")

#------------------------------------------------------------------
        #EXPLAINATION:-
"""
Agar Class 3 ke bacche ko samjhana ho, to is code ko aise explain kar sakte ho:

Tic-Tac-Toe Game (Simple Hinglish)
li = [1,2,3,4,5,6,7,8,9]
Ye game ka board hai. Isme 9 boxes hain.
wins = [...]
Isme bataya gaya hai ki kaun se 3 boxes milkar win banate hain (row, column, ya diagonal).
player = 'X'
Pehla player X se game start karta hai.
flag = 0
Ye check karta hai ki koi jeeta ya nahi.
0 = Game chal raha hai.
1 = Game khatam.
count = 0
Kitni moves ho chuki hain, uski counting karta hai.
while True:
Game tab tak chalta rahega jab tak koi jeet na jaye ya match tie na ho.
print()
Board ko screen par dikhata hai.
input()
Player se poochta hai ki 1 se 9 tak kaunsa box choose karna hai.
if ch in li:
Agar box khali hai, to usme X ya O bhar diya jata hai.
for a,b,c in wins:
Har winning combination ko check karta hai.
if li[a]==li[b]==li[c]:
Agar 3 boxes me same symbol (X ya O) hai, to wahi player Winner hai.
player = 'O' / player = 'X'
Har turn ke baad player change ho jata hai.
else: print("No Cheating..")
Agar player pehle se bhare hue box ko select kare, to message aata hai "No Cheating.."
Ek Line Mein

Ye program do players ke liye Tic-Tac-Toe game banata hai, jahan players X aur O se turn-by-turn khelte hain. Jo pehle ek line me 3 same symbols bana deta hai, woh jeet jata hai. Agar 9 moves ke baad bhi koi nahi jeeta, to match tie ho jata hai.
"""













