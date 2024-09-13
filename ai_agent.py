# create an class for repersenting the env
import numpy as np
import random
from time import sleep
class Enviroment:
    def __init__(self,size):
        self.size=size
        self.state=(0,0)
        self.goal=(size-1,size-1)
        self.actions=["up","down","left","right"]
        self.board=[[" . " for _ in range(self.size)] for _ in range(self.size)]
    def reset(self):
        self.state=(0,0)
    def reward(self,next):
        return 1 if next==self.goal else 0
    def next_state(self,action):
        x,y=self.state
        if action=="up" and x>0:
            x=x-1
        elif action=="down" and x<self.size-1:
            x=x+1
        elif action=="left" and y>0:
            y=y-1
        elif action=="right" and y<self.size-1:
            y=y+1
        return (x,y)
    def render(self):
        print("=====================================")
        for row in range(self.size):
            for col in range(self.size):
                print(self.board[row][col],end="")
            print("")
        print("==================================")
    def update(self,row,col):
        self.board[row][col]="A"
    def resetBoard(self):
        self.board=[[" . " for _ in range(self.size)] for _ in range(self.size)]

# create the program to excute the learning algorithem
learning_rate=0.1
discount_rate=0.9
exploration_rate=0.3
episodes=1000
env=Enviroment(4)
Q_table=np.zeros((env.size,env.size,len(env.actions)))

for episode in range(episodes):

    env.reset()
    env.resetBoard()
    env.board[0][0]="A"
    env.render()

    while env.state!=env.goal:
        if random.uniform(0,1)<exploration_rate:
            action=random.choice(env.actions)
        else:
            action_index=np.argmax(Q_table[env.state[0],env.state[1]])
            action=env.actions[action_index]

        next_state=env.next_state(action)
        reward=env.reward(next_state)
        action_index=env.actions.index(action)

        Q_table[env.state[0],env.state[1],action_index]+=learning_rate*(reward+discount_rate*np.max(Q_table[next_state[0],next_state[1]])-Q_table[env.state[0],env.state[1],action_index])
        env.board[env.state[0]][env.state[1]]=" . "
        env.state=next_state
        if env.state==env.goal:
            sleep(1)
            print("goal state is reached at episode: {}".format(episode))
        env.board[env.state[0]][env.state[1]]="A"
        env.render()
        sleep(0.5)


