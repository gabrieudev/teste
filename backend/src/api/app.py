from flask import Flask, request, jsonify, abort
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from flask_cors import CORS
import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@db/teste")

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['GET'])
def search_operadoras():
    """
    Rota que realiza busca textual nas operadoras.
    """
    query = request.args.get('query', '')
    page = int(request.args.get('page', 1))
    size = int(request.args.get('size', 10))
    
    if not query:
        abort(400, description="O parâmetro 'query' é obrigatório")
    
    ts_query = ' & '.join(query.split())
    
    sql = text("""
        SELECT 
            o.*,
            ts_rank_cd(
                setweight(to_tsvector(coalesce(razao_social, '')), 'A') ||
                setweight(to_tsvector(coalesce(nome_fantasia, '')), 'B'),
                to_tsquery(:ts_query)
            ) AS rank
        FROM operadoras o
        WHERE to_tsvector(coalesce(razao_social, '') || ' ' || coalesce(nome_fantasia, ''))
              @@ to_tsquery(:ts_query)
        ORDER BY rank DESC
        OFFSET :offset
        LIMIT :limit;
    """)
    
    offset = (page - 1) * size
    with SessionLocal() as session:
        result = session.execute(sql, {'ts_query': ts_query, 'offset': offset, 'limit': size}).fetchall()
        if not result:
            return jsonify({"error": "Nenhum registro encontrado"}), 404
        
        operadoras = []
        for row in result:
            operadora = {key: value for key, value in row._mapping.items() if key != 'rank'}
            operadoras.append(operadora)
        
        return jsonify(operadoras)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

