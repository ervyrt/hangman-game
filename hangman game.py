import random 
import time
def draw(mistake):
    if mistake==1:
        print('''
                  ______      
                 |            
                 |            
                 |            
                 |            
                 |            
                 |            
                 |            
                 |          
              ---------''')    
        print("this is your first mistake. There is another 4 chances for you.")
    elif mistake==2:
           print('''
                     ______     
                     |    |     
                     |    |     
                     |    |     
                     |          
                     |          
                     |          
                     |          
                     |          
                     ---------''')
           print("Here comes the second mistake. Be more carefull")
    elif mistake==3:
           print('''
                     ______       
                     |    |       
                     |    |       
                     |    |       
                     |    O       
                     |            
                     |            
                     |            
                     |
                     ---------''')
           print("ohh, here is another mistake!!! I think your frame of mind is not well ")
    elif mistake==4:
           print('''
                     ______      
                     |    |      
                     |    |      
                     |    |      
                     |    O      
                     |    |      
                     |    |      
                     |    |     
                     |          
                     ---------''')
           print("you have another chance.\n use it wisely ")
    elif mistake==5:
           print(''' 
                     ______       
                     |    |       
                     |    |       
                     |    |       
                     |    O       
                     |   /|\      
                     |    |       
                     |    |       
                     |   / \    
                     ---------''')
           print("The game is ended")
           print("the word was:",word1)
           again()
with open("C:/Users/yurtb/OneDrive/Desktop/hangman/4000.csv","r",encoding = 'utf-8') as file:
    x=file.readlines()
print("welcome to hangman game")
name=input("please enter your name:")
print("the game will start in short time {}.".format(name))
time.sleep(1)
def ready():
    global word1
    global word 
    global display 
    global mistake 
    global length
    global last_guesses
    a=random.randint(0,1000)
    word=x[a]
    word=word.rstrip('\n')
    word1=word
    mistake=0
    length=int(len(word))
    display="_"*length
    last_guesses=[]
def play():
    ready()
    global word 
    global display 
    global mistake 
    global last_guesses
    while mistake<5 :
        if word =="_"*length:
            print("Congrats! You have guessed the word correctly!")
            again() 
        print("last guesses:",last_guesses)
        time.sleep(1)
        print(display)
        time.sleep(1)
        letter=input("please make a guess:")
        
        if len(letter)==0 or len(letter)>1 :
            print( "please write a valid guess.")
        elif letter in last_guesses:
                print("Ohh you have already maden this guess,please make another guess")
        elif letter in word: 
                last_guesses.append(letter)
                while letter in word:
                    index=word.find(letter)
                    word=word[:index]+"_"+word[index+1:]
                    display=display[:index]+letter+display[index+1:]
                   
        else:
            last_guesses.append(letter)
            mistake+=1
            time.sleep(1)
            draw(mistake)
              

def again():
    answer=input("If you want to play again place press 'a' if you do not press 'n'")
    if answer=="a":
        play()
    if answer=="n":
        exit()

play()