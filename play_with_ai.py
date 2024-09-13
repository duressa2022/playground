import numpy as np
import random
class Enviroment:
    def __init__(self,number):
        self.state=number
        self.goal=0
    def next_state(self,cur,action):
        if cur-action<=0:
            return True,cur-action
        return False,cur-action
    def reward(self,state):
        if state<=0:
            return -1
        return 0
    def reset(self,number):
        self.state=number
        return False,self.state
    
learning_rate=0.1
discount_factor=0.8
epsilon=0.2
episodes=2000

number=10
env=Enviroment(number=number)
actions=[1,2,3]
q_table=np.zeros((env.state+1,len(actions)))

for episode in range(episodes):
    done,state=env.reset(number)
    while not done:
        if random.uniform(0,1)<epsilon:
            action=np.random.choice(actions)
        else:
            action_index=np.argmax(q_table[state])
            action=actions[action_index]
        
        done,next_state=env.next_state(state,action)
        reward=env.reward(next_state)
        action_index=actions.index(action)

        max_value=0
        for value in q_table[next_state]:
            max_value=max(value,max_value)

        q_table[state,action_index] += learning_rate * ((reward + discount_factor * max_value) - q_table[state,action_index])

        env.state=next_state
        state=next_state
        print(state)
    print("esiode: {}".format(episode))

print("===================testing the model=================")
# test the model 
current=number
while True==True:
    print("Computer is playing!!!")
    print("current number is: {}".format(current))
    action_index=np.argmax(q_table[current])
    action=actions[action_index]
    current=current-action
    if current<=0:
        print("You win the machine!!")
        break
    print("current number is: {}".format(current))
    number=int(input("Enter your move: "))
    current=current-number
    if number==0 or current<=0:
        print("The machine has won you!!")
        break







