
import torch
import torch.nn.functional as F

X = torch.tensor([[1, 2, 0, 1], [0, 1, 3, 2], [2, 0, 1, 0], [1, 1, 2, 1]], dtype=torch.float32)
W = torch.tensor([[1, 0, -1], [1, 0, -1], [1, 0, -1]], dtype=torch.float32)
Y = F.conv2d(X.unsqueeze(0).unsqueeze(0), W.unsqueeze(0).unsqueeze(0), padding=1, stride=2)
print(Y.squeeze().numpy())
# [[-3.  0.]
#  [-2. -1.]]
              