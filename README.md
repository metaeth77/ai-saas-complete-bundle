# AI Meeting Intelligence & Content SaaS Bundle (Production-Ready Backend)

A powerful, production-ready micro-SaaS backend bundle built with Python and FastAPI. This suite helps businesses automate two major workflows: transcribing & summarizing corporate meetings, and instantly turning those summaries into viral social media content.

## 📦 What's Inside the Bundle

### 1. AI Meeting Summarizer (`main.py`)
- **Audio Transcription**: Converts speech from meeting recordings into text via OpenAI Whisper API (`whisper-1`).
- **Smart Summarization**: Extracts key topics, definitive decisions, and actionable tasks with deadlines using Anthropic Claude 3.5 Sonnet.

### 2. AI Social Media Post Generator (`social_uploader.py`)
- **Content Repurposing**: Takes the text summary and automatically creates optimized posts for different social networks.
- **Multi-Platform Focus**: Generates 1 professional LinkedIn post, 2 engaging Twitter/X threads/tweets, and 1 community-focused Telegram post.

## 🛠️ Tech Stack
- Python 3.10+
- FastAPI & Uvicorn
- OpenAI API (Whisper)
- Anthropic API (Claude 3.5 Sonnet)
- Pydantic v2

## 📋 Quick Start Guide

1. **Install all dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set your API Keys (Environment Variables):**
   - **Windows (CMD):**
     ```cmd
     set OPENAI_API_KEY="your-openai-key"
     set ANTHROPIC_API_KEY="your-claude-key"
     ```
   - **Mac/Linux:**
     ```bash
     export OPENAI_API_KEY="your-openai-key"
     export ANTHROPIC_API_KEY="your-claude-key"
     ```

3. **Run the Micro-Services:**
   - Run Meeting Summarizer (Port 8000):
     ```bash
     uvicorn main:app --port 8000 --reload
     ```
   - Run Social Media Generator (Port 8001):
     ```bash
     uvicorn social_uploader:app --port 8001 --reload
     ```

## 🚀 Deployment Ready
Both scripts are fully compatible with modern hosting platforms like **Render**, **Railway**, or **Heroku**. Connect your GitHub repository, add your API keys to the dashboard env variables, and your dual-service AI SaaS backend is live!
