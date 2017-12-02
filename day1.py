def captcha(s, step):
	digits = list(map(int, s))
	return sum(d for i, d in enumerate(digits) if digits[i-step] == d)


s = input()
print(captcha(s, 1)) # part one
print(captcha(s, len(s) // 2)) # part two