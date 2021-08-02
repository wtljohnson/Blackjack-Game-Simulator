import random


class Card:
    def __init__(self, value, face_value=None):
        self.value = value
        if face_value is None:
            self.face_value = str(self.value)
        else:
            self.face_value = face_value
        self.true_value = value

    def __repr__(self):
        return f"{self.face_value}:{self.value}" if self.value is None else f"{self.face_value}"

    def set_value(self, value):
        self.value = value


class Hand:
    def __init__(self, cards, doubled=False, split=False, busted=False, bet=0):
        self.cards = cards
        self.value = 0
        self.any_aces = False
        self.doubled = doubled
        self.split = split
        self.busted = busted
        self.bet = bet

    def __repr__(self):
        return f"{self.cards}"

    def __getitem__(self, key):
        return self.cards[key]

    def hide_hole_card(self):
        return f"[{self.cards[0]}, X]"

    def get_value(self):
        self.value = 0
        if self.cards == []:
            return 0
        for card in self.cards:
            if self.any_aces is False and card.value == 11:
                self.any_aces = True
            self.value += card.value
        if self.value > 21 and self.any_aces:
            hand_copy = self.copy()
            found = False
            for card in hand_copy.cards:
                if card.value == 11 and found is False:
                    card.set_value(1)
                    found = True
            self.value = hand_copy.get_value()
        return self.value

    def get_low_value(self):
        value = 0
        hand_copy = self.copy()
        for card in hand_copy.cards:
            if card.value == 11:
                card.set_value(1)
            value += card.value
        return value

    def set_doubled(self):
        self.doubled = True

    def set_split(self):
        self.split = True

    def set_busted(self):
        self.busted = True

    def set_bet(self, value):
        self.bet = value

    def add_card(self, card):
        if isinstance(card, Card):
            self.cards.append(card)

    def copy(self):
        new_cards = []
        for card in self.cards:
            new_cards.append(Card(card.value))
        return Hand(new_cards)


class Shoe:
    def __init__(self, std_deck, decks, deck_pene):
        self.std_deck = std_deck
        self.shoe = []
        self.deck_pene = deck_pene
        self.generate_shoe(decks)

    def __repr__(self):
        return f"{self.shoe}"

    def copy_std_deck(self):
        return self.std_deck[:]

    def generate_shoe(self, decks):
        self.shoe = self.copy_std_deck() * decks
        random.shuffle(self.shoe)
        if self.deck_pene < 1:
            insert_pos = round(len(self.shoe) * self.deck_pene)
            self.shoe.insert(insert_pos, Card(None, "C"))
            self.shoe.insert(len(self.shoe), Card(None, "S"))
        else:
            self.shoe.insert(len(self.shoe), Card(None, "S"))

    def deal(self, shuffle):
        next_card = self.shoe.pop(0)
        if next_card.face_value == "C":
            next_card = self.shoe.pop(0)
            return next_card, True
        elif next_card.face_value == "S":
            return "S", False
        else:
            return next_card, True if shuffle else False


