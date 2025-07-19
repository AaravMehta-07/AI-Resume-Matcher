@echo off
echo 🔽 Downloading Mistral 7B Instruct (Q5_K_M) Model...

REM Create models folder if it doesn't exist
if not exist "models" (
    mkdir models
)

REM Download model from HuggingFace CDN
curl -L -o "models\mistral-7b-instruct-v0.1.Q5_K_M.gguf" ^
"https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q5_K_M.gguf"

if %errorlevel% neq 0 (
    echo ❌ Download failed. Make sure curl is installed and internet is connected.
    pause
    exit /b 1
)

echo ✅ Download complete! Model saved to: models\mistral-7b-instruct-v0.1.Q5_K_M.gguf
pause
