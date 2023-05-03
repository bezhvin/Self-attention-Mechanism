import matplotlib.pyplot as plt

def image_plotting(list_of_images:list):
    num_images=len(list_of_images)
    fig, ax = plt.subplots(1,num_images)
    for img_ind, image in enumerate(list_of_images):
        ax[img_ind].imshow(image)
