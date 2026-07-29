
WITH tb_freq_abs AS (

	SELECT  descProduto,
			COUNT(idTransacao) AS FreqAb
	FROM points
	
	GROUP BY descProduto
),

tb_freqs AS (
SELECT *,
		sum(FreqAb) OVER (ORDER BY descProduto) AS FreqAbsAcum,
		1.0 * FreqAb/ (SELECT sum(FreqAb) FROM tb_freq_abs) AS FreqAbsR
FROM tb_freq_abs
GROUP BY descProduto
)


SELECT *,
		sum(FreqAbsR) OVER (ORDER BY descProduto) AS FreqAcumuR
FROM  tb_freqs;


