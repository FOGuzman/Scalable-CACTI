import os
import scipy.io
import torch
import cv2


def save_as_mat(tensor, file_name):
    device = tensor.device
    if device.type == 'cuda':
            tensor=tensor.cpu()
    scipy.io.savemat(file_name, {"tensor": tensor.numpy()})

def save_as_torch(tensor, file_name):
    device = tensor.device
    if device.type == 'cuda':
            tensor=tensor.cpu()
    torch.save(tensor, file_name)

def save_as_mp4(tensor, file_name):
    device = tensor.device
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    height, width = tensor.shape[-2:]
    video_writer = cv2.VideoWriter(file_name, fourcc, 2, (width, height))

    for frame in tensor:
        if device.type == 'cuda':
            frame=frame.cpu()

        frame = (frame * 255).byte().numpy()
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        video_writer.write(frame)

    video_writer.release()