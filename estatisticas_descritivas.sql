
WITH sub_set AS (
    SELECT * FROM points

    ORDER BY qtdPontos
    LIMIT 1 + (SELECT count(*) % 2 == 0 FROM points)
    OFFSET (SELECT count(*)/2 FROM points)
),

mediana AS(
SELECT avg(qtdPontos) AS mediana FROM sub_set
),

sub_set_1q AS (
    SELECT qtdPontos FROM points

    ORDER BY qtdPontos
    LIMIT 1 + (SELECT count(*) % 2 == 0 FROM points)
    OFFSET (SELECT 1 * count(*)/4 FROM points)
)

--SELECT avg(qtdPontos) FROM sub_set_1q

-- Terceiro de modo análogo


SELECT max(qtdPontos), min(qtdPontos), avg(qtdPontos) FROM points
