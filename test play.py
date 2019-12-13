from ETTTenv import extreme_TTT

env = extreme_TTT()
env.reset()

while not env.done:
    env.print_board()
    if env.player == 1:
        print(f"Player 1 turn!")
    else:
        print(f"Player 2 turn!")
    # print(env.get_possible_moves())
    
    move_cell = int(input("INPUT MOVE CELL: "))
    move_subcell = int(input("INPUT MOVE SUBCELL: "))
    if (move_cell, move_subcell) not in env.get_possible_moves():
        continue
    else:
        env.move((move_cell, move_subcell))
