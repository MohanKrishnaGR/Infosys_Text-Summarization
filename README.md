# Infosy_Text-Summarization
## Data Collection
Merged selective dataset from 
- CNN, Daily Mail : News, 
- BillSum: Legal, 
- ArXiv : Scientific
- Dialoguesum 
## Model Training & validation
Implemented in model.ipynb .
Retraining the pre-trained transformer model with our derived dataset. Native pytorch method is utilized, rather than using training pipeline API, to get more control of model training and its parameters.

Outlay:
- Setup & initialization
- training loop
- Evaluation loop

Average training loss: 1.3280
Average validation loss: 2.4502 

saved_model:
.
└── fine_tuned_bart

    ├── config.json

    ├── generation_config.json

    ├── merges.txt

    ├── model.safetensors

    ├── special_tokens_map.json

    ├── tokenizer_config copy.json

    ├── tokenizer_config.json
    
    └── vocab.json
 
## Model Validation (Custom)
Performance metrics - ROUGE (Recall-Oriented Understudy for Gisting Evaluation) is best suited to evaluate the model's performance for 'Text Summarizer'.

Aimed to implement a custom evaluation function that calculate ROGUE based on model's inference.