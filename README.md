# Infosy_Text-Summarization
## Data Collection
Merged selective dataset from 
- CNN, Daily Mail : News, 
- BillSum: Legal, 
- ArXiv : Scientific
- Dialoguesum 
## Model Train & validation
Implemented in model.ipynb .
Retraining the pre-trained transformer model with our derived dataset. Native pytorch method is utilized, rather than using training pipeline API, to get more control of model training and its parameters.

Outlay:
- Setup & initialization
- training loop
- Evaluation loop