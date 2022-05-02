"""
The driver here 
"""

#from python include hashed_queue_tree
from oracle import OracleAPI

class PrizeMachine():

    def __init__(self, name):
        self.name_of_prize = name
        self.name_list = []

    def get_input(self):
        
        user_name = input("Enter Name: ")
        while user_name:
            self.name_list.append(user_name)
            user_name = input("-> ")

    def generate_prize_winner(self):
        oracle = OracleAPI("kevin","cisthebestlang")

        user_index = oracle.random_number(0, len(self.name_list)-1)

        return self.name_list[user_index]

    def display_prize_winner(self):
        winner = generate_prize_winner()

        print("ANNNNNNDDDD the winner isssssss {}".format(winner))
    
