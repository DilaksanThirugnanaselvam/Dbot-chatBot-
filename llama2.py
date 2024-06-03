from langchain_community.llms import Ollama

SYSTEM_PROMPT = """
I am a helpful AI assistant. I am Dilak's assistant.
"""

def firePrompt(prompt: str, temp=0.4) -> str:
    llm = Ollama(model="llama2",
             system=SYSTEM_PROMPT,
             temperature=temp
             )
    res = llm.invoke(prompt)
    return res