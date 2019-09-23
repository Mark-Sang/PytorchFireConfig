import warnings
import torch

class DefaultConfig():
    Text = "config test"
    Text2 = "number2 test"
    Text3 = "number3 test"

    def parse(self, kwargs):                                    #根据字典更新config参数，便于命令行更改参数
        for k,v in kwargs.items():                              #更新配置参数
            if not hasattr(self, k):
                warnings.warn("Warning:设置文件里没这个参数")
            setattr(self, k, v) 
            
        print("user config:")
        for k,v in self.__class__.__dict__.items():
            if (not k.startswith('__') and not k.startswith('p')):                
                print(k,getattr(self, k))
        print('\n''\n')