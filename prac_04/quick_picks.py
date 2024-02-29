import random

MIN_NUM = 1
MAX_NUM = 45
NUM_PER_LINE = 6
NUM_QUICK_PICKS = int(input("How many quick picks? "))


def generate_quick_pick():
    return sorted(random.sample(range(MIN_NUM, MAX_NUM + 1), NUM_PER_LINE))


for _ in range(NUM_QUICK_PICKS):
    quick_pick = generate_quick_pick()
    print(" ".join(map(str, quick_pick)))
