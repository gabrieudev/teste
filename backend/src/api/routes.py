from flask import Blueprint, request, jsonify, abort
from sqlalchemy import text
from .database import SessionLocal

operadoras_bp = Blueprint('operadoras', __name__)

@operadoras_bp.route('/search', methods=['GET'])
def search_operadoras():
    query = request.args.get('query', '')
    page = int(request.args.get('page', 1))
    size = int(request.args.get('size', 10))
    
    if not query:
        abort(400, description="O parâmetro 'query' é obrigatório")
    
    if page < 1 or size < 1:
        abort(400, description="Parâmetros 'page' e 'size' devem ser maiores que zero")
    
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
    
    sql_count = text("""
        SELECT COUNT(*) as total
        FROM operadoras o
        WHERE to_tsvector(coalesce(razao_social, '') || ' ' || coalesce(nome_fantasia, ''))
              @@ to_tsquery(:ts_query)
    """)
    
    offset = (page - 1) * size
    with SessionLocal() as session:
        result = session.execute(sql, {'ts_query': ts_query, 'offset': offset, 'limit': size}).fetchall()
        total = session.execute(sql_count, {'ts_query': ts_query}).scalar()
        operadoras = [
            {key: value for key, value in row._mapping.items() if key != 'rank'}
            for row in result
        ]
        
        return jsonify({
            "results": operadoras,
            "total": total,
            "page": page,
            "size": size
        })