import torch
import torchvision.datasets as dataset
import torchvision.transforms as transforms
import os

class MNIST:
    def __init__(self, root:str='./data/mnist'):
        if not os.path.isdir(root):
            os.makedirs(root)
        transform = transforms.Compose([transforms.ToTensor()])
        self.train_set = dataset.MNIST(root=root, train=True, transform=transform, download=True)
        self.test_set = dataset.MNIST(root=root, train=False, transform=transform, download=True)

    def subset_traindata(self, labels:list):
        targets = self.train_set.targets
        indeces = [i for i in range(len(targets)) if targets[i] in labels]
        train_subset = torch.utils.data.Subset(self.train_set, indeces)
        return train_subset




def get_all_data(root:str='./data/mnist'):
    if not os.path.isdir(root):
        os.makedirs(root)
    Trans = transforms.Compose([transforms.ToTensor()])
    train_set = dataset.MNIST(root=root, train=True, transform=Trans, download=True)
    test_set = dataset.MNIST(root=root, train=False, transform=Trans, download=True)
    return train_set, test_set

def get_subset_data(data, labels:list):
    small_dataset_idx=[]
    for label in labels:
        small_dataset_idx.append(data.targets == label)
    small_data_x = data.data[small_dataset_idx].to(torch.float64)
    small_data_y = data.targets[small_dataset_idx].long()
    small_train_y[small_train_y==class1_label]=0
    small_train_y[small_train_y==class2_label]=1