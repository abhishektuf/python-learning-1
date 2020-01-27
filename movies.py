import random
movies=['anand','drishyam','golmaal','black friday','vikram veda','taare zameen par','dangal']
def play():
    p1name=input('Player 1, Please enter your name: ')
    p2name=input('Player 2, Please enter your name: ')
    pp1=0
    pp2=0
    turn=0
    willing=True
    while willing:
        if turn%2==0:
            print(p1name,'Your Turn!')
            picked_movie=random.choice(movies)
            qn=create_question(picked)
            print qn

            not_said=True