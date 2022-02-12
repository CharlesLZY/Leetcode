'''
### Reservoir Sampling
Given a data stream, how to pick m numbers with equal probability P = m/N in O(N) time complexity and O(m) space complexity.


P(data[i] is finally picked) = P(data[i] can enter reservoir) * P(data[i] will not be replaced by data[i+1:])
P(i) = p(i) * R(i,N)


initialize reservoir with data[:m]

when i <= m : p(i) = 1   
when i  > m : p(i) = m/i


For the numbers in reservoir, when i = m+1, the probability it will be replaced is p(i) * 1/m = m/(m+1) * 1/m = 1/(m+1).
So the probability of not being replaced is 1 - 1/(m+1) = m/(m+1)

For the numbers in reservoir, when i = m+2, the probability it will be replaced is p(i) * 1/m = m/(m+2) * 1/m = 1/(m+2).
So the probability of not being replaced is 1 - 1/(m+2) = (m+1)/(m+2)
And the cumulative probability of not being replaced is m/(m+1) * (m+1)/(m+2)

For the number m+1, when i = m+2, the probability it will be replaced is p(i) * 1/m = m/(m+2) * 1/m = 1/(m+2).
So the probability of not being replaced is 1 - 1/(m+2) = (m+1)/(m+2)

We can find that:
for i <= m, R(i, N) = m/(m+1) * (m+1)/(m+2) * ... * (N-1)/N = m/N
for i  > m, R(i, N) = i/(i+1) * (i+1)/(i+2) * ... * (N-1)/N = i/N
when i <= m : R(i, N) =  m / N   P(i) = p(i) * R(i,N) =   1 * m/N = m/N
when i  > m : R(i, N) =  i / N   P(i) = p(i) * R(i,N) = m/i * i/N = m/N



e.g. when m = 1
If we have a total of n numbers and we pick the ith number, this implies that we do not pick any number further from index i+1 to n.
P(1) = 1 * (1-1/2) * (1-1/3) * (1-1/4) * ... * (1-1/N) = 1/N
P(2) = 1/2 * (1-1/3) * (1-1/4) * ... * (1-1/N) = 1/N
P(3) = 1/3 * (1-1/4) * ... * (1-1/N) = 1/N
P(4) = 1/4 * ... * (1-1/N) = 1/N
...
P(N) = 1/N

'''
'''
蓄水池算法关键在于维护一个蓄水池，每次遇到新的候选人，有概率选中，蓄水池中的元素则有概率被替换
'''
import random
def reservoirSampling(data, m):
	reservoir = data[:m]
	for i in range(m, len(data)):
		r = random.randint(0, i)
		if r < m:
			reservoir[r] = data[i]
	return reservoir