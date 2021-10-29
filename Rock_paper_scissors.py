import random 
def play():
    user = input("what is your choice? 'R' for rock, 'P' for paper, 'S' for scissor? \n ").lower()
    computer = random.choice(['s', 'r', 'p'])

    if user == computer:
        return "It\'s a tie"
        # r>s, s>p, p>r
    
    if is_win(user, computer):
        return "You win!"

    return "You lost~!" 
def is_win(player, oponent):
    # r>s, s>p, p>r
    if (player == 'r' and oponent == 's' ) or (player == 's' and oponent == 'p') \
         or (player == 'p' and oponent == 'r'):
         return True

print(play())