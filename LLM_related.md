## Ollama with qwen3-coder
- Download install.sh
- Edit the OLLAMA_INSTALL_DIR into local SW folder
- Run the script to install
- export OLLAMA_MODELS=/..../ollama/models
- If OLLAMA_MODELS is not defined, ~/.ollama/models will be used
- terminal 1: ollama serve
- terminal 2: ollama run qwen3-coder
  - This will download the model and run

## vs code coupling with ollama+qwen2.5-coder
- Qwen3.0-coder is not supported yet (Aug 2025)
- install continue.vsix for vscode
- make sure OLLAM_MODELS is defined if the models are located in non-default location
- terminal 1: ollama serve
- terminal 2: ollama list # make sure if models are detected
- edit ~/.continue/config.yaml
```
models:
  - name: Qwen2.5-Coder
    provider: ollama
    model: qwen2.5-coder:latest
```
- Re-run vscode to load continue package
