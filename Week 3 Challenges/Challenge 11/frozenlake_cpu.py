import gym
import numpy as np
import random

env = gym.make('FrozenLake-v1', is_slippery=False)
state_size = env.observation_space.n
action_size = env.action_space.n

Q = np.zeros((state_size, action_size))

episodes = 10000
learning_rate = 0.8
discount_rate = 0.95
epsilon = 1.0
min_epsilon = 0.01
decay_rate = 0.001

for episode in range(episodes):
    state = env.reset()[0]
    done = False

    while not done:
        if random.uniform(0, 1) < epsilon:
            action = env.action_space.sample()
        else:
            action = np.argmax(Q[state])

        next_state, reward, done, _, _ = env.step(action)

        old_value = Q[state, action]
        next_max = np.max(Q[next_state])

        new_value = (1 - learning_rate) * old_value + learning_rate * (reward + discount_rate * next_max)
        Q[state, action] = new_value

        state = next_state

    epsilon = min_epsilon + (1.0 - min_epsilon) * np.exp(-decay_rate * episode)
