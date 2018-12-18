import gym

env = gym.make('Taxi-v2')

state = env.reset()

env.render()

#--------------------------------------------------------------------------------------------------------------

cnt=1
reward=0

while(reward!=20):
    action=env.action_space.sample()
    state, reward, done, info = env.step(action)
    #env.render()
    cnt+=1

print("Needed " + str(cnt) + " moves to reach the final stage, ")

#--------------------------------------------------------------------------------------------------------------

import numpy as np

Q=np.zeros([500,6])

gamma=0.8
env.render()

env = gym.make('Taxi-v2')

for episode in range(1,1000):
    state = env.reset()
    #env.render()
    cnt = 1
    reward = 0
    while reward != 20:
        action = np.argmax(Q[state])
        state2, reward, done, info = env.step(action)
        Q[state, action] = reward + gamma*np.max(Q[state2])
        state = state2
        cnt+=1

    if episode%50==0:
        print("Needed " + str(cnt) + " moves to reach the final stage. " + str(episode))

#-----------------------------------------------------------------------------------------------------------

import gym
env = gym.make('CartPole-v0')
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())


import gym
env = gym.make('Pendulum-v0')
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())
   

import gym
env = gym.make('Acrobot-v1')
env.reset()
for _ in range(1000):
    env.render()
    env.step(env.action_space.sample())
