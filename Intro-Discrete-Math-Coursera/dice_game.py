import itertools

def count_wins(dice1, dice2):

    assert len(dice1) == 6 and len(dice2) == 6

    dice1_wins, dice2_wins = 0, 0
    for i in dice1:
        for ii in dice2:
            if i > ii:
                dice1_wins += 1
            elif ii > i:
                dice2_wins += 1

    return (dice1_wins, dice2_wins)


def find_the_best_dice(dices):

    d = {}
    for ind in range(len(dices)):
        d[ind] = 0
    for combinations in itertools.combinations(dices,2):

       dice1_score, dice2_score = count_wins(combinations[0],combinations[1])

       if dice1_score > dice2_score:             # How many times dice1 wins.
           d[dices.index(combinations[0])] += 1
       elif dice1_score < dice2_score:           # How many times dice2 wins.
           d[dices.index(combinations[1])] += 1

    final_val = 0
    for k,v in d.items():
        if v == len(dices)-1:            # best dice would be the one who (len(dices)-1) times, against all others. 
            final_val = k
            break
        else:
            final_val = -1               # return -1 when best dices are not found.
    return final_val



def compute_strategy(dices):
    strategy = {}

    if find_the_best_dice(dices) == -1:         #Because no best dices are found
        strategy["choose_first"] = False

        for i in dices:                         # i is your opponent
            for j in dices:                     # j is you.
                if i != j:                      # so that you don't play against yourself
                    score_i, score_j = count_wins(i,j)
                    if score_i < score_j:               # This ensures you choose best dice against opponent
                        strategy[dices.index(i)] = dices.index(j)
    elif find_the_best_dice(dices) != -1:
        strategy["choose_first"] = True
        strategy["first_dice"] = find_the_best_dice(dices) # already determined by find_the_best_dices()
    return strategy

