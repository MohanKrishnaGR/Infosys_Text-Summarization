<div align='center'>
    <a href="https://imgbb.com/"><img src="https://i.ibb.co/KyRp80C/springboard-logo.jpg" alt="springboard-logo" border="0" height='80'></a>
</div>

# Infosy_Text-Summarization
## Data Collection
Merged selective dataset from 
- CNN, Daily Mail : News, 
- BillSum: Legal, 
- ArXiv : Scientific,
- Dialoguesum : Conversations.

Robust, multi-objective data.
 
## Models

## Method 1
### -> Native PyTorch
### Model Training

Implemented in model.ipynb .
Retraining the pre-trained transformer model with our derived dataset. Native pytorch method is utilized, rather than using training pipeline API, to get more control of model training and its parameters.

Outlay:
- Setup & initialization
- training loop
- Evaluation loop

Training loss = 1.3280

saved_model - file structure:

```

└── fine_tuned_bart

    ├── config.json

    ├── generation_config.json

    ├── merges.txt

    ├── model.safetensors

    ├── special_tokens_map.json

    ├── tokenizer_config copy.json

    ├── tokenizer_config.json

    └── vocab.json
```
 
### Model Validation (Custom)

Implemented in src/evaluation.ipynb .
Performance metrics - ROUGE (Recall-Oriented Understudy for Gisting Evaluation) is best suited to evaluate the model's performance for 'Text Summarizer'.

Aimed to implement a custom evaluation function that calculate ROGUE based on model's inference.

Even though the model has very minimal training loss but, the model performed inconsistenly in validation & testing phase. There's a suspected tensor error while training using method 1, which could be attributed to the inconsistency of the model's output. 

## Method 2
### -> Trainer Method
### Model Training
Implemented in src/bart.ipynb .
A function was implemented for the dataset, to convert text data into model inputs and targets. Trainer class from transformer package was utilized for training and evaluation. Tainer is a simple but feature-complete training and eval loop for PyTorch, optimized for transformers.

The model was trained with whole dataset for 10 epochs for 26:24:22 (HH:MM:SS) in 125420 steps.

Training Loss = 0.174700

### Model Validation
Implemented in src/rouge.ipynb .
ROUGE score is again used as the performance metric for model evaluation.

Intresting, this model is quite robust in consistent performance with the Rogue1 score as 61.3224, which is a benchmark standard.

## Model Selection for deployment
Considered the performance metrics of the models trained by the forementioned methods.

After the due analysis, the model trained using 'Method 2' was selected.

## Model Deployment
### Testing Interface
Gradio - an open-source Python package that allows us to quickly build a demo - web-application for the trained models.
For the initial phase after model validation, the 'gradio' library is best suited for our objective.

Implemented in src/interface.ipynb .

### Deployment (Ongoing)
Exploring methods in FastAPI and Flask for selecting the suitable one.
Learning about the Docker containerization.

## Extractive Summarization Model (Ongoing)
Working on it.