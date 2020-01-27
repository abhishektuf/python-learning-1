import random

def select_movie():
   movies = ['anand', 'golmaal', 'matrix', 'avenger', 'ring', 'superman', '1920', 'batman', 'alice the wonder land', 'gravity', 'inception']
   picked_movie = random.choice(movies)
   picked_movie = picked_movie.lower()
   return picked_movie        
def create_question(qn):
   secret = []
   for i in range (len(qn)):
	   if qn[i] == " ":
		   secret.append(qn[i])
	   else:
		   secret.append("@")
   i = i+1
   return secret          
def m_unlock(qn, movie, alp):
   movie = movie.lower()
   movie = list(movie)
   qn = list(qn)
   temp = []
   for i in range (len(movie)):
	   if (movie[i] == " " or movie[i] == alp):
		   temp.append(movie[i])
	   else:
		   if qn[i] == "@":
			   temp.append(qn[i])
		   else:
			   temp.append(qn[i])
   un_qn = "".join(str(x) for x in temp)
   return un_qn         
def play():
   p1name = input('Player 1 please share your name \n')
   p2name = input('Player 2 please share your name \n')   
   p1total = 0
   p2total = 0
   willing = True
   while willing:
	   p1point = 14
	   p2point = 14
	   picked_movie = select_movie()
	   win = True
	   qn = create_question(picked_movie)
	   mlenght = len(qn)
	   turn = int(random.randint(0,1))
	   print ('\n\nThere are ',mlenght,' alphabets in movie name \n')
	   for item in qn: print(item, end=" ")
	   while win:
		   if (p1point <= 0 and p2point <= 0):
			   print("Chances of both players are vanished")
			   print("Movie name was: ", picked_movie)
			   win = False
		   else:                                                                          
			   p1try = 2
			   p2try = 2                                                                                                                                                   
			   if turn == 0 and p1point <= 0:
				   print(p1name, 'Your all chances are exhaused')
				   turn = 1                   
			   elif turn == 0 and p1point > 0:                    
				   print("\n\n",p1name, ": Its your turn now !!!!!")               
				   playerchoice = input('Say "yes" if wanna guess the movie name otherwise say "no"\n \n')
				   playerchoice = playerchoice.lower()
				   if ( playerchoice == "yes" ):
					   guess = input("Enter the movie name \n")
					   guess = guess.lower()
					   if guess == picked_movie:
						   print("Hurray!!  Your guess is right.. \n\n")
						   p1point = p1point - p1try
						   p1total = p1total + p1point
						   turn == 1      
						   win = False
					   else:
						   print('\a\n\nOOopppsss...Wrong guess \n\n')
						   turn = 1
						   p1try = p1try +2
						   p1point = p1point - p1try                            
				   elif playerchoice == "no" :
					   alphabet = input('Provide the alphabet to reveal \n\n')
					   alphabet = alphabet.lower()
					   a_count = picked_movie.count(alphabet)
					   if a_count == 0:
						   print('\a\noohhhh!! Alphabet "', alphabet.upper(),'" not present in movie name.')
						   turn = 1
						   p1try = p1try +2
						   p1point = p1point - p1try                    
					   else:
						   qn = m_unlock(qn, picked_movie, alphabet)                            
						   print(" ".join(str(x) for x in qn.upper())) 
						   p1try = p1try +2
						   p1point = p1point - p1try
						   turn = 0
				   else:
					   print('\n\nPlease provide valid input \n \a')
			   if turn == 1 and p2point <= 0:
				   print("\n\n",p1name, 'Your all chances are exhaused')
				   turn = 0
			   elif turn == 1 and p2point > 0:
				   print("\n", p2name, ": Its your turn !!!!!")
				   playerchoice = input(' Say "Yes" if wanna guess the movie name otherwise say "No"\n \n ')
				   playerchoice = playerchoice.lower()
				   if ( playerchoice == "yes" ):
					   guess = input("Enter the movie name \n")
					   guess = guess.lower()
					   if guess == picked_movie:
						   print("Hurray!!  Your guess is right.. \n")
						   p2point = p2point - p2try
						   p2total = p2total + p2point
						   turn == 0       
						   win = False
					   else:
						   print('\a OOopppsss...Wrong guess \n')
						   turn = 0
						   p2try = p2try +2
						   p2point = p2point - p2try                                                           
				   elif playerchoice == "no" :
					   alphabet = input('Provide the alphabet to reveal \n')
					   alphabet = alphabet.lower()
					   a_count = picked_movie.count(alphabet)
					   if a_count == 0:
						   print('\a oohhhh!! Alphabet "',alphabet.upper(),'" not present in movie name.')
						   turn = 0
						   p2try = p2try +2
						   p2point = p2point - p2try                                               
					   else:
						   qn = m_unlock(qn, picked_movie, alphabet)
						   print(" ".join(str(x) for x in qn.upper())) 
						   p2try = p2try +2
						   p2point = p2point - p2try                           
				   else:
					   print('\nPlease enter valid input \a')   
	   decision= input("Do you like contunue playing? Say 'Yes' to prcceed or 'No' to exit \n\n")
	   decision= decision.lower()
	   if ( decision == "no" ):            
		   print(p1name, "Score is : ", p1total)
		   print(p2name, "Score is : ", p2total)
		   print("Movie name was: ", picked_movie.upper())
		   willing = False
		   win = False
		   print("Game Over !")
	   elif ( decision == "yes" ):
		   continue
	   else:
		   print("Enter valid input")
n=create_question("abhay kumar")
print(len(n))
