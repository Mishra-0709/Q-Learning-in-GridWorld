import numpy as np
import random

# GridWorld environment
grid_size = 5
goal_state = (4, 4)
actions = ['up', 'down', 'left', 'right']
q_table = np.zeros((grid_size, grid_size, len(actions)))
alpha = 0.1
gamma = 0.9
epsilon = 0.2
episodes = 500

def get_next_state(state, action):
    x, y = state
    if action == 'up' and x > 0: x -= 1
    elif action == 'down' and x < grid_size-1: x += 1
    elif action == 'left' and y > 0: y -= 1
    elif action == 'right' and y < grid_size-1: y += 1
    return (x, y)

def get_reward(state):
    return 10 if state == goal_state else -1

for ep in range(episodes):
    state = (0, 0)
    while state != goal_state:
        if random.uniform(0,1) < epsilon:
            action_index = random.randint(0,3)
        else:
            action_index = np.argmax(q_table[state[0], state[1]])

        next_state = get_next_state(state, actions[action_index])
        reward = get_reward(next_state)
        next_max = np.max(q_table[next_state[0], next_state[1]])

        q_table[state[0], state[1], action_index] += alpha * (reward + gamma * next_max - q_table[state[0], state[1], action_index])
        state = next_state

print("Training completed. Q-Table:")
print(q_table)
