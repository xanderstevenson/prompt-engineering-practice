# Prompt Engineering Practice

This repository provides a simple Flask web app to practice crafting effective prompts for a network engineering assistant (LeChat / Mistral). Users will interact with the agent and receive feedback on prompt clarity and actionability.


<p align="center">
  <img src="https://github.com/xanderstevenson/prompt-engineering-practice/blob/main/media/prompt-practice-1.png" width="500px">
  <img src="https://github.com/xanderstevenson/prompt-engineering-practice/blob/main/media/prompt-practice-2.png" width="500px">
</p>


---



## Usage

- Open the web app in your browser.

- Type a message or prompt in the input box.

- Interact with the agent and get feedback on your prompt engineering skills.

- Follow the on-screen instructions for each scenario.


## Requirements

- Python 3.13+
- Mac / Windows / Linux PC
- Mistral AI API Key (from [Mistral AI](https://mistral.ai/))



### Notes

- Ensure your .env or API keys are never committed to Git.

  

## Getting Started

Follow these steps to set up the project locally.


### 1. Clone the Repository
```bash
git clone https://github.com/xanderstevenson/prompt-engineering-practice.git
cd prompt-engineering-practice
```

### 2. Set up the Virtual Environment

```
python3 -m venv venv
```
```
source venv/bin/activate   # On macOS / Linux
```
or
```
venv\Scripts\activate      # On Windows
```

### 3. Install Requirements
```
pip install -r requirements.txt
```

### 4. Set Mistral API Key
```
export MISTRAL_API_KEY="YOUR_MISTRAL_API_KEY"  # Mac
```
or
```
$env:MISTRAL_API_KEY="YOUR_MISTRAL_API_KEY"    # Windows
```

> **Note:** Obtain a Mistral AI API Key
> 1.  *Create a Mistral AI Account*: Go to [Mistral AI](https://mistral.ai/) and sign up for an account. Set up Multi-Factor Authentication (MFA) for enhanced security.
> 2.  *Generate an API Key*: Navigate to the Mistral Console. Go to `API Keys` and click "Create New Key". Copy the generated API key.

### Run the Flask App

```
python app.py
```
 
### File Structure

```
.
├── app.py
├── requirements.txt
├── static
│   └── style.css
├── templates
│   └── index.html
└── venv
    ├── bin
    ├── include
    ├── lib
    └── pyvenv.cfg
```
 
