
"""class implements word embeddings"""
import torch.nn as nn
import torch
from src.layers.layer_base import LayerBase
from allennlp.modules.elmo import Elmo, batch_to_ids

class LayerContextWordEmbeddings(LayerBase):
    """LayerWordEmbeddings implements word embeddings."""
    def __init__(self, word_seq_indexer, gpu, freeze_word_embeddings=False, pad_idx=0):
        super(LayerContextWordEmbeddings, self).__init__(gpu)
        self.embeddings_dim = 1024
        self.output_dim = 1024
        print("Loading ELMo weights...")
        options_file = "embeddings/newscor.lower.elmo.options.json"
        weight_file = "embeddings/newscor.lower.elmo.weights.hdf5"
        device = torch.device("cuda:"+str(gpu) if (torch.cuda.is_available() and gpu > -1) else "cpu")        
        self.elmo = Elmo(options_file, weight_file, 2, dropout=0)
        self.elmo = self.elmo.to(device) # Using cuda
        print("ELMo weights loaded")


    def is_cuda(self):
        return self.embeddings.weight.is_cuda

    def forward(self, word_sequences):
        #print("Creating ELMo weights...", word_sequences.shape)
        character_ids = batch_to_ids(word_sequences)
        if(self.gpu > -1):
            device = torch.device("cuda:"+str(self.gpu) if (torch.cuda.is_available() and self.gpu > -1) else "cpu")        
            character_ids = character_ids.to(device)
        embeddings = self.elmo(character_ids)
        word_embeddings_feature = embeddings['elmo_representations'][0]
        #print("ELMo weights created")
        return word_embeddings_feature
