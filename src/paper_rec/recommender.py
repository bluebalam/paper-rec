import torch
import torch.nn as nn
import numpy as np
import json

from sentence_transformers import SentenceTransformer
from huggingface_hub import hf_hub_download

REC_MODEL_HF_REPO_ID = "bluebalam/paper-rec"
REC_MODEL_STATE_DICT = "paper-rec-model.pth"
REC_PAPERS_DATA = "papers.jsonl"
LANG_MODEL = 'sentence-transformers/all-MiniLM-L6-v2'
EMBEDDING_DIM = 384


class Recommender:
    def __init__(self):
        super().__init__()
        self.papers = None
        self.model = None

    class MF(torch.nn.Module):
        def __init__(self, item_content_embeddings):
            super().__init__()
            self.item_embeddings = nn.Embedding.from_pretrained(item_content_embeddings)

        def forward(self, user_embedding, item):
            return (user_embedding * self.item_embeddings(item)).sum(1)

    def encode(self, sentences):
        lang_model = SentenceTransformer(LANG_MODEL)
        return lang_model.encode(sentences)

    def embedding(self, sentences):
        embs = self.encode(sentences)
        return np.mean(embs, axis=0)

    def load_data(self):
        # the papers
        papers = []
        papers_data_path = hf_hub_download(repo_id=REC_MODEL_HF_REPO_ID, filename=REC_PAPERS_DATA)
        with open(papers_data_path) as fin:
            for l in fin:
                papers.append(json.loads(l))
        self.papers = papers

    def load_model(self):
        n_papers = len(self.papers)
        # the model
        state_dict_path = hf_hub_download(repo_id=REC_MODEL_HF_REPO_ID, filename=REC_MODEL_STATE_DICT)
        model = self.MF(torch.rand(n_papers, EMBEDDING_DIM))
        model.load_state_dict(torch.load(state_dict_path))
        model.eval()
        self.model = model

    def recommend(self, user_embedding, top_k=10):
        scores = self.model(user_embedding, torch.LongTensor(range(len(self.papers))))
        preds = torch.topk(scores, top_k)
        indices = preds.indices.numpy()
        recs = [self.papers[i] for i in indices]
        return recs

