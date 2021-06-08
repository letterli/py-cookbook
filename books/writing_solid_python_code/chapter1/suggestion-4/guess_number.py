#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Description: 猜数字游戏
# @version python 2.7

"""
适当添加空行使代码布局更为优雅、合理
"""

import random


def guess_number():
    guesses_made = 0

    name = input('Hello! What is your name?')

    number = random.randint(1, 20)

    print('Well, {0}, I am thinking of a number between 1 and 20.'.format(name))

    while guesses_made < 6:
        guess = int(input('Take a guess: '))
        guesses_made += 1

        if guess < number:
            print('Your guess is too low.')
        elif guess > number:
            print('Your guess is too high.')
        else:
            break

    if guess == number:
        print('Good job, {0}! You guessed my number in {1} guesses!'.format(name, guesses_made))
    else:
        print('Nope. The number I was thinking of was {0}'.format(number))
