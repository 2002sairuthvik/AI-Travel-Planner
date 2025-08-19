from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import GROQ_API_KEY

llm = ChatGroq(
    api_key=GROQ_API_KEY, 
    model_name="llama-3.3-70b-versatile",
    temperature=0.3
)

itineary_prompt = ChatPromptTemplate([
    ("system","You are a helpful travel assistant. Create a day trip itineary for {city} based on user's intrest: {intrests}. Provide a brief , bulleted itineary"),
    ("human","Create a itineary for my day trip")
])

def generate_itineary(city:str, intrests:list[str]) -> str:
    response = llm.invoke(
        itineary_prompt.format_messages(city=city, intrests=', '.join(intrests))
    )
    return response.content