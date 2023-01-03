from collections import deque


OP_NUM_IDX = -1
TEST_NUM_IDX = -1
OP_IDX = 4
ROUNDS = 10000

monkeys = []
# this will be the product of all the divisors from the tests
m = 1

class Monkey:
    def __init__(self, items, op, test, true_monkey, false_monkey):
        self.items = deque(items)
        op_tokens = op.split()
        self.same_op_num = False
        if op_tokens[OP_NUM_IDX] == "old":
            self.same_op_num = True
        else:
            self.op_num = int(op_tokens[OP_NUM_IDX])
        self.op = op_tokens[OP_IDX]
        test_tokens = test.split()
        self.test_num = int(test_tokens[TEST_NUM_IDX])
        self.true_monkey = int(true_monkey.split()[-1])
        self.false_monkey = int(false_monkey.split()[-1])
        self.inspect_count = 0

    def inspect(self, item):
        worry_level = item
        if self.op == "+":
            if self.same_op_num:
                worry_level += item
            else:
                worry_level += self.op_num

        elif self.op == "*":
            if self.same_op_num:
                worry_level *= item
            else:
                worry_level *= self.op_num

        worry_level = worry_level % m
        self.inspect_count += 1

        return worry_level

    def test(self, worry_level):
        return True if worry_level % self.test_num == 0 else False

    def remove_item(self):
        if self.items:
            return self.items.popleft()
        
        # deque is empty
        return None

    def give_monkey_item(self, condition, worry_level):
        if condition:
            monkeys[self.true_monkey].items.append(worry_level)

        else:
            monkeys[self.false_monkey].items.append(worry_level)

input = []
with open('input.txt') as file:
    for line in file:
        line = line.strip("\n")
        if line:
            input.append(line)

i = 0
while i < len(input):
    # parse starting items
    starting_items = input[i + 1].split(":")
    items_str = starting_items[-1].split(",")
    items = []
    for item_str in items_str:
        item_str = item_str.strip()
        items.append(int(item_str))

    op_str = input[i + 2]
    test_str = input[i + 3]
    true_str = input[i + 4]
    false_str = input[i + 5]
    m *= int(test_str.split()[TEST_NUM_IDX])

    # create monkey
    monkeys.append(Monkey(items, op_str, test_str, true_str, false_str))

    i += 6

r = 0
while r < ROUNDS:
    for monkey in monkeys:
        while monkey.items:
            item = monkey.remove_item()
            worry_level = monkey.inspect(item)
            test_res = monkey.test(worry_level)
            monkey.give_monkey_item(test_res, worry_level)

    r += 1

ans = []
for monkey in monkeys:
    ans.append(monkey.inspect_count)

ans.sort(reverse=True)
print(ans[0] * ans[1])