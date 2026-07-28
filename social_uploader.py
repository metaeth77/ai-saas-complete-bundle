import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from anthropic import Anthropic

app = FastAPI(title="AI Social Media Content Generator API")

# Инициализация клиента Claude ИИ
claude_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# Структура данных, которую программа будет принимать
class ContentRequest(BaseModel):
    source_text: str

@app.post("/generate-posts/")
async def generate_posts(request: ContentRequest):
    if not request.source_text.strip():
        raise HTTPException(status_code=400, detail="Исходный текст не может быть пустым")
    
    try:
        # Промпт для создания вирусного контента под разные соцсети
        prompt = f"""Преврати этот текст в серию профессиональных постов для социальных сетей. 
        Напиши:
        1. Один глубокий, структурированный пост для LinkedIn (с абзацами и эмодзи-маркерами).
        2. Два коротких, цепляющих поста (твита) для Twitter/X.
        3. Один вовлекающий пост для Telegram-канала с призывом к обсуждению.
        
        Исходный текст:
        {request.source_text}"""

        message = claude_client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        # ИСПРАВЛЕНО: Добавлен индекс [0] для корректного извлечения текста
        summary = message.content[0].text

        return {
            "status": "success",
            "generated_content": summary
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
