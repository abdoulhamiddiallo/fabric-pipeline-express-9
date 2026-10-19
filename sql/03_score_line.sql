-- PL_Line, activité Script « Score line » (type Requête, contenu dynamique)
-- Lit la table de la ligne dans le lakehouse par son nom à trois parties et inscrit une phrase verdict
-- Un train est à l'heure s'il part avec moins de 60 secondes de retard
INSERT INTO dbo.line_scores
SELECT '@{pipeline().parameters.line_code}',
       CAST(100.0 * SUM(CASE WHEN CAST(delay_s AS int) < 60 THEN 1 ELSE 0 END) / COUNT(*) AS decimal(5,1)),
       CONCAT('@{pipeline().parameters.line_name} ',
              CAST(100.0 * SUM(CASE WHEN CAST(delay_s AS int) < 60 THEN 1 ELSE 0 END) / COUNT(*) AS decimal(5,1)),
              ' % à l''heure (', COUNT(*), ' départs, max ', MAX(CAST(delay_s AS int)), ' s)')
FROM LH_Shinkansen.dbo.dep_@{pipeline().parameters.line_code};
SELECT 1 AS ok;
