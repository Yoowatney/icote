def solution(s):
    # answer = 0
    words = ["zero","one", "two", "three", "four", "five", "siv", "seven", "eight", "nine"]
    nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for word, num in zip(words, nums):
        s = s.replace(word, num)
    return int(s)


print(solution("1twothreefourtwo3"))
