# STEM-MATE

This repository contains the code for a STEM Chat Bot application that leverages a fine-tuned Llama 2 language model, optimized using the PEFT LoRA technique. The model is designed to assist with complex mathematical, scientific, and engineering questions, making it a valuable tool for STEM students and professionals.

## Project Overview

The project includes:
- A **Jupyter Notebook** for fine-tuning the Llama 2 model using the AutoTrain library, which can be easily adapted for your own datasets and models.
- Integration of the model with a **Streamlit** web application to provide a seamless conversational interface.
- Model and token management via **Hugging Face**, allowing access to the model for further use.

## Dataset

The model was fine-tuned on a specialized STEM dataset, which can be accessed via Hugging Face. **Note:** You will need a Hugging Face token to access this dataset via the jupyter notebook.

**Dataset Link**: [https://huggingface.co/garage-bAInd/Platypus2-7B]

You can obtain a Hugging Face token by signing up for an account on Hugging Face:  
[Hugging Face Sign-Up](https://huggingface.co/join)

## Fine-tuning

Follow the LLM autotrain notebook and fine-tune the model. The model will be automatically pushed to your hugging face repo upon successful completion.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/YourUsername/STEM-Chat-Bot.git
   cd STEM-Chat-Bot
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
3. Ensure you have a Hugging Face token for authentication to access your fine-tuned model on Huggingface and add it to a .env file.
4. Run the app
   ```bash
   streamlit run app.py

