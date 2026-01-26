from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from src.prompt_template import get_anime_prompt

class AnimeRecommender:
    def __init__(self, retriever, api_key: str, model_name: str):
        self.llm = ChatGroq(api_key=api_key, model=model_name, temperature=0)
        self.prompt = get_anime_prompt()
        self.retriever = retriever

        # Helper to format documents
        def format_docs(docs):
            return "\n\n".join(doc.page_content for doc in docs)

        # THE NEW LCEL CHAIN
        self.qa_chain = (
            {
                "context": self.retriever | format_docs,
                "question": RunnablePassthrough()
            }
            | self.prompt
            | self.llm
            | StrOutputParser()
        )

    def get_recommendation(self, query: str):
        # Invoke is the new standard (instead of calling it like a function)
        result = self.qa_chain.invoke(query)
        return result  # StrOutputParser already returns a string