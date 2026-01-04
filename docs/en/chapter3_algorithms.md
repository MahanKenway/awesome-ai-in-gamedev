# Chapter 3: AI Techniques and Algorithms in Games

In this chapter, we delve into the most technical aspects of game AI.

## 3.1 Finite State Machines (FSM)
The most basic and oldest technique. In this method, an NPC is in a specific "state" at any given moment and transitions to another state based on inputs.
- **Example**: A zombie is in the **Idle** state. If it sees the player, it transitions to the **Chase** state, and if it reaches the player, it moves to the **Attack** state.

## 3.2 Behavior Trees
A tree structure that breaks down decision-making into small, modular parts.
- **Components**: Selector nodes, Sequence nodes, and Leaf nodes.
- **Advantage**: Much more scalable than FSM and allows for easy management of complex behaviors.

## 3.3 Goal-Oriented Action Planning (GOAP)
A method where instead of writing all the steps, we only give the NPC a "goal" and "possible actions."
- **How it works**: The NPC checks which actions can lead to the goal and chooses the best path.
- **Utility AI**: The NPC selects the best action in the moment based on the weight and value of each action.

## 3.4 Pathfinding Algorithms
- **A* Algorithm**: The most popular method. It uses the formula `f(n) = g(n) + h(n)` to find the shortest and most optimal path.
- **Dijkstra**: Similar to A* but without a heuristic estimation, making it more accurate for weighted graphs but slower.
- **Flow Field**: Suitable for managing the movement of large crowds (Crowd Simulation).

## 3.5 Reinforcement Learning
A method where an intelligent agent learns the best strategy through trial and error and receiving rewards or penalties.
- **AlphaGo Zero**: An example that reached mastery without any human data, only by playing against itself.
