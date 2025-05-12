# 🎮 Q-Learning in GridWorld

This project implements a basic **Q-Learning algorithm** in a custom **GridWorld** environment. It simulates an agent learning to navigate from a start point to a goal using reinforcement learning.

## 🧠 What is Q-Learning?

Q-Learning is a type of **model-free reinforcement learning algorithm**. The agent learns an optimal policy by interacting with an environment and updating a **Q-table**, which stores the expected rewards for taking an action in a given state.

---

## 🧱 GridWorld Setup

- Environment: 5x5 grid
- Start state: (0, 0)
- Goal state: (4, 4)
- Actions: `up`, `down`, `left`, `right`
- Rewards:
  - **+10** for reaching the goal
  - **-1** for each step (to encourage faster solutions)

The agent explores the grid using **ε-greedy policy** and updates its knowledge using the Q-learning formula.

---

## 📈 Algorithm Parameters

- **Learning rate (α)**: 0.1  
- **Discount factor (γ)**: 0.9  
- **Exploration rate (ε)**: 0.2  
- **Episodes**: 500  

![image](https://github.com/user-attachments/assets/1ea9ed1a-29f4-4995-b5cc-115fed05aedc)
