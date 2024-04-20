import torch
import numpy

class ImagesDataset(torch.utils.data.Dataset):

    def __init__(self, image_dir, width: int = 100, height: int = 100, dtype = None):
        if width < 100 or height < 100:
            raise ValueError("Image size cannot be less than 100x100")
        else:
            pass

    def __getitem__(self, index):
        pass

    def __len__(self):
        pass

#print(torch.__version__)