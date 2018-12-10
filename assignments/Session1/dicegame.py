from enum import Enum
import random

class Joueurs(Enum):
    PLAYER = 'player'
    COMPUTER = 'computer'

def testFin(scores):
    if scores[Joueurs.PLAYER] >= 100 or scores[Joueurs.COMPUTER] >= 100:
        return True
    else:
        return False


def switch_the_player(actualPlayer):
    
    if (actualPlayer == Joueurs.PLAYER):
        actualPlayer = Joueurs.COMPUTER
        
    else:
        actualPlayer = Joueurs.PLAYER

    return actualPlayer


def launchDice():
    finish = False
    current_score = 0

    while not finish:
        number = random.choice([1,2,3,4,5,6 ])
        print('Le resultat est  : ' + str(number))
        
        if number != 1:
            current_score += number
            
        else:
            print('C est finis')
            finish = True
            current_score = 0
           

    return current_score



def jouer():
    
    actualPlayer = Joueurs.COMPUTER
    
    results = {
        Joueurs.PLAYER: 0, 
        Joueurs.COMPUTER: 0
    }
    
    while not testFin(results):
        scorePlayer = str(results[Joueurs.PLAYER])
        scoreComputer = str(results[Joueurs.COMPUTER])
        print('Joueur:'+scorePlayer)
        print('Ordinateur:'+scoreComputer)

        if actualPlayer == Joueurs.PLAYER:
            results[Joueurs.PLAYER] += launchDice()
            
        else:
            results[Joueurs.COMPUTER] += random.randint(1, 6)

        actualPlayer = switch_the_player(actualPlayer)


    finalResult = ""
    
    if testFin(results) and results[Joueurs.PLAYER] >= 100:
        print('victoire')
        
    else:
        print('Defait')

    print(finalResult)

jouer()