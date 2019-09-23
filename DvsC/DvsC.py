from dataload import DogCat
from config import DefaultConfig
from torchvision.utils import save_image
from torchvision import models
import torch
import os
import fire

opt = DefaultConfig()

def help():
    print('There are help')
    print('It is a test')

def test(**kwargs):
    opt.parse(kwargs)                    #根据命令行参数配置更新
    
    test = DogCat('./test',test=True)
    print('test fire successfully')
    print(opt.Text,'success')
    print(opt.Text2,'success')
    print(opt.Text3,'success')
    print(test.__getitem__(6))

if __name__ == '__main__':
    #imgs = [os.path.join('./test',img) for img in os.listdir('./test')]
    #aaa = imgs[0].split('.')[-2].split('\\')[-1]
    #print(aaa)
    model = models.resnet34(pretrained = True)
    print(model)
    #fire.Fire() 
