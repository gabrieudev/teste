WITH max_date AS (
    SELECT MAX(data) AS max_d FROM despesas
)
SELECT 
    o.nome_fantasia AS operadora,
    SUM(d.vl_saldo_final - d.vl_saldo_inicial) AS total_despesa
FROM despesas d
JOIN operadoras o ON d.reg_ans = o.registro_ans
CROSS JOIN max_date
WHERE d.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
    AND d.data >= date_trunc('month', max_date.max_d) - INTERVAL '2 months'
    AND d.data <= max_date.max_d
GROUP BY o.registro_ans, o.nome_fantasia
ORDER BY total_despesa DESC
LIMIT 10;

WITH max_date AS (
    SELECT MAX(data) AS max_d FROM despesas
)
SELECT 
    o.nome_fantasia AS operadora,
    SUM(d.vl_saldo_final - d.vl_saldo_inicial) AS total_despesa
FROM despesas d
JOIN operadoras o ON d.reg_ans = o.registro_ans
CROSS JOIN max_date
WHERE d.descricao = 'EVENTOS/ SINISTROS CONHECIDOS OU AVISADOS DE ASSISTÊNCIA A SAÚDE MEDICO HOSPITALAR'
    AND d.data >= max_date.max_d - INTERVAL '1 year'
GROUP BY o.registro_ans, o.nome_fantasia
ORDER BY total_despesa DESC
LIMIT 10;