import bot


def average():
    success_rate = 0
    solved_count = 0
    while True:
        solve = 1 if bot.solve() is True else 0
        success_rate = (solved_count * success_rate + solve) / (solved_count + 1)
        solved_count += 1
        if (solved_count / 250).is_integer():
            print(f"{round(success_rate * 100, 3)}%. {solved_count} matches")


#average()
bot.solve()
