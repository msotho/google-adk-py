# Google Python ADK

## Requirements

- Python 3.13+
- uv package manager
- M-series MacOS with 16GB of RAM or more

## Getting started

1. Clone the repository:
   ```bash
   git clone https://github.com/msotho/google-adk-py.git
    ```

2. Create a virtual environment and activate it:
   ```bash
   cd google-adk-py
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Set Hugging Face access token as an environment variable:
   ```bash
   export HF_TOKEN="<your_hugging_face_access_token>"
   ```
   Get your access token from [Hugging Face settings](https://huggingface.co/settings/tokens).

4. Install the required dependencies:
   ```bash
   uv sync
   ```

5. Run mlx inference to test the installation:
   ```bash
   mlx_vlm.generate --model mlx-community/gemma-4-12B-it-OptiQ-4bit --max-tokens 100 --temperature 0.0 --prompt "What is your name?"
   ```
   This will download the Google Gemma 4 12B model and run inference on it. You should see the output of the model in
   the terminal. Model information is available
   at [Hugging Face](https://huggingface.co/mlx-community/gemma-4-12B-it-OptiQ-4bit).

## Start the MLX LM server

   ```bash
   mlx_vlm.server --model mlx-community/gemma-4-12B-it-OptiQ-4bit --port 8080
   ```

## Open another terminal and start the Google ADK Web

   ```bash
   source .venv/bin/activate
   adk web
   ```