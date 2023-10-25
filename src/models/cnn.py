import torch.nn as nn
import torch



class CNNClassifier(nn.Module):
    def __init__(self, n_classes):
        super(CNNClassifier, self).__init__()
        self.feature_extractor = nn.Sequential(
        nn.Conv2d(1,10,kernel_size=5),
        nn.MaxPool2d(kernel_size=2),
        nn.ReLU(),
        nn.Conv2d(10,20, kernel_size=5),
        nn.Dropout2d(),
        nn.MaxPool2d(kernel_size=2),
        nn.ReLU()
        )
        
        self.classifier=nn.Sequential(
        nn.Linear(320,50),
        nn.ReLU(),
        nn.Dropout(),
        nn.Linear(50,n_classes)
        )
        
    
    def forward(self,x):
        x = self.feature_extractor(x)
        x = torch.flatten(x,1)
        logits = self.classifier(x)
        return logits