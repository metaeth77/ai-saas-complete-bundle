# AI Business Intelligence & Content Automation SaaS Bundle

A powerful, production-ready micro-SaaS backend bundle built with Python and FastAPI. This suite helps businesses automate three major workflows: transcribing corporate meetings, instantly turning summaries into viral social media content, and automatically managing brand reputation by analyzing customer reviews.

## 📦 What's Inside the Bundle

### 1. AI Meeting Summarizer (`main.py`)
- **Audio Transcription**: Converts speech from meeting recordings into text via OpenAI Whisper API (`whisper-1`).
- **Smart Summarization**: Extracts key topics, definitive decisions, and actionable tasks using Anthropic Claude 3.5 Sonnet.

### 2. AI Social Media Post Generator (`social_uploader.py`)
- **Content Repurposing**: Takes any text summary and automatically creates optimized posts for different social networks.
- **Multi-Platform Focus**: Generates 1 structured LinkedIn post, 2 catchy tweets for X, and 1 community post for Telegram.

### 3. AI Reputation & Review Manager (`review_analyzer.py`)
- **Sentiment & Feedback Analysis**: Processes lists of customer reviews to extract top-3 compliments and top-3 complaints.
- **Automated Customer Support**: Instantly generates tailored, polite, and empathetic responses for every review based on star ratings.

## 🛠️ Tech Stack
- Python 3.10+
- FastAPI & Uvicorn
- OpenAI API (Whisper & GPT-4o-mini)
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
   - Run Review Analyzer (Port 8002):
     ```bash
     uvicorn review_analyzer:app --port 8002 --reload
     ```

## 🚀 Deployment Ready
All scripts are fully compatible with hosting platforms like **Render** or **Railway**. Connect your GitHub repository, add your API keys to the dashboard environment variables, and your triple-service AI SaaS backend is live!
