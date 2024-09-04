# python code for working q learning algorithem from RL.
import numpy as np
import random

#init the env varibles for the usage
grid_size=4
goal=(3,3)
actions=["up","down","left","right"]

# init q table for working with the problem
Q_table=np.zeros((grid_size,grid_size,len(actions)))

# define hyperparametrs for working with the problem
learning_rate=0.1
discount_rate=0.9
exploration_rate=0.1
episodes=3000

# define the reward function for working with the reward
def reward(state):
    return 1 if state==goal else 0

# define state transition function for the problem
def next_state(state,action):
    x,y=state
    if action=="up" and x>0:
        x=x-1
    elif action=="down" and x<grid_size-1:
        x=x+1
    elif action=="left" and y>0:
        y=y-1
    elif action=="right" and y<grid_size-1:
        y=y+1
    return (x,y)

# work with the q learning algorithem 
for episode in range(1,episodes+1):
    # start from the init state of the problem
    state=(0,0)
    while state!=goal:
        # exploration by using e-greedy startegy 
        if random.uniform(0,1)<exploration_rate:
            action=random.choice(actions)
        else:
            action_index=np.argmax(Q_table[state[0],state[1]])
            action=actions[action_index]
        
        # getting new state based on the current state and action
        next=next_state(state,action)
        reward_value=reward(next)
        action_index=actions.index(action)
        # update q table by using the above values of the process
        Q_table[state[0],state[1],action_index]+=learning_rate*(reward_value+discount_rate*np.max(Q_table[next[0],next[1]])-Q_table[state[0],state[1],action_index])
        state=next
        if state==goal:
            print("goal state is reached! at {}".format(episode))
        print(state)
    print("episode: {} is completed!".format(episode))



