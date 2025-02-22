# PTIT'S AI Assistance

## Description
PTIT'S AI Assistance is an intelligent AI assistant solution designed to help PTIT students quickly retrieve and process information for effective admissions counseling. Leveraging advanced technologies like data crawling, Retrieval-Augmented Generation (RAG), vector search, Langchain, and state-of-the-art LLMs, the system delivers context-aware responses through a user-friendly interface.
## Overview
![alt text](.\images\image-2.png)

![alt text](.\images\image.png)

![alt text](.\images\image-1.png)

![alt text](.\images\image-3.png)
## Features
- **Intelligent Assistance:** Provides fast and accurate information retrieval to support admissions counseling.
- **Data Crawling & Preprocessing:** Automatically collects data from reliable sources and processes it into high-quality datasets.
- **Advanced RAG System:** Integrates query translation, routing, and retrieval for context-aware outputs.
- **Seamless Integration:** Offers an API-driven, user-friendly interface that ensures smooth interaction.

## Tech Stack
- **Data Crawling:** Automated Python scripts.
- **RAG & Vector Search:** Query Translation, Routing, and Retrieval integrated with vector databases.
- **Langchain & LLMs:** Utilized for advanced natural language processing.
- **Website Development:** Modern frontend (Vuejs) and backend (FastAPI) technologies for a seamless user experience.

## Team
- **Team Size:** 5 members  

## Getting Started

1. **Clone the repository:**
   ```bash
    git clone https://github.com/trong269/Chatbot_PTIT.git
2. **Install labriry**
   ```bash
    pip instal -r requirements.txt
3. **Run front end**
   ```bash
    cd .\frontend\
    yarn install
    yarn dev
4. **Run back end Server**
   ```bash
    cd .\backend\chatbot_service\ 
    uvicorn api.app.main:app --reload 
