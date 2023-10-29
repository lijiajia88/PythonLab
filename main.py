# Python will generate a random answer between 1 and 99 inclusive.
# The user then has a maximum of 10 attempts to guess the number.
# If the user guesses correctly, the game is won.
# If the user guesses too low, a “too low” message is generated.
#If the user guesses too high, a “too high” message is generated.
# If the user enters a number that was previously input, a message “you
#tried that already” is generated and the turn count is not increased.
# The user can quit the game by entering a guess of -1.


import random


def generateAnswer():
    return random.randint(1, 99)


def analyseGuess(answer, guess):
    if guess < answer:
        return -1  # 猜测太低
    elif guess > answer:
        return -2  # 猜测太高
    else:
        return 0  # 猜测正确


def checkPrevious(guesses, guess):
    return guess in guesses


def main():
    answer = generateAnswer()
    attempts = 0
    guessed_numbers = []

    print("欢迎参加猜数字游戏！")
    print("我已经生成了一个1到99之间的随机数字。你有最多10次尝试。")

    while attempts < 10:
        guess = int(input("请输入你的猜测 (-1 退出): "))

        if guess == -1:
            print("游戏结束。正确答案是:", answer)
            break

        if guess < 1 or guess > 99:
            print("请输入1到99之间的数字。")
            continue

        if checkPrevious(guessed_numbers, guess):
            print("你已经尝试过这个数字了。")
            continue

        attempts += 1
        guessed_numbers.append(guess)

        result = analyseGuess(answer, guess)
        if result == -1:
            print("太低了，再试一次。")
        elif result == -2:
            print("太高了，再试一次。")
        else:
            print(f"恭喜！你猜对了，答案是 {answer}。你用了 {attempts} 次尝试。")
            break

    if attempts == 10:
        print("很遗憾，你用完了所有的尝试。正确答案是:", answer)


# 启动游戏
main()
