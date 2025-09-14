from fastapi import APIRouter, Form
from llm.chat_service import MistralChat
from llm.conversation import handle_farmer_query

router = APIRouter()
chat_engine = MistralChat()

@router.post("/query")
async def query_mistral(user_input: str = Form(...), detected_lang: str = Form(...)):
    """
    Accept user question and return Mistral's farmer-friendly answer.
    """
    answer = chat_engine.ask(user_input)
    final_answer = handle_farmer_query(answer, detected_lang)

    return {
        "answer": answer,
        "translated_answer": final_answer
        }
