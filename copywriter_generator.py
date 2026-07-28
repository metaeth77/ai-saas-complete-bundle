import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI(title="AI Marketing Copywriter API")

# Инициализация клиента OpenAI
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Структура данных, которую программа будет принимать от пользователя
class CopyRequest(BaseModel):
    product_name: str
    product_description: str
    target_audience: str

@app.post("/generate-copy/")
async def generate_copy(request: CopyRequest):
    # Проверка на пустые поля
    if not request.product_name.strip() or not request.product_description.strip() or not request.target_audience.strip():
        raise HTTPException(status_code=400, detail="Все поля (product_name, product_description, target_audience) обязательны для заполнения")
    
    try:
        # Формируем глубокий промпт для ИИ маркетолога
        prompt = f"""Ты — первоклассный международный контент-маркетолог и эксперт по продажам.
        Напиши высококонверсионные рекламные тексты для продукта "{request.product_name}".
        
        Описание продукта: {request.product_description}
        Целевая аудитория: {request.target_audience}
        
        Сгенерируй тексты строго по двум классическим маркетинговым фреймворкам:
        
        1. Фреймворк AIDA (Attention, Interest, Desire, Action):
           - Attention (Внимание): Цепляющий заголовок.
           - Interest (Интерес): Вовлекающий абзац, раскрывающий суть.
           - Desire (Желание): Главные преимущества, бьющие в боли аудитории.
           - Action (Действие): Четкий призыв к действию (CTA).
        
        2. Фреймворк PAS (Problem, Agitation, Solution):
           - Problem (Проблема): Описание главной боли клиента.
           - Agitation (Агитация): Раздувание проблемы, почему её нельзя игнорировать.
           - Solution (Решение): Как наш продукт идеально решает эту проблему.
        
        Оформи результат красиво, используя абзацы и эмодзи-маркеры для удобства чтения."""

        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )
        
        copywriting_result = response.choices[0].message.content

        return {
            "status": "success",
            "marketing_copy": copywriting_result
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
