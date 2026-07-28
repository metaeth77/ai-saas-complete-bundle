import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from openai import OpenAI
from anthropic import Anthropic

app = FastAPI(title="AI Meeting Summarizer API")

# Инициализация ИИ-клиентов (ключи берутся из настроек сервера)
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
claude_client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

@app.post("/process-audio/")
async def process_audio(file: UploadFile = File(...)):
    # 1. Проверяем формат файла
    if not file.filename.endswith(('.mp3', '.wav', '.m4a')):
        raise HTTPException(status_code=400, detail="Неверный формат аудио")
    
    try:
        # Сохраняем временный файл
        temp_file_path = f"temp_{file.filename}"
        with open(temp_file_path, "wb") as buffer:
            buffer.write(await file.read())

        # 2. ШАГ ИИ: Превращаем аудио в текст (OpenAI Whisper)
        with open(temp_file_path, "rb") as audio_file:
            transcript_response = openai_client.audio.transcriptions.create(
                model="whisper-1", 
                file=audio_file
            )
        full_text = transcript_response.text

        # Удаляем временный файл после обработки
        os.remove(temp_file_path)

        # 3. ШАГ ИИ: Делаем выжимку встречи (Claude 3.5 Sonnet)
        prompt = f"""Анализируй этот текст бизнес-созвона и сделай структурированную выжимку:
        1. Главная тема обсуждения.
        2. Ключевые решения, к которым пришли.
        3. Список задач (Кто, что и до какого срока должен сделать).
        
        Текст созвона:
        {full_text}"""

        message = claude_client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1500,
            messages=[{"role": "user", "content": prompt}]
        )
        summary = message.content[0].text

        # Возвращаем покупателю готовый результат
        return {
            "status": "success",
            "full_transcript": full_text,
            "summary": summary
        }

    except Exception as e:
        if os.path.exists(temp_file_path):
            os.remove(temp_file_path)
        raise HTTPException(status_code=500, detail=str(e))