class Game:
    def __init__(self, rules, std_deck, bankroll, strategy):
        self.rules = rules
        self.std_deck = std_deck
        self.reset_hands()
        self.shoe = Shoe(std_deck, rules["decks"], rules["pene"])
        self.bankroll = bankroll
        self.strategy = strategy
        self.bet = 0

    def __repr__(self):
        return f"Player hand: {self.player_hands[hand] for hand in self.player_hands}, Dealer hand: {self.dealer_hand}"

    def reset_hands(self):
        self.player_hands = [Hand([])]
        self.dealer_hand = Hand([])

    def next_card(self, shuffle):
        next_card, shuffle = self.shoe.deal(shuffle)
        if next_card == "S":
            print("No more cards, reshuffling...")
            if self.strategy:
                self.strategy.running_count = 4 - (4 * self.rules["decks"])
            self.shoe = Shoe(self.std_deck, self.rules["decks"], self.rules["pene"])
            next_card, shuffle = self.shoe.deal(shuffle)
        return next_card, shuffle

    def check_soft(self, hand):
        if not hand.any_aces:
            return False

        if hand.get_low_value() != hand.get_value():
            return True
        return False

    def dealer_plays(self, shuffle):
        print(f"Dealers hole card is {self.dealer_hand[1]}!")
        print(f"Dealer hand: {self.dealer_hand}")
        print(self.dealer_hand.get_value())

        while self.dealer_hand.get_value() <= 17:
            hand_value = self.dealer_hand.get_value()
            if hand_value == 17:
                if not self.check_soft(self.dealer_hand):
                    print("Dealer stands!")
                    return hand_value, shuffle
                if self.rules["s17"]:
                    print("Dealer stands!")
                    return hand_value, shuffle
            card, shuffle = self.next_card(shuffle)
            self.dealer_hand.add_card(card)
            if self.strategy:
                self.strategy.update_running_count(card)
            print("")
            print(f"Dealer draws {card.value}!")
            print(f"Dealer hand: {self.dealer_hand}")
            print(self.dealer_hand.get_value())

        if self.dealer_hand.get_value() > 21:
            print("Dealer busts!")
            return 0, shuffle
        print("Dealer stands!")
        return (self.dealer_hand.get_value(), shuffle)

    def get_decisions(self, hand, shuffle):
        if hand.doubled is True:
            return []

        decisions = ["Hit", "Stand"]
        if len(hand.cards) == 2:
            if hand[0].value == hand[1].value and len(self.player_hands) - 1 < self.rules["resplit"]:
                if hand[0].value == 11:
                    if hand.split:
                        if self.rules["resplit_aces"]:
                            if self.bankroll - self.bet > 0:
                                decisions.append("Split")
                    else:
                        if self.bankroll - self.bet > 0:
                            decisions.append("Split")
                else:
                    decisions.append("Split")
            if hand.get_value() in self.rules["can_double"]:
                if hand.split:
                    if self.rules["das"]:
                        if self.bankroll - self.bet > 0:
                            decisions.append("Double")
                else:
                    if self.bankroll - self.bet > 0:
                        decisions.append("Double")
            if self.rules["late_surr"]:
                decisions.append("Surrender")
        elif len(hand.cards) == 1:
            if hand[0].value == 11:
                if not self.rules["hit_aces"]:
                    card, shuffle = self.next_card(shuffle)
                    hand.add_card(card)
                    if self.strategy:
                        self.strategy.update_running_count(card)
                    print(f"Your hand is now {hand}!")
                    return [], shuffle
            card, shuffle = self.next_card(shuffle)
            hand.add_card(card)
            if self.strategy:
                self.strategy.update_running_count(card)
            print(f"Your hand is now {hand}!")
            return self.get_decisions(hand, shuffle)
        return (decisions, shuffle)

    def make_decision(self, decisions, shuffle, count):
        print(f"Hand currently playing: {self.player_hands[count]}")
        print(f"Dealer hand: {self.dealer_hand.hide_hole_card()}")
        print("")
        print("Enter these to quickly make a decision: st = Stand, h = Hit, sp = Split, d = Double, su = Surrender")
        output = "You can: "
        for i, dec in enumerate(decisions):
            output += f"{dec}, " if i < len(decisions) - 1 else f"{dec}."
        print(output)
        print("")

        while True:
            if not self.strategy:
                decision = input("Enter decision from above: ")
            else:
                decision = self.strategy.sim_decision(decisions, self.player_hands[count].get_value(), self.dealer_hand[0].value, self.check_soft(self.player_hands[count]))
            if decision == "st":
                decision = "Stand"
            elif decision == "h":
                decision = "Hit"
            elif decision == "sp":
                decision = "Split"
            elif decision == "d":
                decision = "Double"
            elif decision == "su":
                decision = "Surrender"

            if decision in decisions:
                break
            else:
                if self.strategy:
                    raise Exception("Lul wut are you doing")
                print("Not a valid decision!")

        if decision == "Stand":
            print("You stood!")
            print("")
            return ("Stand", shuffle)
        elif decision == "Hit":
            card, shuffle = self.next_card(shuffle)
            self.player_hands[count].add_card(card)
            if self.strategy:
                self.strategy.update_running_count(card)
            print(f"You drew {card}!")
            print("")
            return ("Hit", shuffle)
        elif decision == "Double":
            card, shuffle = self.next_card(shuffle)
            self.player_hands[count].add_card(card)
            self.player_hands[count].set_doubled()
            self.player_hands[count].set_bet(self.bet * 2)
            self.bankroll -= self.bet
            if self.strategy:
                self.strategy.update_running_count(card)
            print(f"You doubled and drew {card}!")
            print("")
            return ("Double", shuffle)
        elif decision == "Split":
            hand = self.player_hands.pop(count)
            hand1 = Hand([hand.cards[0]])
            hand1.set_split()
            hand2 = Hand([hand.cards[1]])
            hand2.set_split()
            hand2.set_bet(self.bet)
            self.bankroll -= self.bet
            self.player_hands.insert(count, hand1)
            self.player_hands.insert(count + 1, hand2)
            print("You split your hand!")
            print(f"Your hands: {self.player_hands}")
            print("")
            return ("Split", shuffle)
        elif decision == "Surrender":
            print("You surrendered!")
            print("")
            return ("Surrender", shuffle)

    def play_round(self, bet, shuffle):
        self.bankroll -= bet
        print(f"Your bankroll is ${self.bankroll}")
        print("")
        self.bet = bet
        self.player_hands[0].set_bet(bet)

        # Initial deal
        card, shuffle = self.next_card(shuffle)
        self.player_hands[0].add_card(card)
        if self.strategy:
            self.strategy.update_running_count(card)

        card, shuffle = self.next_card(shuffle)
        self.dealer_hand.add_card(card)
        if self.strategy:
            self.strategy.update_running_count(card)

        card, shuffle = self.next_card(shuffle)
        self.player_hands[0].add_card(card)
        if self.strategy:
            self.strategy.update_running_count(card)

        card, shuffle = self.next_card(shuffle)
        self.dealer_hand.add_card(card)
        if self.strategy:
            self.strategy.update_running_count(card)

        print("")
        print(f"Your hand: {self.player_hands[0]}, Dealer hand: {self.dealer_hand.hide_hole_card()}")
        print("")

        # Dealer peeks
        if self.rules["peeks"] and self.dealer_hand[0].value == 10:
            if self.dealer_hand.get_value() == 21:
                if self.player_hands[0].get_value() == 21:
                    print(f"Dealers hole card is {self.dealer_hand[1]}!")
                    print(f"Dealer has blackjack! {self.dealer_hand}, Draw!")
                    self.bankroll += bet
                    self.strategy.draw()
                    return bet, shuffle
                else:
                    print(f"Dealers hole card is {self.dealer_hand[1]}!")
                    print(f"Dealer has blackjack! {self.dealer_hand}, You lose!")
                    self.strategy.lose()
                    return -bet, shuffle

        # Insurance
        if self.dealer_hand[0].value == 11:
            if not self.strategy:
                insurance = input("Insure hand? (Y/N): ")[0].upper()
                print("")
            else:
                insurance = "N"
            if insurance == "Y":
                insurance = True
                self.bankroll -= bet / 2
                print(f"You bet {bet / 2} on insurance!")
            else:
                insurance = False
            if self.dealer_hand.get_value() == 21:
                if self.player_hands[0].get_value() == 21:
                    print(f"Dealers hole card is {self.dealer_hand[1]}!")
                    print(f"Dealer has blackjack! {self.dealer_hand}, Draw!")
                    self.bankroll += bet
                    self.strategy.draw()
                    return bet, shuffle
                else:
                    print(f"Dealers hole card is {self.dealer_hand[1]}!")
                    print(f"Dealer has blackjack! {self.dealer_hand}, You lose!")
                    if insurance:
                        self.bankroll += bet
                        self.strategy.lose()
                        return bet, shuffle
                    else:
                        self.strategy.lose()
                        return -bet, shuffle
            print("Dealer does not have blackjack!")

        # Check for player blackjack
        if self.player_hands[0].get_value() == 21:
            print("You have blackjack!")
            if self.dealer_hand.get_value() == 21:
                print(f"Dealers hole card is {self.dealer_hand[1]}!")
                print(f"Dealer has blackjack! {self.dealer_hand}, Draw!")
                self.bankroll += bet
                self.strategy.draw()
                return bet, shuffle
            else:
                print(f"Dealers hole card is {self.dealer_hand[1]}!")
                print(f"Dealer doesn't have blackjack! {self.dealer_hand}, You win!")
                self.bankroll += bet * self.rules["bj_payout"]
                self.strategy.win()
                return bet * self.rules["bj_payout"], shuffle

        # Player plays
        count = 0
        while count < len(self.player_hands):
            any_decisions = True
            hand = self.player_hands[count]
            while hand.get_value() < 21 and any_decisions:
                decisions, shuffle = self.get_decisions(hand, shuffle)
                if not decisions:
                    any_decisions = False
                else:
                    choice, shuffle = self.make_decision(decisions, shuffle, count)
                    if choice == "Stand" or choice == "Double":
                        any_decisions = False
                    hand = self.player_hands[count]
            if any_decisions:
                print("You've busted!")
                print("")
                hand.set_busted()
            count += 1
            print(f"Your hand(s): {self.player_hands}")

        # Dealer plays
        print("")
        final_dealer_value, shuffle = self.dealer_plays(shuffle)
        print("")

        # Result check
        money = 0
        for hand in self.player_hands:
            if hand.get_value() > final_dealer_value and not hand.busted:
                print(f"Your hand {hand}, beats {self.dealer_hand}!")
                self.bankroll += hand.bet * 2
                money += hand.bet * 2
                if self.strategy:
                    self.strategy.win()
            elif hand.get_value() == final_dealer_value:
                print(f"Your hand {hand}, draws with {self.dealer_hand}!")
                self.bankroll += bet
                money += hand.bet
                if self.strategy:
                    self.strategy.draw()
            else:
                print(f"Your hand {hand}, loses to {self.dealer_hand}!")
                money -= hand.bet
                if self.strategy:
                    self.strategy.lose()

        # Shuffle if necessary
        if shuffle:
            shuffle = False
            print("Hit the cut card in the last hand, shuffling!")
            print("")
            self.shoe = Shoe(self.std_deck, self.rules["decks"], self.rules["pene"])
            if self.strategy:
                self.strategy.running_count = 4 - (4 * self.rules["decks"])

        return money, shuffle


