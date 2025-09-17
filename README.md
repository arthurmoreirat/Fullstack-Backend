# Full Stack - Backend

## Tarefa

Implementar um `CRUD` em FastAPI.

| Letra | Descrição | Implementado |
| --- | --- | --- |
| C | Create | :white_check_mark: |
| R | Read (All) | :white_check_mark: |
| R | Read (id_users) | :white_check_mark: |
| U | Update | :white_check_mark: |
| D | Delete | :white_check_mark: |

## Comandos Úteis

Instalar biblioteca

```
pip install fastapi
```

Iniciar API

```python
python -m fastapi dev
```

## Erro

O que faltou para o `INSERT` funcionar foi [essa](./sqllite.py#L12) linha, no final da função `run_sql`.

```python
con.commit()
```

## Referências

- [Slide](https://www.canva.com/design/DAGlpCzcjpk/XaYBM2AEBjCus2TIBR9nVA/edit?utm_content=DAGlpCzcjpk&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton)

- [SQLite Viewer - Florian Klampfer](https://marketplace.visualstudio.com/items/?itemName=qwtel.sqlite-viewer)

- [Artigo Medium](https://medium.com/@guilhermehuther/back-end-basics-e9a2ed1f244a)

- [Documentação FastAPI](https://fastapi.tiangolo.com/)

- [Documentação sqllite](https://docs.python.org/3/library/sqlite3.html)

- [HTTP/HTTPS](http://developer.mozilla.org/pt-BR/docs/Web/HTTP)
