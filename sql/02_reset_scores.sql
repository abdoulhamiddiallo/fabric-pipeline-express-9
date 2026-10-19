-- PL_Network, activité Script « Reset scores » (type Requête) : vide le tableau avant chaque exécution
DELETE FROM dbo.line_scores; SELECT 1 AS ok;
