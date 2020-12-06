#                         --- Day 1: Report Repair ---


# =============================================================================
#                                   PART 1
# =============================================================================

# After saving Christmas five years in a row, you've decided to take a vacation 
# at a nice resort on a tropical island. Surely, Christmas will go on without 
# you. The tropical island has its own currency and is entirely cash-only. The
# gold coins used there have a little picture of a starfish; the locals just
# call them stars. None of the currency exchanges seem to have heard of them,
# but somehow, you'll need to find fifty of these coins by the time you arrive
# so you can pay the deposit on your room. To save your vacation, you need to
# get all fifty stars by December 25th. Collect stars by solving puzzles. Two
# puzzles will be made available on each day in the Advent calendar; the second
# puzzle is unlocked when you complete the first. Each puzzle grants one star.
# Good luck! Before you leave, the Elves in accounting just need you to fix
# your expense report (your puzzle input); apparently, something isn't quite
# adding up. Specifically, they need you to find the two entries that sum to 
# 2020 and then multiply those two numbers together.

with open("day1_input.txt") as file:
    expense_report = [int(x) for x in file.read().split("\n")]

# method 1: brute force
def solve1(arr):
    for i in arr:
        for k in arr:
            if i + k == 2020:
                return i * k

#method 2: lookback dict
def solve2(arr):
    nums = {}
    for i in arr:
        nums[i] = 0
        if 2020 - i in nums:
            return (2020-i) * i


print("Part 1 method 1 solution:", solve1(expense_report))
print("Part 1 method 2 solution:", solve2(expense_report))

# =============================================================================
#                                   PART 2
# =============================================================================

# The Elves in accounting are thankful for your help; one of them even offers 
# you a starfish coin they had left over from a past vacation. They offer you a
# second one if you can find three numbers in your expense report that meet the
# same criteria. Using the above example again, the three entries that sum to
# 2020 are 979, 366, and 675. Multiplying them together produces the answer, 
# 241861950. In your expense report, what is the product of the three entries,
# that sum to 2020?

# method 1: brute force
# completed in 639685 iterations
def p2_solve1(arr):
    for i in arr:
        for j in arr[1:]:
            for k in arr[2:]:
                if i + k + j == 2020:
                    return i*k*j

# method 2: smarter brute force
# completed in 255 iterations
def p2_solve2(arr):
    arr = sorted(arr)
    for i in arr:
        for j in arr[1:]:
            if i + j > 2020 - arr[0]:
                break
            for k in arr[2:]:
                if i + j + k > 2020:
                    break
                if i + j + k == 2020:
                    return i*j*k


print("Part 2 method 1 solution:", p2_solve1(expense_report))
print("Part 2 method 2 solution:", p2_solve2(expense_report))