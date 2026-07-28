import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from openai import OpenAI

app = FastAPI(title="AI Review Analyzer & Responder API")

# Инициализация клиента OpenAI для анализа текста
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Структура данных для одного отзыва
class ReviewItem(BaseModel):
    review_id: str
    author: str
    rating: int
    text: str

# Структура запроса, принимающая список отзывов
class ReviewRequest(BaseModel):
    reviews: List[ReviewItem]

@app.post("/analyze-reviews/")
async def analyze_reviews(request: ReviewRequest):
    if not request.reviews:
        raise HTTPException(status_code=400, detail="Список отзывов не может быть пустым")
    
    try:
        # Формируем текст всех отзывов для ИИ
        formatted_reviews = ""
        for r in request.reviews:
            formatted_reviews += f"ID: {r.review_id} | Рейтинг: {r.rating}* | Автор: {r.author}\nТекст: {r.text}\n---\n"

        # Промпт для глубокого анализа и генерации ответов
        prompt = f"""Ты — профессиональный ИИ-менеджер по работе с репутацией бренда. 
        Проанализируй список отзывов ниже и сделай следующее:
        1. Общая аналитика: выдели топ-3 главные жалобы клиентов и топ-3 вещи, которые им нравятся больше всего.
        2. Для КАЖДОГО отзыва напиши идеальный, вежливый ответ от лица компании:
           - Если отзыв положительный (4-5 звезд): поблагодари и пригласи снова.
           - Если отзыв негативный (1-3 звезды): принеси глубокие извинения, прояви эмпатию и предложи решение проблемы.
        
        Список отзывов для обработки:
        {formatted_reviews}"""

        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2500
        )
        
        analysis_result = response.choices[0].message.content

        return {
            "status": "success",
            "analysis_and_responses": analysis_result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
