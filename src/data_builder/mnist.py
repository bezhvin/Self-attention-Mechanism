import torch
import torchvision.datasets as dataset
import torchvision.transforms as transforms
import os

def get_all_data(root:str='./data/mnist'):
    if not os.path.isdir(root):
        os.makedirs(root)
    Trans = transforms.Compose([transforms.ToTensor()])
    train_set = dataset.MNIST(root=root, train=True, transform=Trans, download=True)
    test_set = dataset.MNIST(root=root, train=False, transform=Trans, download=True)
    return train_set, test_set
