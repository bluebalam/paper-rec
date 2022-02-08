# paper-rec

What paper in ML/AI should I read next? It is difficult to choose from all great research publications published daily. This demo gives you a personalized selection of papers from the latest scientific contributions available in [arXiv](https://arxiv.org/).
You just input the title or abstract (or both) of paper(s) you liked in the past or you can also use keywords of topics of interest and get the top-10 article recommendations tailored to your taste.

Enjoy!

## Demo
Demo using Hugging Face spaces: https://huggingface.co/spaces/bluebalam/paper-rec

## Model
Model that can be loaded and used directly by `paper-rec` can be found here: https://huggingface.co/bluebalam/paper-rec

## Model Card

Last updated: 2022-02-04

## Model Details
`paper-rec` goal is to recommend users what scientific papers to read next based on their preferences. This is a test model used to explore Hugging Face Hub capabilities and identify requirements to enable support for recommendation task in the ecosystem. 

### Model date
2022-02-04

### Model type
Recommender System model with support of a Language Model for feature extraction.

### Paper & samples
The overall idea for `paper-rec` test model is inspired by this work: [NU:BRIEF – A Privacy-aware Newsletter Personalization Engine for Publishers](https://arxiv.org/abs/2109.03955).

However, for `paper-rec`, we use a different language model more suitable for longer text, namely *Sentence Transformers*: [Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks](https://arxiv.org/abs/1908.10084), in particular: [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2).

## Model Use
The intended direct users are recommender systems' practitioners and enthusiasts that would like to experiment with the task of scientific paper recommendation.

## Data, Performance, and Limitations
### Data 
The data used for this model corresponds to the [RSS news feeds for arXiv updates](https://arxiv.org/help/rss) accessed on 2022-02-04. In particular to the ones related to Machine Learning and AI:

1. [Artificial Intelligence](http://arxiv.org/rss/cs.AI)
1. [Computation and Language](http://arxiv.org/rss/cs.CL)
1. [Computer Vision and Pattern Recognition](http://arxiv.org/rss/cs.CV)
1. [Information Retrieval](http://arxiv.org/rss/cs.IR)
1. [Machine Learning (cs)](http://arxiv.org/rss/cs.LG)
1. [Machine Learning (stat)](http://arxiv.org/rss/stat.ML)

### Performance 
N/A

## Limitations
The model is limited to the papers fetched on 2022-02-04, that is, those papers are the only ones it can recommend.
