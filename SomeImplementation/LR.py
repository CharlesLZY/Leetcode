import numpy as np
### feature 1: height feature 2: hair length
### label: gender 1 male 0 female
# x = np.array([[170, 5], 
#               [160, 30], 
#               [175, 3], 
#               [165, 25], 
#               [169, 4], 
#               [162, 35]], dtype=np.float16)

# y = np.array([1,0,1,0,1,0])

# x_train = x[:4, :]
# y_train = y[:4]
# x_test  = x[4:, :]
# y_test  = y[4:]


x = np.random.rand(100, 2)
y = np.random.rand(100)

x_train = x[:75, :]
y_train = y[:75]
x_test  = x[75:, :]
y_test  = y[75:]

def normalize(x): ### 训练集和测试集的normalize要分开来做，否则会引入测试集的信息
    
    X = np.array(x)

    _, k = x.shape
    for i in range(k):
        mu = np.mean(x[:,i])
        delta = np.std(x[:,i])
        X[:,i] = (X[:,i] - mu) / delta

    return X

x_train = normalize(x_train)
x_test = normalize(x_test)

theta = np.random.rand(2,1) ### initialize the parameter and bias
bias = np.random.rand(1)

def sigmoid(z):
    return 1 / (1 + np.exp(-z) )

def h(theta, bias, x):
    return sigmoid(x@theta + bias).reshape(-1)

def CrossEntropy(y_pred, y):
    return np.sum(-y * np.log(y_pred) - (1-y)*np.log(1-y_pred))


epoch = 5
alpha = 0.1


y_pred = h(theta, bias, x_test)


for e in range(epoch):
    N, k = x_train.shape
    for i in range(N):
        theta_copy = np.array(theta)
        for j in range(k):
            theta[j] = theta[j] - alpha * (h(theta_copy, bias, x_train[i,:]) - y_train[i]) * x_train[i,j] 

        bias = bias - alpha * (h(theta_copy, bias, x_train[i,:]) - y_train[i]) * 1


y_pred = h(theta, bias, x_test)


print(CrossEntropy(y_pred, y_test))


import torch
import torch.nn as nn
import torch.optim as optim


x_train = torch.rand(100, 2)
y_train = torch.ones(100, dtype=torch.float32)


x_test = torch.rand(10,2)
y_test = torch.ones(10)

class LR(nn.Module):
    def __init__(self):
        super(LR, self).__init__()
        self.linear = nn.Linear(2,1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        x = self.linear(x)
        return self.sigmoid(x)


model = LR()
criterion = nn.BCELoss()
optimizer = optim.SGD(model.parameters(), lr=1e-2)

epoch = 10
for e in range(epoch):
    y_pred = model(x_train).reshape((-1))
    
    loss = criterion(y_pred, y_train)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    print(loss.item())