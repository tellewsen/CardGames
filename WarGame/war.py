class WarGame:
    # This class simulates the card game war. It takes in a list of 52 cards, splits that list in two and gives each
    # half to each player. If the game lasts longer than 10,000 turns the game stops and the game is assumed to be in
    # an infinite loop.

    def __init__(self, seed):
        self.player1 = []
        self.player2 = []
        self.cards = seed
        self.counter = 0
        self.winnable = bool
        self.endgame = False
        self.give_cards()
        self.play_game()

    def __str__(self):
        self.name = 'WarGame'
        return self.name

    # Give the cards to the players
    def give_cards(self):
        self.player1 = self.cards[:26]
        self.player2 = self.cards[26:]

    # Simulate the game
    def play_game(self):
        # As long as players have cards continue playing unless
        # there is a war and somebody has too few cards

        while self.endgame is False:
            # Check victory conditions
            if len(self.player1) == 52:
                # print('Player 1 won')
                # print('Used ', self.counter, 'steps')
                self.winnable = True
                self.endgame = True
                break

            if len(self.player2) == 52:
                # print('Player 2 won')
                # print('Used ', self.counter, 'steps')
                self.winnable = True
                self.endgame = True
                break

            # One card each on the table
            self.cards = [self.player1.pop(0), self.player2.pop(0)]

            # Check who wins
            if self.cards[0] > self.cards[1]:  # P1 won, give cards to them
                for card in self.cards:
                    self.player1.append(card)
            if self.cards[0] < self.cards[1]:  # P2 won, give cards to them
                for card in self.cards:
                    self.player2.append(card)

            # Same value on cards means war!
            if self.cards[0] == self.cards[1]:
                self.war()

            # Prevent infinite loop
            if self.counter > 10000:
                # print('reached counter')
                # print('Used ', self.counter, 'steps')
                self.winnable = False
                self.endgame = True
                break

            # Increase counter
            self.counter += 1

    # War function
    def war(self):
        if len(self.player1) < 4:
            # print('Player1 too few cards for war. Player 2 won.')
            # print('Used ', self.counter, 'steps')
            self.winnable = True
            self.endgame = True
            return
        self.cards += self.player1[:4]
        del self.player1[:4]

        if len(self.player2) < 4:
            # print('Player2 too few cards for war. Player 1 won.')
            # print('Used ', self.counter, 'steps')
            self.winnable = True
            self.endgame = True
            return

        self.cards += self.player2[:4]
        del self.player2[:4]

        # Player 1 won, give all cards to them
        if self.cards[-5] > self.cards[-1]:
            for card in self.cards:
                self.player1.append(card)

        # Player 2 won, give all cards to them
        if self.cards[-5] < self.cards[-1]:
            for card in self.cards:
                self.player2.append(card)

        # War again!
        if self.cards[-5] == self.cards[-1]:  # WAR!
            self.war()
