# 1.Question: You toss a dice 100 time: (1)if 1,2 >> step-1 (2)elif 3,4,5 >> step + 1 (3) else 6 >>step + toss the dice again
# 2.Limitation:(1) can't go below; (2) 0.1% chance of falling down the stairs; 
# 3.Solve:the probabillity you'll reach step 60
# Import numpy and set seed
import numpy as np
np.random.seed(123)
# Initialize all_walks
all_walks = []
# Simulate random walk 10 times
for i in range(500):
    # Initialization
    random_walk = [0]
      #Simulate toss a dice 100 time:
    for x in range(100) :
        step = random_walk[-1]
        # Use randint() to simulate a dice
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1) #Limitation(1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)
    # Append random_walk to all_walks
    all_walks.append(random_walk)
# Print all_walks
print(all_walks)
# plot all walks
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()
#Plot the distribution
ends = np_aw_t[-1,:]
plt.hist(ends)
plt.show()
#Calculate the odds
np.mean(ends>=60)
