//
// Created by Andreas on 05-Aug-18.
//

#include <yvals.h>
#include <any>
#include "war.h"
using namespace std;

void WarGame( list<int> cards) {
    //This class simulates the card game war. It takes in a list of 52 cards, splits that list in two and gives each
    //half to each player. If the game lasts longer than 10,000 turns the game stops and the game is assumed to be in
    //an infinite loop.
    list<int> player1 = cards{:26};
    list<int> player2 = cards{26:};
    int counter = 0;
    bool winnable;
    bool endgame = false;


    while (endgame == false) {
        //Check victory conditions

        //As long as players have cards continue playing unless
        //there is a war and somebody has too few cards
        if(len(player1) == 52){
            std:out("('Player 1 won')");
            std:out('Used ', self.counter, 'steps');
            winnable = true;
            endgame = true;
            break;
        }
        if(len(player2) == 52){
            std:out('Player 2 won');
            std:out('Used ', counter, 'steps');
            winnable = true;
            endgame = true;
            break;
        //One card each on the table
        cards = {player1.pop(0), player2.pop(0)};

        //Check who wins

        // P1 won, give cards to them
        if (cards[0] > cards[1]){
            for(card in cards){
                player1.append(card);
            }
        };
        // P2 won, give cards to them
        if (cards[0] < cards[1]) {
            for(card in cards):
                player2.append(card);
            }
        }
        // Same value on cards means war!
        if (cards[0] == cards[1]){
            war();
        }
        // Prevent infinite loop
        if(counter > 10000){
            std:out('reached counter');
            std:out('Used ', counter, 'steps');
            winnable = false;
            endgame = true;
            break;
        // Increase counter
        counter += 1;
        }
    };
    return WarGame;
};


//# War function
//def war(self):
//if len(self.player1) < 4:
//# print('Player1 too few cards for war. Player 2 won.')
//# print('Used ', self.counter, 'steps')
//self.winnable = True
//self.endgame = True
//return
//self.cards += self.player1[:4]
//del self.player1[:4]
//
//if len(self.player2) < 4:
//# print('Player2 too few cards for war. Player 1 won.')
//# print('Used ', self.counter, 'steps')
//self.winnable = True
//self.endgame = True
//return
//
//self.cards += self.player2[:4]
//del self.player2[:4]
//
//# Player 1 won, give all cards to them
//if self.cards[-5] > self.cards[-1]:
//for card in self.cards:
//self.player1.append(card)
//
//# Player 2 won, give all cards to them
//if self.cards[-5] < self.cards[-1]:
//for card in self.cards:
//self.player2.append(card)
//
//# War again!
//if self.cards[-5] == self.cards[-1]:  # WAR!
//self.war()
