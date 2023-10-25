import matplotlib.pyplot as plt
import torch

class Trainer:
    def __init__(self, model, optimizer, criterion, train_data, num_epoch):
        self.model = model
        self.optimizer = optimizer
        self.criterion = criterion
        self.data = train_data
        self.num_epoch = num_epoch
        self.train_loss=[]
        self.val_loss=[]

    def run(self, verbose=0):
        batch_size = self.data.batch_size
        for epoch in range(0,self.num_epoch):
            for batch_id, (x, y) in enumerate(self.data):
                y_pred = self.model(x)
                loss = self.criterion(y_pred, y)
                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()
                self.train_loss.append(loss.item())
            if verbose>0: print(f"epoch {epoch} is ended: train loss {torch.mean(torch.Tensor(self.train_loss))}")
    def plot_error(self):
        plt.plot(range(len(self.train_loss)),self.train_loss,label='trainig_error')
        plt.plot(range(len(self.val_loss)),self.val_loss, label='validation error')
        plt.legend()