# dice roller module
import random

def d4():
	return random.randint(1, 4)

def d6():
	return random.randint(1, 6)

def d8():
	return random.randint(1, 8)

def d10():
	return random.randint(1, 10)

def d12():
	return random.randint(1, 12)

def d20():
	return random.randint(1, 20)

def main():
	print("4-sided die:", d4())
	print("6-sided die:", d6())
	print("8-sided die:", d8())
	print("10-sided die:", d10())
	print("12-sided die:", d12())
	print("20-sided die:", d20())

if __name__ == "__main__":
	main()
