class StrategyTable:
    def __init__(self):
        self.hard_values = {
            21: {2: [[], None], 3: [[], None], 4: [[], None], 5: [[], None], 6: [[], None], 7: [[], None], 8: [[], None], 9: [[], None], 10: [[], None], 11: [[], None]},
            20: {2: [[], None], 3: [[], None], 4: [[], None], 5: [[], None], 6: [[], None], 7: [[], None], 8: [[], None], 9: [[], None], 10: [[], None], 11: [[], None]},
            19: {2: [[], None], 3: [[], None], 4: [[], None], 5: [[], None], 6: [[], None], 7: [[], None], 8: [[], None], 9: [[], None], 10: [[], None], 11: [[], None]},
            18: {2: [[], None], 3: [[], None], 4: [[], None], 5: [[], None], 6: [[], None], 7: [[], None], 8: [[], None], 9: [[], None], 10: [[], None], 11: [[], None]},
            17: {2: [[], None], 3: [[], None], 4: [[], None], 5: [[], None], 6: [[], None], 7: [[], None], 8: [[], None], 9: [[], None], 10: [[], None], 11: [[], None]},
            16: {2: [[], None], 3: [[], None], 4: [[], None], 5: [[], None], 6: [[], None], 7: [[], None], 8: [[], None], 9: [[], None], 10: [[], None], 11: [[], None]},
            15: {2: [[], None], 3: [[], None], 4: [[], None], 5: [[], None], 6: [[], None], 7: [[], None], 8: [[], None], 9: [[], None], 10: [[], None], 11: [[], None]},
            14: {2: [[], None], 3: [[], None], 4: [[], None], 5: [[], None], 6: [[], None], 7: [[], None], 8: [[], None], 9: [[], None], 10: [[], None], 11: [[], None]},
            13: {2: [[], None], 3: [[], None], 4: [[], None], 5: [[], None], 6: [[], None], 7: [[], None], 8: [[], None], 9: [[], None], 10: [[], None], 11: [[], None]},
            12: {2: [[], None], 3: [[], None], 4: [[], None], 5: [[], None], 6: [[], None], 7: [[], None], 8: [[], None], 9: [[], None], 10: [[], None], 11: [[], None]},
            11: {2: [[], None], 3: [[], None], 4: [[], None], 5: [[], None], 6: [[], None], 7: [[], None], 8: [[], None], 9: [[], None], 10: [[], None], 11: [[], None]},
            10: {2: [[], None], 3: [[], None], 4: [[], None], 5: [[], None], 6: [[], None], 7: [[], None], 8: [[], None], 9: [[], None], 10: [[], None], 11: [[], None]},
            9: {2: [[], None], 3: [[], None], 4: [[], None], 5: [[], None], 6: [[], None], 7: [[], None], 8: [[], None], 9: [[], None], 10: [[], None], 11: [[], None]},
            8: {2: [[], None], 3: [[], None], 4: [[], None], 5: [[], None], 6: [[], None], 7: [[], None], 8: [[], None], 9: [[], None], 10: [[], None], 11: [[], None]},
            7: {2: [[], None], 3: [[], None], 4: [[], None], 5: [[], None], 6: [[], None], 7: [[], None], 8: [[], None], 9: [[], None], 10: [[], None], 11: [[], None]},
            6: {2: [[], None], 3: [[], None], 4: [[], None], 5: [[], None], 6: [[], None], 7: [[], None], 8: [[], None], 9: [[], None], 10: [[], None], 11: [[], None]},
            5: {2: [[], None], 3: [[], None], 4: [[], None], 5: [[], None], 6: [[], None], 7: [[], None], 8: [[], None], 9: [[], None], 10: [[], None], 11: [[], None]},
            4: {2: [[], None], 3: [[], None], 4: [[], None], 5: [[], None], 6: [[], None], 7: [[], None], 8: [[], None], 9: [[], None], 10: [[], None], 11: [[], None]},
        }

        self.soft_values = {
            21: {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: []},
            20: {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: []},
            19: {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: []},
            18: {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: []},
            17: {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: []},
            16: {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: []},
            15: {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: []},
            14: {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: []},
            13: {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: []},
            12: {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: []},
        }

        self.splits = {
            11: {2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True, 10: True, 11: True},
            10: {2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False, 10: False, 11: False},
            9: {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: []},
            8: {2: True, 3: True, 4: True, 5: True, 6: True, 7: True, 8: True, 9: True, 10: True, 11: True},
            7: {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: []},
            6: {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: []},
            5: {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: []},
            4: {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: []},
            3: {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: []},
            2: {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: []},
        }

        self.surrender = {
            16: [9, 10, 11],
            15: [10],
        }

        def set_strategy_value(self, dict, row, col, value):
            self.dict["row"]["col"] = value


class Strategy:
    def __init__(self, strategy_table, rules, betting_spread, deviations, optimal=False):
        self.strategy_table = strategy_table
        self.rules = rules
        self.betting_spread = betting_spread
        if self.optimal:
            self.optimal_bet_spread()
        self.deviations = deviations
        self.running_count = 4 - (4 * self.rules["decks"])
        self.key_count = self.find_key_count()
        self.wdl_count = [0, 0, 0]

    def set_betting_spread(self, value):
        self.betting_spread = value

    def sim_decision(self, decisions, value, dealer_upcard, soft):
        if "Split" in decisions:
            if self.strategy_table.splits[value][dealer_upcard]:
                return "Split"
        if soft:
            for dec in self.strategy_table.soft_values[value][dealer_upcard]:
                if dec in decisions:
                    return dec
        if self.deviations:
            if self.strategy_table.hard_values[value][dealer_upcard][1] is not None:
                if self.running_count > self.strategy_table.hard_values[value][dealer_upcard][1][0]:
                    return self.strategy_table.hard_values[value][dealer_upcard][1][1]
        for dec in self.strategy_table.hard_values[value][dealer_upcard][0]:
            if dec in decisions:
                return dec

    def find_key_count(self):
        if self.rules["decks"] == 1:
            self.key_count = 2
        elif self.rules["decks"] == 2:
            self.key_count = 1
        elif self.rules["decks"] == 6:
            self.key_count = -4
        elif self.rules["decks"] == 8:
            self.key_count = -6

    def bet_lookup(self):
        if not self.optimal:
            if self.running_count >= self.key_count:
                return self.betting_spread
            return 1
        else:
            if self.running_count >= self.key_count:
                return self.betting_spread[list(self.betting_spread.keys())[-1]]
            elif self.running_count < list(self.betting_spread.keys())[1]:
                return self.betting_spread[list(self.betting_spread.keys())[1]]
            return self.betting_spread[self.running_count]

    def update_running_count(self, card):
        if card.value > 9:
            self.running_count -= 1
        elif card.value < 8:
            self.running_count += 1

    def optimal_bet_spread(self):
        if self.rules["decks"] == 1:
            self.betting_spread = {}
        elif self.rules["decks"] == 2:
            self.betting_spread = {}
        elif self.rules["decks"] == 6:
            self.betting_spread = {}
        elif self.rules["decks"] == 8:
            self.betting_spread = {}

    def win(self):
        self.wdl_count[0] += 1

    def draw(self):
        self.wdl_count[1] += 1

    def lose(self):
        self.wdl_count[2] += 1
