from fastapi import APIRouter, FastAPI, HTTPException
from models import Usuario, Conteudo, Genero, ContGenero, Avaliacao, ItemLista, Lista, HistVisualizacao, Visualizacao, Recomendacao, Seguidores
from db import get_conection
from typing import List, Optional

router = APIRouter()

@router.post("/usuario")
async def criar_usuario(usr: Usuario):
    conn = get_conection()
    cur = conn.cursor()

    try:
        cur.execute(
            """
            INSERT INTO usuario(id_usuario, nome, email, senha, data_cadastro, data_nascimento) VALUES (%s, %s, %s, %s, %s, %s)
            """, (usr.id_usuario, usr.nome, usr.email, usr.senha, usr.data_cadastro, usr.data_nascimento)
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()
    return {"msg": "Usuário criado com sucesso"}

@router.post("/conteudo")
async def criar_conteudo(conteudo: Conteudo):
    conn = get_conection()
    cur = conn.cursor()

    try:
        cur.execute(
            """
            INSERT INTO conteudo(id_conteudo, titulo, tipo, ano_lancamento, duracao, classificacao_indicativa, sinopse) VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (conteudo.id_conteudo, conteudo.titulo, conteudo.tipo, conteudo.ano_lancamento, conteudo.duracao, conteudo.classificacao_indicativa, conteudo.sinopse)
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()

    return {"msg": "Conteúdo criado com sucesso"}

@router.post("/genero")
async def criar_genero(genero: Genero): 
    conn = get_conection()
    cur = conn.cursor()

    try:
        cur.execute(
            """
            INSERT INTO genero(id_genero, nome) VALUES (%s, %s)
            """, (genero.id_genero, genero.nome)
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()

    return {"msg": "Gênero criado com sucesso"}

@router.post("/cont_genero")
async def criar_cont_genero(cont_genero: ContGenero):
    conn = get_conection()
    cur = conn.cursor()

    try:
        cur.execute(
            """
            INSERT INTO cont_genero(id_conteudo, id_genero) VALUES (%s, %s)
            """, (cont_genero.id_conteudo, cont_genero.id_genero)
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()

    return {"msg": "Conteúdo-Gênero criado com sucesso"}

@router.post("/avaliacao")
async def criar_avaliacao(avaliacao: Avaliacao):
    conn = get_conection()
    cur = conn.cursor()

    try:
        cur.execute(
            """
            INSERT INTO avaliacao(id_avaliacao, id_usuario, id_conteudo, nota, comentario, data_avaliacao) VALUES (%s, %s, %s, %s, %s, %s)
            """, (avaliacao.id_avaliacao, avaliacao.id_usuario, avaliacao.id_conteudo, avaliacao.nota, avaliacao.comentario, avaliacao.data_avaliacao)
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()

    return {"msg": "Avaliação criada com sucesso"}

@router.post("/recomendacao")
async def criar_recomendacao(recomendacao: Recomendacao):
    conn = get_conection()
    cur = conn.cursor()

    try:
        cur.execute(
            """
            INSERT INTO recomendacao(id_recomendacao, id_usuario_recomenda, id_usuario_recebe, id_conteudo, mensagem, data_recomendacao) VALUES (%s, %s, %s, %s, %s, %s)
            """, (recomendacao.id_recomendacao, recomendacao.id_usuario_recomenda, recomendacao.id_usuario_recebe, recomendacao.id_conteudo, recomendacao.mensagem, recomendacao.data_recomendacao)
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()

    return {"msg": "Recomendação criada com sucesso"}

@router.post("/seguidores")
async def criar_seguidor(seguidor: Seguidores):
    conn = get_conection()
    cur = conn.cursor()

    try:
        cur.execute(
            """
            INSERT INTO seguidores(id_seguidor, id_seguido) VALUES (%s, %s)
            """, (seguidor.id_seguidor, seguidor.id_seguido)
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()

    return {"msg": "Seguidor criado com sucesso"}


@router.get("/usuario", response_model=List[Usuario])
async def obter_usuario():
    conn = get_conection()
    cur = conn.cursor()
    cur.execute("SELECT id_usuario, nome, email, senha, data_cadastro, data_nascimento FROM usuario")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [
        Usuario(
            id_usuario=row[0],
            nome=row[1],
            email=row[2],
            senha=row[3],
            data_cadastro=row[4],
            data_nascimento=row[5]
        ) 
        for row in rows
    ]

@router.get("/conteudo", response_model=List[Conteudo])
async def obter_conteudo():
    conn = get_conection()
    cur = conn.cursor()
    cur.execute("SELECT id_conteudo, titulo, tipo, ano_lancamento, duracao, classificacao_indicativa, sinopse FROM conteudo")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [
        Conteudo(
            id_conteudo=row[0],
            titulo=row[1],
            tipo=row[2],
            ano_lancamento=row[3],
            duracao=row[4],
            classificacao_indicativa=row[5],
            sinopse=row[6]
        ) 
        for row in rows
    ]

@router.get("/avaliacao", response_model=List[Avaliacao])
async def obter_avaliacao():
    conn = get_conection()
    cur = conn.cursor()
    cur.execute("SELECT id_avaliacao, id_usuario, id_conteudo, nota, comentario, data_avaliacao FROM avaliacao")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [
        Avaliacao(
            id_avaliacao=row[0],
            id_usuario=row[1],
            id_conteudo=row[2],
            nota=row[3],
            comentario=row[4],
            data_avaliacao=row[5]
        )
        for row in rows
    ]

@router.get("/recomendacao", response_model=List[Recomendacao])
async def obter_recomendacao():
    conn = get_conection()
    cur = conn.cursor()
    cur.execute("SELECT id_recomendacao, id_usuario_recomenda, id_usuario_recebe, id_conteudo, mensagem, data_recomendacao FROM recomendacao")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [
        Recomendacao(
            id_recomendacao=row[0],
            id_usuario_recomenda=row[1],
            id_usuario_recebe=row[2],
            id_conteudo=row[3],
            mensagem=row[4],
            data_recomendacao=row[5]
        )
        for row in rows
    ]
@router.get("/genero", response_model=List[Genero])
async def obter_generos():
    conn = get_conection()
    cur = conn.cursor()
    cur.execute("SELECT id_genero, nome FROM genero")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [Genero(id_genero=row[0], nome=row[1]) for row in rows]

@router.get("/cont_genero")
async def obter_cont_generos():
    conn = get_conection()
    cur = conn.cursor()
    cur.execute("SELECT id_conteudo, id_genero FROM cont_genero")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [ContGenero(id_conteudo=row[0], id_genero=row[1]) for row in rows]

@router.get("/seguidores", response_model=List[Seguidores])
async def obter_seguidores():
    conn = get_conection()
    cur = conn.cursor()
    cur.execute("SELECT id_seguidor, id_seguido FROM seguidores")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [Seguidores(id_seguidor=row[0], id_seguido=row[1]) for row in rows]



@router.patch("/usuario/{id_usuario}")
async def atualizar_usuario(id_usuario: int, usuario: Usuario):
    conn = get_conection()
    cur = conn.cursor()
    cur.execute("SELECT id_usuario FROM usuario WHERE id_usuario = %s", (id_usuario,))
    if not cur.fetchone():
        cur.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    
    fields = []
    values = []   
    for field, value in usuario.dict(exclude_unset=True).items():
        fields.append(f"{field} = %s")
        values.append(value) 
    if not fields:
        cur.close()
        conn.close()
        raise HTTPException(status_code=400, detail="Nenhum campo a ser atualizado")

    values.append(id_usuario)
    try:
        cur.execute(
            f"""
            UPDATE usuario SET {', '.join(fields)} WHERE id_usuario = %s
            """, tuple(values)
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()
    return {"msg": "Usuário atualizado com sucesso"}

@router.patch("/conteudo/{id_conteudo}")
async def atualizar_conteudo(id_conteudo: int, conteudo: Conteudo):
    conn = get_conection()
    cur = conn.cursor()
    cur.execute("SELECT id_conteudo FROM conteudo WHERE id_conteudo = %s", (id_conteudo,))
    if not cur.fetchone():
        cur.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Conteúdo não encontrado")

    fields = []
    values = []
    for field, value in conteudo.dict(exclude_unset=True).items():
        fields.append(f"{field} = %s")
        values.append(value)
    if not fields:
        cur.close()
        conn.close()
        raise HTTPException(status_code=400, detail="Nenhum campo a ser atualizado")

    values.append(id_conteudo)
    try:
        cur.execute(
            f"""
            UPDATE conteudo SET {', '.join(fields)} WHERE id_conteudo = %s
            """, tuple(values)
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()
    return {"msg": "Conteúdo atualizado com sucesso"}

@router.patch("/avaliacao/{id_avaliacao}")
async def atualizar_avaliacao(id_avaliacao: int, avaliacao: Avaliacao):
    conn = get_conection()
    cur = conn.cursor()
    cur.execute("SELECT id_avaliacao FROM avaliacao WHERE id_avaliacao = %s", (id_avaliacao,))
    if not cur.fetchone():
        cur.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")

    fields = []
    values = []
    for field, value in avaliacao.dict(exclude_unset=True).items():
        fields.append(f"{field} = %s")
        values.append(value)
    if not fields:
        cur.close()
        conn.close()
        raise HTTPException(status_code=400, detail="Nenhum campo a ser atualizado")

    values.append(id_avaliacao)
    try:
        cur.execute(
            f"""
            UPDATE avaliacao SET {', '.join(fields)} WHERE id_avaliacao = %s
            """, tuple(values)
        )
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        conn.close()
    return {"msg": "Avaliação atualizada com sucesso"}

@router.delete("/usuario/{id_usuario}")
async def deletar_usuario(id_usuario: int):
    conn = get_conection()
    cur = conn.cursor()
    cur.execute("DELETE FROM usuario WHERE id_usuario = %s", (id_usuario,))
    conn.commit()
    cur.close()
    return {"msg": "Usuário deletado com sucesso"}

@router.delete("/conteudo/{id_conteudo}")
async def deletar_conteudo(id_conteudo: int):
    conn = get_conection()
    cur = conn.cursor()
    cur.execute("DELETE FROM conteudo WHERE id_conteudo = %s", (id_conteudo,))
    conn.commit()
    cur.close()
    return {"msg": "Conteúdo deletado com sucesso"}

@router.delete("/avaliacao/{id_avaliacao}")
async def deletar_avaliacao(id_avaliacao: int): 
    conn = get_conection()
    cur = conn.cursor()
    cur.execute("DELETE FROM avaliacao WHERE id_avaliacao = %s", (id_avaliacao,))
    conn.commit()
    cur.close()
    return {"msg": "Avaliação deletada com sucesso"}

@router.delete("/genero/{id_genero}")
async def deletar_genero(id_genero: int):
    conn = get_conection()
    cur = conn.cursor()
    cur.execute("DELETE FROM genero WHERE id_genero = %s", (id_genero,))
    conn.commit()
    cur.close()
    return {"msg": "Gênero deletado com sucesso"}

    
@router.delete("/cont_genero")
async def deletar_cont_genero(id_conteudo: int, id_genero: int):
    conn = get_conection()
    cur = conn.cursor()
    cur.execute("DELETE FROM cont_genero WHERE id_conteudo = %s AND id_genero = %s", (id_conteudo, id_genero))
    conn.commit()
    cur.close()
    return {"msg": "Relação conteúdo-gênero deletada com sucesso"}

@router.delete("/recomendacao/{id_recomendacao}")
async def deletar_recomendacao(id_recomendacao: int):
    conn = get_conection()
    cur = conn.cursor()
    cur.execute("DELETE FROM recomendacao WHERE id_recomendacao = %s", (id_recomendacao,))
    conn.commit()
    cur.close()
    return {"msg": "Recomendação deletada com sucesso"}

@router.delete("/seguidores")
async def deletar_seguidor(id_usuario: int, id_seguidor: int):
    conn = get_conection()
    cur = conn.cursor()
    cur.execute("DELETE FROM seguidores WHERE id_seguidor = %s AND id_seguido = %s", (id_seguidor, id_usuario))
    conn.commit()
    cur.close()
    conn.close()
    return {"msg": "Seguidor removido com sucesso"}


