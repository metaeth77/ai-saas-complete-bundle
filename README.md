# 💰 PROJECT FOR SALE / ACQUISITION AVAILABLE

**This complete, production-ready 4-in-1 AI codebase is officially available for full acquisition.** 
* **Asking Price:** $8,000 (Full ownership transfer, single payment, no recurring licensing fees).
* **Live Product Showcase:** https://ultimate-ai.site
* **Verified Escrow Platforms:** [Acquire.com](https://acquire.com) | [StartuPage](https://startupage.com)

If you are an entrepreneur or an automation agency looking to buy and instantly commercialize this FastAPI suite for your clients or build a SaaS around it, please contact me directly:
📩 **Email:** hakan77701@gmail.com
💬 **Or open a GitHub Issue / send a direct inquiry.**

---

# # Ultimate AI Business Intelligence & Marketing Automation SaaS Bundle

A comprehensive, production-ready micro-SaaS backend bundle built with Python and FastAPI. This suite automates four major high-value business workflows in one package: corporate meeting analysis, automated multi-platform social media marketing, customer review sentiment management, and framework-based copywriting generation.

## 📦 What's Inside the Bundle

### 1. AI Meeting Summarizer (`main.py`)
- **Audio Transcription**: Converts speech from meeting recordings into accurate text via OpenAI Whisper API (`whisper-1`).
- **Smart Summarization**: Extracts key topics, definitive decisions, and actionable tasks with deadlines using Anthropic Claude 3.5 Sonnet.

### 2. AI Social Media Post Generator (`social_uploader.py`)
- **Content Repurposing**: Takes any text summary and automatically creates highly optimized posts for different social networks.
- **Multi-Platform Focus**: Generates 1 structured LinkedIn post, 2 catchy tweets for X, and 1 community post for Telegram.

### 3. AI Reputation & Review Manager (`review_analyzer.py`)
- **Sentiment Analysis**: Processes customer reviews to extract top-3 compliments and top-3 complaints.
- **Automated Support**: Instantly generates tailored, polite, and empathetic responses based on star ratings.

### 4. AI Marketing Copywriter (`copywriter_generator.py`)
- **Framework Copywriting**: Instantly generates high-converting marketing copies based on input product parameters and target audience.
- **Classic Sales Formulas**: Automatically outputs copies structured around **AIDA** (Attention, Interest, Desire, Action) and **PAS** (Problem, Agitation, Solution) frameworks.

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
   - Run Marketing Copywriter (Port 8003):
     ```bash
     uvicorn copywriter_generator:app --port 8003 --reload
     ```

## 🚀 Deployment Ready
All services are optimized for cloud infrastructure. Connect your GitHub repository to platforms like **Render** or **Railway**, configure your API keys in the environment variables, and your 4-service ИИ SaaS backend is live!
