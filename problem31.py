# ProjectEuler, solution to problem 31 #
# This solution is an example of a State Space Tree, Without the use of Backtracking #

from math import ceil

class CoinsCounter:
    def __init__(self, coins, target):
        self.coins = coins
        self.max_index = len(coins) - 1
        self.target = target
        self.solutions_count = 0
    
    def count_solutions(self):
        state = State(self, 0,self.target)
        state.generate_child_states()
        return self.solutions_count


class State:
    def __init__(self, context_table, unit_index, target_sum):
        self.context = context_table
        self.unit_index = unit_index
        self.unit = self.context.coins[unit_index]
        self.target_sum = target_sum
        self.factors = []
        self.find_factors()
        self.count_solution()

    def count_solution(self):
        if self.target_sum % self.unit == 0:
            self.context.solutions_count += 1

    def find_factors(self):
        max_factor = ceil(self.target_sum / self.unit - 1)
        self.factors = list(range(max_factor, -1, -1))
    
    def generate_child_states(self):
        if self.unit_index == self.context.max_index:
            return
        for f in self.factors:
            index = self.unit_index + 1
            sub_target = self.target_sum - (f * self.unit)
            child = State(self.context, index, sub_target)
            child.generate_child_states()


if __name__ == "__main__":
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    target = 200
    coins_counter = CoinsCounter(coins, target)
    count = coins_counter.count_solutions()
    print(f"Total number of solutions: {count}")