-- PL_Network, activité Script « Read scores » (type Requête) : assemble le tableau en une phrase, de la ligne la plus ponctuelle à la moins ponctuelle
SELECT STRING_AGG(summary, ' | ') WITHIN GROUP (ORDER BY on_time_pct DESC) AS report FROM dbo.line_scores;
