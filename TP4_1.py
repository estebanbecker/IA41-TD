#Make a program that solve the missionary and cannibal problem

import sys

#Define the initial state
initial_state = [3,3,1]

#Define the goal state
goal_state = [0,0,0]

#Define a function to return the possible states
def nextStates( s ):
    #Define the possible states
    possible_states = []
    
    if( s[2] == 1 ):
        if(isValide( [s[0]-1,s[1],0] )):
            possible_states.append( [s[0]-1,s[1],0] )
        if(isValide( [s[0],s[1]-1,0] )):
            possible_states.append( [s[0],s[1]-1,0] )
        if(isValide( [s[0]-2,s[1],0] )):
            possible_states.append( [s[0]-2,s[1],0] )
        if(isValide( [s[0],s[1]-2,0] )):
            possible_states.append( [s[0],s[1]-2,0] )
        if(isValide( [s[0]-1,s[1]-1,0] )):
            possible_states.append( [s[0]-1,s[1]-1,0] )
    else:
        if(isValide( [s[0]+1,s[1],1] )):
            possible_states.append( [s[0]+1,s[1],1] )
        if(isValide( [s[0],s[1]+1,1] )):
            possible_states.append( [s[0],s[1]+1,1] )
        if(isValide( [s[0]+2,s[1],1] )):
            possible_states.append( [s[0]+2,s[1],1] )
        if(isValide( [s[0],s[1]+2,1] )):
            possible_states.append( [s[0],s[1]+2,1] )
        if(isValide( [s[0]+1,s[1]+1,1] )):
            possible_states.append( [s[0]+1,s[1]+1,1] )

    return possible_states



#Define a function to check if a state is valid
def isValide( s ):
    #If the number of missionaries is less than the number of cannibals on the left side
    if( s[0] < s[1] and s[0] != 0 ):
        return False
    #If the number of missionaries is less than the number of cannibals on the right side
    if( s[0] > s[1] and s[0] != 3 ):
        return False
    #If the number of missionaries is less than 0
    if( s[0] < 0 ):
        return False
    #If the number of cannibals is less than 0
    if( s[1] < 0 ):
        return False
    #If the number of missionaries is greater than 3
    if( s[0] > 3 ):
        return False
    #If the number of cannibals is greater than 3
    if( s[1] > 3 ):
        return False
    
    return True

#Define a function to check if a state is the goal state
def isGoal( s ):
    if( s == goal_state ):
        return True
    else:
        return False

#Define a function to check if a state is already in the frontier
def isAlreadyInFrontier( s, frontier ):
    if( s in frontier ):
        return True
    else:
        return False

#Define a function to check if a state is already in the explored
def isAlreadyInExplored( s, explored ):
    if( s in explored ):
        return True
    else:
        return False

#Define a function to check if a state is already in the frontier or explored
def isAlreadyInFrontierOrExplored( s, frontier, explored ):
    if( isAlreadyInFrontier( s, frontier ) or isAlreadyInExplored( s, explored ) ):
        return True
    else:
        return False

#define a function to print the path
def printPath( path ):
    print("Path:")
    for i in range( len(path) ):
        print(path[i])

#define a function to do a BFS
def BFS( initial_state, goal_state ):

    #Define the frontier
    frontier = []

    #Define the explored
    explored = []

    #Define the path
    path = []

    #Add the initial state to the frontier
    frontier.append( [initial_state, path] )

    #While the frontier is not empty
    while( len(frontier) != 0 ):

        #Get the first state in the frontier
        state = frontier.pop(0)

        #Add the state to the explored
        explored.append( state[0] )

        #If the state is the goal state
        if( isGoal( state[0] ) ):
            path = state[1]
            path.append( state[0] )
            printPath( path )
            return

        #Get the possible states
        possible_states = nextStates( state[0] )

        #For each possible state
        for i in range( len(possible_states) ):
            #If the possible state is not already in the frontier or explored
            if( not isAlreadyInFrontierOrExplored( possible_states[i], frontier, explored ) ):
                #Add the possible state to the frontier
                path = state[1].copy()
                path.append( state[0] )
                frontier.append( [possible_states[i], path] )

    #If the frontier is empty and the goal state is not found
    print("No solution")
    return
 

#Define a function to do a DFS
def DFS( initial_state, goal_state ):

    #Define the frontier
    frontier = []

    #Define the explored
    explored = []

    #Define the path
    path = []

    #Add the initial state to the frontier
    frontier.append( [initial_state, path] )

    #While the frontier is not empty
    while( len(frontier) != 0 ):

        #Get the first state in the frontier
        state = frontier.pop(0)

        #Add the state to the explored
        explored.append( state[0] )

        #If the state is the goal state
        if( isGoal( state[0] ) ):
            path = state[1]
            path.append( state[0] )
            printPath( path )
            return

        #Get the possible states
        possible_states = nextStates( state[0] )

        #For each possible state
        for i in range( len(possible_states) ):
            #If the possible state is not already in the frontier or explored
            if( not isAlreadyInFrontierOrExplored( possible_states[i], frontier, explored ) ):
                #Add the possible state to the frontier
                path = state[1].copy()
                path.append( state[0] )
                frontier.insert( 0, [possible_states[i], path] )

    #If the frontier is empty and the goal state is not found
    print("No solution")
    return

print("BFS:")
BFS( initial_state, goal_state )
print("DFS:")
DFS( initial_state, goal_state )