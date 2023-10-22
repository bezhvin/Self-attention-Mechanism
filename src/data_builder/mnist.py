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

def get_subset_data(data, labels:list):
    small_dataset_idx=[]
    for label in labels:
        small_dataset_idx.append(data.targets == label)
    small_data_x = data.data[small_dataset_idx].to(torch.float64)
    small_data_y = data.targets[small_dataset_idx].long()
    small_train_y[small_train_y==class1_label]=0
    small_train_y[small_train_y==class2_label]=1