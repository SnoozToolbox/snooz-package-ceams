import torch
from pathlib import Path
from typing import Union

import sys, os
# Get the directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))

# Add the parent directory to the Python path
sys.path.append(current_dir)
from sumo.model import SUMO


def get_model(path: Union[str, Path], config):
    path = Path(path)

    model_file = path # modified by me
    # model_file = current_dir + '/final.ckpt'  # added by me
    gpu = torch.cuda.is_available()  # added by me

    if gpu:
        model_checkpoint = torch.load(model_file)
    else:
        model_checkpoint = torch.load(model_file, map_location='cpu')

    model = SUMO(config)
    model.load_state_dict(model_checkpoint['state_dict'])

    return model