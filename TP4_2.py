#Make a program to solve a taquin 3 by 3 puzzle by BFS

from importlib.resources import path


initial_state = [[1,0,2,4,5,3,7,8,6],1]
goal_state = [[1,2,3,4,5,6,7,8,0],8]

def nextState(s):
    possible_states = []
    
    if(s[1] % 3 != 0):
        possible_states.append( [swap(s[0].copy(),s[1],s[1]-1),s[1]-1] )
    if(s[1] % 3 != 2):
        possible_states.append( [swap(s[0].copy(),s[1],s[1]+1),s[1]+1] )
    if(s[1] > 2):
        possible_states.append( [swap(s[0].copy(),s[1],s[1]-3),s[1]-3] )
    if(s[1] < 6):
        possible_states.append( [swap(s[0].copy(),s[1],s[1]+3),s[1]+3] )

    return possible_states

def swap(s,i,j):

    s[i],s[j] = s[j],s[i]
    return s

def isValide(s, goal_state):
    if(s == goal_state):        
        return True
    return False

def BFS(initial_state,goal_state):
    visited_states = []
    queue = []
    path = []
    queue.append([initial_state,path])
    
    while(len (queue) != 0):
        s = queue.pop(0)
        if(isValide(s[0],goal_state)):
            return path
        
        possible_states = nextState(s[0])
        visited_states.append(s[0])
        for i in range(len(possible_states)):
            if(possible_states[i] not in visited_states):
                
                path=s[1].copy()
                path.append(s[0])
                queue.append([possible_states[i],path])
    return False
            


print(BFS(initial_state,goal_state))

