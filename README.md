# 🎬 LLMOPS Anime Recommender System

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Container-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestration-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Grafana](https://img.shields.io/badge/Grafana-Observability-F46800?style=for-the-badge&logo=grafana&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-EC2-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)

## 📖 Overview

The **Anime Recommender System** is an end-to-end LLMOps (Large Language Model Operations) project designed to provide personalized anime suggestions.

Unlike simple filtering apps, this project leverages **LLMs (Groq/HuggingFace)** to understand natural language queries. It is designed with a production-first mindset, utilizing **Docker** for containerization, **Kubernetes (Minikube)** for orchestration, and **Grafana Cloud** for real-time observability and resource monitoring.

## 🏗️ Architecture

The application follows a microservices-inspired architecture deployed on AWS EC2.

```mermaid
graph TD
    User[User (Browser)] -->|HTTP Request| EC2[AWS EC2 Instance]
    EC2 -->|Port Forward :8501| K8s[Kubernetes Cluster (Minikube)]
    
    subgraph "Kubernetes Cluster"
        Service[Service (Load Balancer)] -->|Route Traffic| Pod[App Pod]
        
        subgraph "Anime Recommender Pod"
            Container[Streamlit Container]
        end
        
        subgraph "Observability Stack"
            Agent[Grafana Agent] -->|Scrape Metrics| Container
        end
    end
    
    Pod -->|API Call| LLM[External LLM API (Groq/HF)]
    Agent -->|Push Metrics| Grafana[Grafana Cloud Dashboard]

LLMOPS--anime_recomender/
├── Dockerfile              # Instructions to build the container image
├── llmops-k8s.yaml         # Kubernetes Deployment & Service manifests
├── pyproject.toml          # Python dependencies (managed by uv)
├── app.py                  # Main Streamlit application entry point
├── README.md               # Project documentation
└── ...
