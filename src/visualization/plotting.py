import matplotlib.pyplot as plt
import numpy as np

def image_plotting(list_of_images:list):
    num_images=len(list_of_images)
    fig, ax = plt.subplots(1,num_images)
    for img_ind, image in enumerate(list_of_images):
        ax[img_ind].imshow(image)


def display_images_torch_grid(original, patches, patch_size):
    image_width = int(np.sqrt(len(patches)))
    fig, ax = plt.subplots(image_width, image_width, figsize=(10,5))
    for i in range(len(patches)):
        r=int(i // image_width)
        c= int(i % image_width)
        ax[r,c].imshow(patches[i].numpy(), cmap='gray')
        ax[r,c].set_xticklabels([])
        ax[r,c].set_yticklabels([])
    plt.subplots_adjust(wspace=-.7, hspace=0.1)
    plt.show()