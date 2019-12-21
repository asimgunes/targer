"""creates various optimizers"""
import torch.optim as optim
from torch.optim.lr_scheduler import LambdaLR
from src.layers.layer_word_embeddings import LayerWordEmbeddings
from src.layers.layer_context_word_embeddings import LayerContextWordEmbeddings

class EmbeddingsFactory():
    """OptimizerFactory contains wrappers to create various optimizers."""
    @staticmethod
    def create(emb_type, word_seq_indexer, gpu, freeze_word_embeddings):
        if emb_type == 'elmo':
            return LayerContextWordEmbeddings(word_seq_indexer, gpu, freeze_word_embeddings)
        return LayerWordEmbeddings(word_seq_indexer, gpu, freeze_word_embeddings)
