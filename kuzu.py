

from __future__ import print_function
import torch
import torch.nn as nn
import torch.nn.functional as F

class NetLin(nn.Module):
    # linear function followed by log_softmax
    def __init__(self):
        super(NetLin, self).__init__()
        self.lin_layer = nn.Linear(28*28, 10)

    def forward(self, x):
        x = x.view(x.shape[0], -1)
        x = self.lin_layer(x)
        x = F.log_softmax(x, dim=1)
        return x

class NetFull(nn.Module):
    # two fully connected tanh layers followed by log softmax
    def __init__(self):
        super(NetFull, self).__init__()
        self.fc1 = nn.Linear(784, 256)
        self.fc2 = nn.Linear(256, 10)
        
    def forward(self, x):
        x = x.view(shape[0], -1)
        x = torch.tanh(self.fc1(x))
        x = self.fc2(x)
        x = torch.log_softmax(x, dim=1)
        return x

class NetConv(nn.Module):
    # two convolutional layers and one fully connected layer,
    # all using relu, followed by log_softmax
    def __init__(self):
        super(NetConv, self).__init__()
        self.conv1=nn.Conv2d(in_channels = 1, out_channels = 64, karnel_size = 5, padding=2)
        self.max_pool=nn.MaxPool2d(2,2)
        self.conv2=nn.Conv2d(in_channels = 64, out_channels = 24, kernel_size = 5, padding=2)
        self.fc1=nn.Linear(1176,159)
        self.fc2=nn.Linear(159,10)
        
    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = self.max_pool(x)
        x = F.relu(self.conv2(x))
        x = self.max_pool(x)
        x = x.view(x.size(0), -1)
        x = F.relu(self.fc1(x))
        x = self.fc2(x)
        x = F.log_softmax(x, dim=1)
        return x
