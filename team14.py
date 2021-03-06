####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Domination' # Only 10 chars displayed.
strategy_name = 'Example Dominator'
strategy_description = 'How does this strategy decide?'

import random
        
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.
    
    Make my move.
    Returns 'c' or 'b'. 
    '''

    # my_history: a string with one letter (c or b) per round that has been played with this opponent.
    # their_history: a string of the same length as history, possibly empty. 
    # The first round between these two players is my_history[0] and their_history[0].
    # The most recent round is my_history[-1] and their_history[-1].
    
    # Analyze my_history and their_history and/or my_score and their_score.
    # Decide whether to return 'c' or 'b'.
    
    if len(my_history)==1 and their_history[-1] == 'b':##betray if 1st move was to betray
        return 'b'
    elif len(my_history)<3:#collude if first 3 moves are collude
        return 'c' 
    elif 'bbb' in their_history or 'b' in their_history[-2:]:#Pattern sensing if someone is always betraying then I will betray
        return 'b'
    elif 'ccc' in their_history and their_history<=100 and not 'b' in their_history:
        return 'c'        
    elif 'ccccccccc' in their_history and their_history>100:
        if 'b' in their_history: 
            return 'b'
        elif len(my_history)>105 and 'b' not in their_history:
            return 'b' 
        elif random.random()<0.05: # 5% of the other rounds
            return 'b'         # Betray
        else:
            return 'c'
            
    elif my_history[-1]=='c' and their_history[-1]=='b':
        return 'b'
    else:
        return 'c'            
        
    
def test_move(my_history, their_history, my_score, their_score, result):
    '''calls move(my_history, their_history, my_score, their_score)
    from this module. Prints error if return value != result.
    Returns True or False, dpending on whether result was as expected.
    '''
    real_result = move(my_history, their_history, my_score, their_score)
    if real_result == result:
        return True
    else:
        print("move(" +
            ", ".join(["'"+my_history+"'", "'"+their_history+"'",
                       str(my_score), str(their_score)])+
            ") returned " + "'" + real_result + "'" +
            " and should have returned '" + result + "'")
        return False

if __name__ == '__main__':
     
    # Test 1: Betray on first move.
    if test_move(my_history='',
              their_history='', 
              my_score=0,
              their_score=0,
              result='c'):
         print 'Test passed'
     # Test 2: Continue betraying if they collude despite being betrayed.
    test_move(my_history='bbb',
              their_history='ccc', 
              # Note the scores are for testing move().
              # The history and scores don't need to match unless
              # that is relevant to the test of move(). Here,
              # the simulation (if working correctly) would have awarded 
              # 300 to me and -750 to them. This test will pass if and only if
              # move('bbb', 'ccc', 0, 0) returns 'b'.
              my_score=0, 
              their_score=0,
              result='c')             