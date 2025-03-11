from fastapi import FastAPI, Query
from typing import List

app = FastAPI()

# Simulação de base de dados de processos (em um cenário real, isso viria do PJe)
processos_mock = [
    {"numero": "0001234-56.2024.1.00.0001", "nome": "João Silva", "status": "Em andamento"},
    {"numero": "0005678-90.2023.1.00.0002", "nome": "Maria Souza", "status": "Concluído"},
    {"numero": "0001122-33.2022.1.00.0003", "nome": "Carlos Oliveira", "status": "Em recurso"},
]

@app.get("/consulta")
def consultar_processos(nome: str = Query(..., title="Nome da parte no processo")) -> List[dict]:
    """
    Consulta processos no PJe com base no nome da parte envolvida.
    """
    resultados = [p for p in processos_mock if nome.lower() in p["nome"].lower()]
    return {"resultados": resultados}
