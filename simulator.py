class StrategyTable:
    def __init__(self):
        self.hard_values = {
            21: {2: [["Stand"], None], 3: [["Stand"], None], 4: [["Stand"], None], 5: [["Stand"], None], 6: [["Stand"], None], 7: [["Stand"], None], 8: [["Stand"], None], 9: [["Stand"], None], 10: [["Stand"], None], 11: [["Stand"], None]},
            20: {2: [["Stand"], None], 3: [["Stand"], None], 4: [["Stand"], None], 5: [["Stand"], None], 6: [["Stand"], None], 7: [["Stand"], None], 8: [["Stand"], None], 9: [["Stand"], None], 10: [["Stand"], None], 11: [["Stand"], None]},
            19: {2: [["Stand"], None], 3: [["Stand"], None], 4: [["Stand"], None], 5: [["Stand"], None], 6: [["Stand"], None], 7: [["Stand"], None], 8: [["Stand"], None], 9: [["Stand"], None], 10: [["Stand"], None], 11: [["Stand"], None]},
            18: {2: [["Stand"], None], 3: [["Stand"], None], 4: [["Stand"], None], 5: [["Stand"], None], 6: [["Stand"], None], 7: [["Stand"], None], 8: [["Stand"], None], 9: [["Stand"], None], 10: [["Stand"], None], 11: [["Stand"], None]},
            17: {2: [["Stand"], None], 3: [["Stand"], None], 4: [["Stand"], None], 5: [["Stand"], None], 6: [["Stand"], None], 7: [["Stand"], None], 8: [["Stand"], None], 9: [["Stand"], None], 10: [["Stand"], None], 11: [["Stand"], None]},
            16: {2: [["Stand"], None], 3: [["Stand"], None], 4: [["Stand"], None], 5: [["Stand"], None], 6: [["Stand"], None], 7: [["Hit"], None], 8: [["Hit"], None], 9: [["Hit"], None], 10: [["Hit"], None], 11: [["Hit"], None]},
            15: {2: [["Stand"], None], 3: [["Stand"], None], 4: [["Stand"], None], 5: [["Stand"], None], 6: [["Stand"], None], 7: [["Hit"], None], 8: [["Hit"], None], 9: [["Hit"], None], 10: [["Hit"], None], 11: [["Hit"], None]},
            14: {2: [["Stand"], None], 3: [["Stand"], None], 4: [["Stand"], None], 5: [["Stand"], None], 6: [["Stand"], None], 7: [["Hit"], None], 8: [["Hit"], None], 9: [["Hit"], None], 10: [["Hit"], None], 11: [["Hit"], None]},
            13: {2: [["Stand"], None], 3: [["Stand"], None], 4: [["Stand"], None], 5: [["Stand"], None], 6: [["Stand"], None], 7: [["Hit"], None], 8: [["Hit"], None], 9: [["Hit"], None], 10: [["Hit"], None], 11: [["Hit"], None]},
            12: {2: [["Hit"], None], 3: [["Hit"], None], 4: [["Stand"], None], 5: [["Stand"], None], 6: [["Stand"], None], 7: [["Hit"], None], 8: [["Hit"], None], 9: [["Hit"], None], 10: [["Hit"], None], 11: [["Hit"], None]},
            11: {2: [["Double", "Hit"], None], 3: [["Double", "Hit"], None], 4: [["Double", "Hit"], None], 5: [["Double", "Hit"], None], 6: [["Double", "Hit"], None], 7: [["Double", "Hit"], None], 8: [["Double", "Hit"], None], 9: [["Double", "Hit"], None], 10: [["Double", "Hit"], None], 11: [["Hit"], None]},
            10: {2: [["Double", "Hit"], None], 3: [["Double", "Hit"], None], 4: [["Double", "Hit"], None], 5: [["Double", "Hit"], None], 6: [["Double", "Hit"], None], 7: [["Double", "Hit"], None], 8: [["Double", "Hit"], None], 9: [["Double", "Hit"], None], 10: [["Hit"], None], 11: [["Hit"], None]},
            9: {2: [["Hit"], None], 3: [["Double", "Hit"], None], 4: [["Double", "Hit"], None], 5: [["Double", "Hit"], None], 6: [["Double", "Hit"], None], 7: [["Hit"], None], 8: [["Hit"], None], 9: [["Hit"], None], 10: [["Hit"], None], 11: [["Hit"], None]},
            8: {2: [["Hit"], None], 3: [["Hit"], None], 4: [["Hit"], None], 5: [["Hit"], None], 6: [["Hit"], None], 7: [["Hit"], None], 8: [["Hit"], None], 9: [["Hit"], None], 10: [["Hit"], None], 11: [["Hit"], None]},
            7: {2: [["Hit"], None], 3: [["Hit"], None], 4: [["Hit"], None], 5: [["Hit"], None], 6: [["Hit"], None], 7: [["Hit"], None], 8: [["Hit"], None], 9: [["Hit"], None], 10: [["Hit"], None], 11: [["Hit"], None]},
            6: {2: [["Hit"], None], 3: [["Hit"], None], 4: [["Hit"], None], 5: [["Hit"], None], 6: [["Hit"], None], 7: [["Hit"], None], 8: [["Hit"], None], 9: [["Hit"], None], 10: [["Hit"], None], 11: [["Hit"], None]},
            5: {2: [["Hit"], None], 3: [["Hit"], None], 4: [["Hit"], None], 5: [["Hit"], None], 6: [["Hit"], None], 7: [["Hit"], None], 8: [["Hit"], None], 9: [["Hit"], None], 10: [["Hit"], None], 11: [["Hit"], None]},
            4: {2: [["Hit"], None], 3: [["Hit"], None], 4: [["Hit"], None], 5: [["Hit"], None], 6: [["Hit"], None], 7: [["Hit"], None], 8: [["Hit"], None], 9: [["Hit"], None], 10: [["Hit"], None], 11: [["Hit"], None]},
        }

        self.soft_values = {
            21: {2: ["Stand"], 3: ["Stand"], 4: ["Stand"], 5: ["Stand"], 6: ["Stand"], 7: ["Stand"], 8: ["Stand"], 9: ["Stand"], 10: ["Stand"], 11: ["Stand"]},
            20: {2: ["Stand"], 3: ["Stand"], 4: ["Stand"], 5: ["Stand"], 6: ["Stand"], 7: ["Stand"], 8: ["Stand"], 9: ["Stand"], 10: ["Stand"], 11: ["Stand"]},
            19: {2: ["Stand"], 3: ["Stand"], 4: ["Stand"], 5: ["Stand"], 6: ["Stand"], 7: ["Stand"], 8: ["Stand"], 9: ["Stand"], 10: ["Stand"], 11: ["Stand"]},
            18: {2: ["Stand"], 3: ["Double", "Stand"], 4: ["Double", "Stand"], 5: ["Double", "Stand"], 6: ["Double", "Stand"], 7: ["Stand"], 8: ["Stand"], 9: ["Hit"], 10: ["Hit"], 11: ["Hit"]},
            17: {2: ["Hit"], 3: ["Double", "Hit"], 4: ["Double", "Hit"], 5: ["Double", "Hit"], 6: ["Double", "Hit"], 7: ["Hit"], 8: ["Hit"], 9: ["Hit"], 10: ["Hit"], 11: ["Hit"]},
            16: {2: ["Hit"], 3: ["Hit"], 4: ["Double", "Hit"], 5: ["Double", "Hit"], 6: ["Double", "Hit"], 7: ["Hit"], 8: ["Hit"], 9: ["Hit"], 10: ["Hit"], 11: ["Hit"]},
            15: {2: ["Hit"], 3: ["Hit"], 4: ["Double", "Hit"], 5: ["Double", "Hit"], 6: ["Double", "Hit"], 7: ["Hit"], 8: ["Hit"], 9: ["Hit"], 10: ["Hit"], 11: ["Hit"]},
            14: {2: ["Hit"], 3: ["Hit"], 4: ["Hit"], 5: ["Double", "Hit"], 6: ["Double", "Hit"], 7: ["Hit"], 8: ["Hit"], 9: ["Hit"], 10: ["Hit"], 11: ["Hit"]},
            13: {2: ["Hit"], 3: ["Hit"], 4: ["Hit"], 5: ["Double", "Hit"], 6: ["Double", "Hit"], 7: ["Hit"], 8: ["Hit"], 9: ["Hit"], 10: ["Hit"], 11: ["Hit"]},
            12: {2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: [], 10: [], 11: []},
        }

        self.splits = {
            11: {2: [True, True], 3: [True, True], 4: [True, True], 5: [True, True], 6: [True, True], 7: [True, True], 8: [True, True], 9: [True, True], 10: [True, True], 11: [True, True]},
            10: {2: [False, False], 3: [False, False], 4: [False, False], 5: [False, False], 6: [False, False], 7: [False, False], 8: [False, False], 9: [False, False], 10: [False, False], 11: [False, False]},
            9: {2: [True, True], 3: [True, True], 4: [True, True], 5: [True, True], 6: [True, True], 7: [False, False], 8: [True, True], 9: [True, True], 10: [False, False], 11: [False, False]},
            8: {2: [True, True], 3: [True, True], 4: [True, True], 5: [True, True], 6: [True, True], 7: [True, True], 8: [True, True], 9: [True, True], 10: [True, True], 11: [True, True]},
            7: {2: [True, True], 3: [True, True], 4: [True, True], 5: [True, True], 6: [True, True], 7: [True, True], 8: [False, False], 9: [False, False], 10: [False, False], 11: [False, False]},
            6: {2: [False, True], 3: [True, True], 4: [True, True], 5: [True, True], 6: [True, True], 7: [False, False], 8: [False, False], 9: [False, False], 10: [False, False], 11: [False, False]},
            5: {2: [False, False], 3: [False, False], 4: [False, False], 5: [False, False], 6: [False, False], 7: [False, False], 8: [False, False], 9: [False, False], 10: [False, False], 11: [False, False]},
            4: {2: [False, False], 3: [False, False], 4: [False, False], 5: [False, True], 6: [False, True], 7: [False, False], 8: [False, False], 9: [False, False], 10: [False, False], 11: [False, False]},
            3: {2: [False, True], 3: [False, True], 4: [True, True], 5: [True, True], 6: [True, True], 7: [True, True], 8: [False, False], 9: [False, False], 10: [False, False], 11: [False, False]},
            2: {2: [False, True], 3: [False, True], 4: [True, True], 5: [True, True], 6: [True, True], 7: [True, True], 8: [False, False], 9: [False, False], 10: [False, False], 11: [False, False]},
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
        self.optimal = optimal
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
            if self.rules["das"]:
                if self.strategy_table.splits[value // 2 if value % 2 == 0 else 11][dealer_upcard][1]:
                    return "Split"
            else:
                if self.strategy_table.splits[value][dealer_upcard][0]:
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
            return 2
        elif self.rules["decks"] == 2:
            return 1
        elif self.rules["decks"] == 6:
            return -4
        elif self.rules["decks"] == 8:
            return -6

    def bet_multiplier(self):
        if not self.optimal:
            if self.running_count >= self.key_count:
                return self.betting_spread
            return 1
        else:
            if self.running_count > self.key_count:
                return self.betting_spread[list(self.betting_spread.keys())[-1]]
            elif self.running_count < list(self.betting_spread.keys())[1]:
                return self.betting_spread[list(self.betting_spread.keys())[1]]
            return self.betting_spread[self.running_count]

    def update_running_count(self, card):
        if card.true_value > 9:
            self.running_count -= 1
        elif card.true_value < 8:
            self.running_count += 1

    def optimal_bet_spread(self):
        if self.rules["decks"] == 1:
            self.betting_spread = {
                1: 1,
                2: 2,
                3: 4,
                4: 5
            }
        elif self.rules["decks"] == 2:
            self.betting_spread = {
                0: 1,
                1: 2,
                2: 3,
                3: 4,
                4: 5
            }
        elif self.rules["decks"] == 6:
            self.betting_spread = {
                -5: 1,
                -4: 2,
                -3: 2,
                -2: 3,
                -1: 4,
                0: 5,
                1: 6,
                2: 8,
                3: 9,
                4: 10
            }
        elif self.rules["decks"] == 8:
            self.betting_spread = {
                -7: 1,
                -6: 2,
                -5: 2,
                -4: 2,
                -3: 3,
                -2: 4,
                -1: 5,
                0: 6,
                1: 7,
                2: 8,
                3: 9,
                4: 10
            }

    def win(self):
        self.wdl_count[0] += 1

    def draw(self):
        self.wdl_count[1] += 1

    def lose(self):
        self.wdl_count[2] += 1
