#!/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
import random

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        super().move()
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        super().move()
        human_choice = input("Enter your move by typing either"
                             " 'rock',"
                             " 'paper',"
                             " or 'scissors':\n")
        while True:
            if human_choice == 'rock' \
                    or human_choice == 'paper' \
                    or human_choice == 'scissors':
                return human_choice
            else:
                human_choice = input("Please enter a valid move:\n")
                continue


class ReflectPlayer(Player):
    def __init__(self):
        self.their_last_move = None
        self.my_move = None

    def move(self):
        super().move()
        return self.their_last_move

    def learn(self, my_move, their_move):
        super().learn(my_move, their_move)


class CyclePlayer(Player):
    my_current_move = None
    my_last_move = None
    def move(self):
        super().move()
        return self.my_current_move

    def learn(self, my_move, their_move):
        super().learn(my_move, their_move)
        if self.my_last_move == 'rock':
            self.my_current_move = 'paper'
        elif self.my_last_move == 'paper':
            self.my_current_move = 'scissors'
        elif self.my_last_move == 'scissors':
            self.my_current_move = 'rock'


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    comp_score = 0
    your_score = 0
    m1 = ''
    m2 = ''

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def outcome(self, m1, m2):
        while (m1 == 'rock' or m1 == 'paper' or m1 == 'scissors') and \
                (m2 == 'rock' or m2 == 'paper' or m2 == 'scissors'):
            if beats(m1, m2):
                self.comp_score += 1
                print("Computer wins")
                print(f"Computer score: {self.comp_score}\n"
                      f"Your score: {self.your_score}")
                break
            elif beats(m2, m1):
                self.your_score += 1
                print("You win")
                print(f"Computer score: {self.comp_score}\n"
                      f"Your score: {self.your_score}")
                break
            else:
                print("It's a draw")
                break
        else:
            print("Please enter a valid move")

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Computer: {move1}  You: {move2}")
        self.outcome(move1, move2)
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):

        print("Game start!")
        rounds = 3
        for round in range(rounds):
            print(f"Round {round + 1}:")
            self.play_round()

    def final_result(self):
        print(f"Final Score:\n"
              f"Computer: {self.comp_score}\n"
              f"You: {self.your_score}")
        if self.comp_score > self.your_score:
            print("The computer wins")
        elif self.comp_score < self.your_score:
            print("You win!")
        else:
            print("It's a draw")
        print("Game over!")

    def repeat(self):
        while True:
            print("Do you want to play again?")
            inp = input("Enter 'y' for yes and 'n' for no\n")
            if inp.lower() == 'n':
                print("Thanks for playing")
                break
            elif inp.lower() == 'y':
                game.play_game()
                game.final_result()
            else:
                print("Please enter valid input")
                continue


if __name__ == '__main__':
    game = Game(CyclePlayer(), HumanPlayer())
    game.play_game()
    game.final_result()
    game.repeat()
