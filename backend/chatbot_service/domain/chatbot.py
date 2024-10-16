from retriever import Retriever
from query_translation import QueryTranslation
from api_key import API_KEY, GEMINI_MODEL, EMBEDDING_MODEL


class ChatBot():
    def __init__(self , api_key , top_k ):
        self.api_key = api_key 
        self.top_k = top_k
    
    def query( model ):
        return 


