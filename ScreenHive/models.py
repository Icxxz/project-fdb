from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class Usuario(BaseModel):
    id_usuario: int
    nome: str
    email: str
    senha: str
    data_cadastro: Optional[date] = None
    data_nascimento: Optional[date] = None

class UsuarioUpdate(BaseModel):
    nome: str
    email: str
    senha: Optional[str] = None
    data_nascimento: Optional[date] = None

class Conteudo(BaseModel):
    id_conteudo: int
    titulo: str
    tipo: str
    ano_lancamento: Optional[date] = None
    duracao: float
    classificacao_indicativa: Optional[str] = None
    sinopse: str

class ConteudoUpdate(BaseModel):
    titulo: str
    tipo: str
    ano_lancamento: Optional[date] = None
    classificacao_indicativa: Optional[str] = None
    sinopse: str

class Genero(BaseModel):
    id_genero: int
    nome: str

class ContGenero(BaseModel):
    id_conteudo: int
    id_genero: int

class Avaliacao(BaseModel):
    id_avaliacao: int
    id_usuario: int
    id_conteudo: int
    nota: float
    comentario: Optional[str] = None
    data_avaliacao: Optional[date] = None

class AvaliacaoUpdate(BaseModel):
    nota: float
    comentario: Optional[str] = None

class ItemLista(BaseModel):
    id_conteudo: int
    id_lista: int

class Lista(BaseModel):
    id_lista: int
    id_usuario: int
    nome_lista: str

class HistVisualizacao(BaseModel):
    id_historico: int
    id_usuario: int
    id_conteudo: int
    concluido: bool
    data_ultima_visualizacao: Optional[date] = None

class HistVisualizacaoUpdate(BaseModel):
    concluido: bool
    data_ultima_visualizacao: Optional[date] = None

class Visualizacao(BaseModel):
    id_visualizacao: int
    id_usuario: int
    id_conteudo: int
    minutos_assistidos: float
    data_visualizacao: Optional[date] = None

class VisualizacaoUpdate(BaseModel):
    minutos_assistidos: float
    data_visualizacao: Optional[date] = None

class Recomendacao(BaseModel):
    id_recomendacao: int
    id_usuario_recomenda: int
    id_usuario_recebe: int
    id_conteudo: int
    mensagem: Optional[str] = None
    data_recomendacao: Optional[date] = None

class Seguidores(BaseModel):
    id_seguidor: int  
    id_seguido: int   

