#
# CS1010FC --- Programming Methodology
#
# Mission N Solutions
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.
import random
import constants as c

#######
#Task 1a#
#######

# [Marking Scheme]
# Points to note:
# Matrix elements must be equal but not identical
# 1 mark for creating the correct matrix

# return iniialized matrix

def new_game(n):
    matrix = []

    for i in range(n):
    #####################################################################
    # TODO:                                                             #
    #                                                                   #
    #                                                                   #
    #                                                                   #
    #####################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    return matrix

###########
# Task 1b #
###########

# [Marking Scheme]
# Points to note:
# Must ensure that it is created on a zero entry
# 1 mark for creating the correct loop


def add_two(mat):
    a = random.randint(0, len(mat)-1)
    b = random.randint(0, len(mat)-1)

    #####################################################################
    # TODO:                                                             #
    #                                                                   #
    #                                                                   #
    #                                                                   #
    #####################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    mat[a][b] = 2
    return mat

###########
# Task 1c #
###########

# [Marking Scheme]
# Points to note:
# Matrix elements must be equal but not identical
# 0 marks for completely wrong solutions
# 1 mark for getting only one condition correct
# 2 marks for getting two of the three conditions
# 3 marks for correct checking


def game_state(mat):
    #####################################################################
    # TODO:               check if 2048 exists                                              
    #                                                                   
    #                                                                   
    #                                                                   
    #####################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****


    
    for i in range(len(mat)-1):
        # intentionally reduced to check the row on the right and below
        # more elegant to use exceptions but most likely this will be their solution
        for j in range(len(mat[0])-1):
            if mat[i][j] == mat[i+1][j] or mat[i][j+1] == mat[i][j]:
                return 'not over'
                
    for i in range(len(mat)):  
    #####################################################################
    # TODO:              check for any zero entries                                              
    #                                                                   
    #                                                                   
    #                                                                   
    #####################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

                return 'not over'

                
    for k in range(len(mat)-1):  
    #####################################################################
    # TODO:         to check the left/right entries on the last row                                             
    #                                                                   
    #                                                                   
    #                                                                   
    #####################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

                return 'not over'



    for j in range(len(mat)-1):  
    #####################################################################
    # TODO:         What else?                                             
    #                                                                   
    #                                                                   
    #                                                                   
    #####################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
            return 'not over'


    return 'lose'

###########
# Task 2a #
###########

# [Marking Scheme]
# Points to note:
# 0 marks for completely incorrect solutions
# 1 mark for solutions that show general understanding
# 2 marks for correct solutions that work for all sizes of matrices


def reverse(mat):
    new = []
    for i in range(len(mat)):
        new.append([])
        for j in range(len(mat[0])):
            #####################################################################
            # TODO:         Reverse input matrix (mat)                                            
            #               Refer to Task 2b for help                                                    
            #                                                                   
            #                                                                   
            #####################################################################
            # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

            pass

            # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    return new

###########
# Task 2b #
###########

# [Marking Scheme]
# Points to note:
# 0 marks for completely incorrect solutions
# 1 mark for solutions that show general understanding
# 2 marks for correct solutions that work for all sizes of matrices


def transpose(mat):
    new = []
    for i in range(len(mat[0])):
        new.append([])
        for j in range(len(mat)):
            new[i].append(mat[j][i])
    return new

##########
# Task 3 #
##########

# [Marking Scheme]
# Points to note:
# The way to do movement is compress -> merge -> compress again
# Basically if they can solve one side, and use transpose and reverse correctly they should
# be able to solve the entire thing just by flipping the matrix around
# No idea how to grade this one at the moment. I have it pegged to 8 (which gives you like,
# 2 per up/down/left/right?) But if you get one correct likely to get all correct so...
# Check the down one. Reverse/transpose if ordered wrongly will give you wrong result.


def cover_up(mat):
    new = []
    for j in range(c.GRID_LEN):
        partial_new = []
        for i in range(c.GRID_LEN):
            partial_new.append(0)
        new.append(partial_new)
    done = False
    for i in range(c.GRID_LEN):
        count = 0
        for j in range(c.GRID_LEN):
            if mat[i][j] != 0:
                new[i][count] = mat[i][j]
                if j != count:
                    done = True
                count += 1
    return (new, done)


def merge(mat):
    done = False
    for i in range(c.GRID_LEN):
        for j in range(c.GRID_LEN-1):
    #####################################################################
    # TODO:       # sum up the scores if adjacent slots have same number                                           
    #                                                                   
    #                                                                   
    #                                                                   
    #####################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    return (mat, done)


def up(game):
    print("up")
    # return matrix after shifting up
    game = transpose(game)
    game, done = cover_up(game)
    temp = merge(game)
    game = temp[0]
    done = done or temp[1]
    game = cover_up(game)[0]
    game = transpose(game)
    return (game, done)


def down(game):
    #####################################################################
    # TODO:       # return matrix after shifting down                                           
    #                                                                   
    #                                                                   
    #                                                                   
    #####################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****


def left(game):
    print("left")
    
    #####################################################################
    # TODO:         # return matrix after shifting left                                          
    #                                                                   
    #                                                                   
    #                                                                   
    #####################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****


def right(game):
    print("right")
    
    #####################################################################
    # TODO:       # return matrix after shifting right                                           
    #                                                                   
    #                                                                   
    #                                                                   
    #####################################################################
    # *****START OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****

    pass

    # *****END OF YOUR CODE (DO NOT DELETE/MODIFY THIS LINE)*****
    return (game, done)
