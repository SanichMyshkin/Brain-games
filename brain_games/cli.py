#!/usr/bin/env python

import prompt

def welcome_user():
	name = prompt.string('May I have your name? ')
	print("Hellow, {0}!".format(name))

if __name__ == '__main__':
    welcome_user()
