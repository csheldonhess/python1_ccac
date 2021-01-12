# -*- coding: utf-8 -*-
'''
Coral
Python 1 - DAT-119 
Dice roller module example
'''

import random


def d4():
	"""gives us a random number from 1-4"""
	return random.randint(1, 4)


def d6():
	"""gives us a random number from 1-6"""
	return random.randint(1, 6)


def d8():
	"""gives us a random number from 1-8"""
	return random.randint(1, 8)


def d10():
	"""gives us a random number from 1-10"""
	return random.randint(1, 10)


def d12():
	"""gives us a random number from 1-12"""
	return random.randint(1, 12)


def d20():
	"""gives us a random number from 1-20"""
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
