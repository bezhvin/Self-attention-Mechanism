import torch
import torchvision.datasets as dataset
import torchvision.transforms as transforms
import os
import copy
import numpy as np
def image_flatten(x):
    return  x.flatten(start_dim=1)


class MNIST:
    def __init__(self, root:str='./data/mnist', flatten=False):
        if not os.path.isdir(root):
            os.makedirs(root)
        if flatten:
            transform = transforms.Compose([transforms.ToTensor(), transforms.Lambda(image_flatten)])
        else:
            transform = transforms.Compose([transforms.ToTensor()])
        self.train_set = dataset.MNIST(root=root, train=True, transform=transform, download=True)
        self.test_set = dataset.MNIST(root=root, train=False, transform=transform, download=True)

    def subset_traindata(self, labels:list):
        targets = self.train_set.targets
        indeces = [i for i in range(len(targets)) if targets[i] in labels]
        train_subset = copy.deepcopy(torch.utils.data.Subset(self.train_set, indeces))
        for i, label in enumerate(labels):
            train_subset.dataset.targets[train_subset.dataset.targets == label]=i
            
        return train_subset


def image_patching(image, num_patch=16):
    num_dim = image.dim()
    for _ in range(4-num_dim):
        image = image.unsqueeze(dim=0)
    _,_, w, h = image.shape
    patch_size = int(w//(np.sqrt(num_patch)))
    stride=patch_size
    unfolded = torch.nn.functional.unfold(image.to(torch.float), patch_size, stride=stride)
    unfolded = unfolded.permute(0, 2, 1).reshape(-1, patch_size, patch_size)
    return unfolded, patch_size