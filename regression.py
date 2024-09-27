import numpy as np
from time import sleep

def regression(train_input,train_output,learning_rate,episodes):

    number_of_sample=len(train_input[0])
    weights=np.array([0 for _ in range(number_of_sample)])
    bias=0

    for episode in range(episodes):
        predicted=np.array([np.dot(weights,np.array(_input))+bias for _input in  train_input ])

        weights_gradaint=np.array([])
        for _input in train_input:
            dw=1/(number_of_sample)*np.dot(np.array(_input),predicted-output_train)
            weights_gradaint.append(dw)

        db=1/(number_of_sample)*np.sum(predicted-train_output)

        weights=weights-learning_rate*weights_gradaint
        bias=bias-learning_rate*db

        if episode%100==0:
            print("episode: {}".format(episode))
            sleep(0.5)


    return weights,bias

# test code for  working with data

input_train=[
    [1,2],
    [4,5],
    [8,9]
]
input_train=np.array(input_train)
output_train=[
    3,
    9,
    17
]
learning_rate=0.1
episodes=1000
weights,bias=regression(input_train,output_train,learning_rate,episodes)

test_input=[
    [1,2],
    [4,5],
    [8,9]
]
test_output=[
    3,
    9,
    17
]
ans=[np.dot(weights,test)+bias for test in test_input]

print(test_output,ans)



