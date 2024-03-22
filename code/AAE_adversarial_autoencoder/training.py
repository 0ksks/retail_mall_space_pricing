from torch.utils.data import DataLoader
from pytorch_lightning import Trainer,loggers
from typing import Literal
def get_dataloader(dataset, batch_size, shuffle=True):
    return DataLoader(dataset=dataset, batch_size=batch_size, shuffle=shuffle, num_workers=3, persistent_workers=True)
def train_unit(layers,max_epochs,type:Literal["tri","rec"],hiddenDim=None,lr=1e-3):
    from autoencoder import Autoencoder
    model = Autoencoder(6,2,layers,type,lr,hiddenDim)
    save_dir = "code/AAE_adversarial_autoencoder"
    trainer = Trainer(max_epochs=max_epochs,  log_every_n_steps=10, logger=loggers.TensorBoardLogger(save_dir=save_dir,version=f"(lay,hid)=({layers},{hiddenDim})"))
    trainer.fit(model, dataloader)
if __name__ == "__main__":
    from datasets import AEDataset
    batch_size = 1000
    max_epochs = 60
    dataloader = get_dataloader(AEDataset('norm'),batch_size)
    # best (6,6)
    for layers in range(2,6):
        for hiddenDim in range(2,6):
            train_unit(layers,max_epochs,'rec',hiddenDim)
    
    
'''
tensorboard --logdir=code/AAE_adversarial_autoencoder/lightning_logs
'''
