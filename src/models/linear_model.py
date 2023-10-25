import torch.nn as nn
import torch.nn.functional as F
import torch



class LinearClassifier(nn.Module):
    def __init__(self, dim, num_output):
        super(LinearClassifier,self).__init__()
        self.linear_model = nn.Linear(dim*dim, num_output, bias=True, dtype=torch.float64)
        
    def forward(self, x):
        logits = self.linear_model(x.to(torch.float64))
        return logits

    def get_parameters(self):
        return self.linear_model.parameters()