###########
# RUN
###########


def run(rules, strategy):
    std_deck = [Card(2), Card(3), Card(4), Card(5), Card(6), Card(7), Card(8), Card(9), Card(10), Card(10, "J"), Card(10, "Q"), Card(10, "K"), Card(11, "A"),
                Card(2), Card(3), Card(4), Card(5), Card(6), Card(7), Card(8), Card(9), Card(10), Card(10, "J"), Card(10, "Q"), Card(10, "K"), Card(11, "A"),
                Card(2), Card(3), Card(4), Card(5), Card(6), Card(7), Card(8), Card(9), Card(10), Card(10, "J"), Card(10, "Q"), Card(10, "K"), Card(11, "A"),
                Card(2), Card(3), Card(4), Card(5), Card(6), Card(7), Card(8), Card(9), Card(10), Card(10, "J"), Card(10, "Q"), Card(10, "K"), Card(11, "A")]
    bankroll = input("Enter starting bankroll (min bets are $1): ")
    bankroll = bankroll.strip("$")
    bankroll = float(bankroll)
    starting_bankroll = bankroll
    game = Game(rules, std_deck, bankroll, strategy)
    count = int(input("Enter number of hands to play: ")) if strategy else -1
    start_count = count
    shuffle = False
    while game.bankroll > 0 and count != 0:
        print("")
        if not strategy:
            bet = input("Enter bet amount: ")
            bet = bet.strip("$")
            bet = float(bankroll)
        else:
            bet = strategy.bet_multiplier()
        money, shuffle = game.play_round(bet, shuffle)
        if money > 0:
            print(f"You won ${money}!")
        else:
            print(f"You lost ${money * -1}")
        print(f"Your bankroll is ${game.bankroll}")
        game.reset_hands()
        if strategy:
            count -= 1
    print(f"You made {game.bankroll - starting_bankroll}")
    if strategy:
        win = (strategy.wdl_count[0] / (start_count - count)) * 100
        draw = (strategy.wdl_count[1] / (start_count - count)) * 100
        loss = (strategy.wdl_count[2] / (start_count - count)) * 100
        print("")
        print(f"Hands played: {start_count - count}")
        print(f"Win {win:.2f}%, Draw {draw:.2f}%, Loss {loss:.2f}%, \n House Edge via Basic Strategy: {(win + draw - loss):.2f}, \n House Edge via Profit: {(100 - ((game.bankroll / starting_bankroll) * 100)):.2f}")
