#!/usr/bin/env python
# coding: utf-8

# In[7]:


# uniform cost function
# returns the minimum cost (Bonus: returns path to minimum cost as well)
from queue import PriorityQueue
def  uniform_cost_search(start, goal, graph, cost):
    answer = {node: {'cost': float('inf'), 'path': []} for node in goal}
    openQueue = PriorityQueue()
    openQueue.put((0,start,[start]))
    closedQueue = set()   
    
    while not openQueue.empty():
       current_cost, current_node, path =  openQueue.get()
    
       if current_node in closedQueue :
            continue 
       closedQueue.add(current_node)
       if current_node in goal and current_cost < answer[current_node]['cost']:
          answer[current_node] = {'cost': current_cost, 'path': path}

       for child in graph[current_node]:
            if child not in closedQueue:
                new_cost = current_cost + cost.get((current_node, child), float('inf'))
                openQueue.put((new_cost, child, path + [child]))        
            
    return answer
 
# main function
if __name__ == '__main__':
     
    # create a graph with no more than 30 nodes
    graph, cost = [[] for i in range(30)], {}
 
    # add edges to the graph
    graph[0].append(4)
    graph[0].append(5)
    graph[0].append(16)
    graph[2].append(1)
    graph[3].append(1)
    graph[4].append(2)
    graph[4].append(3)
    graph[4].append(5)
    graph[5].append(8)
    graph[5].append(18)
    graph[6].append(3)
    graph[6].append(7)
    graph[8].append(16)
    graph[8].append(17)
    graph[16].append(17)
    graph[18].append(6)
    
 
    # add cost to each edge
    cost[(0, 4)] = 3
    cost[(0, 5)] = 9
    cost[(0, 16)] = 1
    cost[(2, 1)] = 2
    cost[(3, 1)] = 2
    cost[(4, 2)] = 1
    cost[(4, 3)] = 8
    cost[(4, 5)] = 2
    cost[(5, 8)] = 3
    cost[(5, 18)] = 2
    cost[(6, 3)] = 3
    cost[(6, 7)] = 2
    cost[(8, 16)] = 4
    cost[(8, 17)] = 4
    cost[(16, 17)] = 15
    cost[(18, 6)] = 1
    
    # set start state 
    start = 0
    
    # set goal state, there can be multiple goal states
    goal = [7]
    
    # call uniform_search_cost function to get the minimum cost to reach gaol. Bonus points for path
    # ****** You have to implement this function *****
    min_cost_info = uniform_cost_search(start, goal, graph, cost)

for node in goal:
        info = min_cost_info.get(node, None)
        if info and info['cost'] < float('inf'):
            print(f"Minimum cost from {start} to {node} is {info['cost']}")
            print(f"Path: {' -> '.join(map(str, info['path']))}")
        else:
            print(f"No path found from {start} to {node}.")
      
    #   **** Bonus ****
    #   print(f'Path: {info["path"]}')


# In[ ]:





# In[ ]:




