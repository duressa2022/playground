# code for working with q learning algorithem
import numpy as np
import random
# create a class for repsenting the env
class Enviroment:
    def __init__(self,size):
        self.grid_size=size
        self.state=(0,0)
        self.goal=(self.grid_size-1,self.grid_size-1)
        self.actions=["up","down","left","right"]
    def reset(self):
        self.state=(0,0)
        return self.state,self.goal

    def next_state(self,action):
        x,y=self.state
        if action=="up" and x>0:
            x=x-1
        elif action=="down" and x<self.grid_size-1:
            x=x+1
        elif action=="left" and y>0:
            y=y-1
        elif action=="right" and y<self.grid_size-1:
            y=y+1
        return (x,y)
    def reward(self,next):
        return 1 if next==self.goal else 0
    
# create a procedure for working with q learning
learning_rate=0.1
discount_rate=0.9
exploration_rate=0.1
episodes=1000
env=Enviroment(size=4)
q_table=np.zeros((env.grid_size,env.grid_size,len(env.actions)))

for episode in range(episodes):
    env.reset()
    while env.state!=env.goal:
        if random.uniform(0,1)<exploration_rate:
            action=random.choice(env.actions)
        else:
            action_index=np.argmax(q_table[env.state[0],env.state[1]])
            action=env.actions[action_index]
        next_state=env.next_state(action)
        action_index=env.actions.index(action)
        reward=env.reward(next_state)
        q_table[env.state[0],env.state[1],action_index]+=learning_rate*(reward+discount_rate*np.max(q_table[next_state[0],next_state[1]])-q_table[env.state[0],env.state[1],action_index])

        env.state=next_state
        if env.state==env.goal:
            print("goal is reached")
        print(env.state)



