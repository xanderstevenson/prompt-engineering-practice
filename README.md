# Prompt Engineering Practice

This repository provides a simple Flask web app to practice crafting effective prompts for a network engineering assistant (LeChat / Mistral). Users will interact with the agent and receive feedback on prompt clarity and actionability.

<br>

<p align="center">
  <img src="https://github.com/xanderstevenson/prompt-engineering-practice/blob/main/media/prompt-practice-1.png" width="450px">
  <img src="https://github.com/xanderstevenson/prompt-engineering-practice/blob/main/media/prompt-practice-2.png" width="450px">
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
- Mistral Agent ID



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

> **Note:** How to obtain a Mistral AI API Key
> 1.  **Create a Mistral AI Account**: Go to [Mistral AI](https://mistral.ai/) and sign up for an account. Create an Organization. Set up Multi-Factor Authentication (MFA) for enhanced security.
> 2.  **Generate an API Key**: Navigate to the Mistral dashboard console (La Platforme). Go to `API Keys` and click "Create New Key". Copy the generated API key.

- Detailed instructions on how to sign up for Mistral and obtain an API key are found in this [PDF](https://www.ciscolive.com/c/dam/r/ciscolive/global-event/docs/2025/pdf/CISCOU-1060.pdf) from a Cisco Live session regarding Mistral APIs.

```
export MISTRAL_API_KEY="YOUR_MISTRAL_API_KEY"  # Mac
```
or
```
$env:MISTRAL_API_KEY="YOUR_MISTRAL_API_KEY"    # Windows
```

### 5. Create the Mistral Agent

- From the [Agents](https://console.mistral.ai/build/agents) tab in Mistral's La Platforme, click `Create new Agent'.
- Name it, select a model, select the Randomness and enter Instructions / System prompt with details on how the agent should converse regarding prompts. [Here](https://github.com/xanderstevenson/prompt-engineering-practice/blob/main/media/example-system-prompt.txt) is and example system prompt for prompt engineering.
- Click `Deploy` and copy the Agent ID near the top of the page.

> **Note:** If you select "Le Chat", a URL for an in-browser chat assistant trained on your system prompt will be generated as well.


### 4. Set Mistral Agent ID

```
export MISTRAL_AGENT_ID="YOUR_MISTRAL_AGENT_ID"  # Mac
```
or
```
$env:MISTRAL_AGENT_ID="YOUR_MISTRAL_AGENT_ID"    # Windows
```


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
 
