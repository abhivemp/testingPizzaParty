"""
The driver here 
"""

#from python include hashed_queue_tree
from oracle import OracleAPI

class prize_macine:
    def __init__(self, name):
        name_of_prize = self.name
        name_list = []

    def get_input():
        
        user_name = input("Enter Name: ")
        while user_name:
            self.name_list.append(user_name)
            user_name = input("-> ")

    def generate_prize_winner():
        oracle = OracleAPI("kevin","cisthebestlang")

        user_index = oracle.random_number(0, len(self.name_list)-1)

        return self.name_list[user_index]

    def display_prize_winner():
        winner = generate_prize_winner()

        print("ANNNNNNDDDD the winner isssssss {}".format(winner))
    
