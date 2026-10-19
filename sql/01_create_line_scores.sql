-- À exécuter une fois dans l'entrepôt WH_Shinkansen (pas dans le point de terminaison SQL du lakehouse, qui est en lecture seule)
CREATE TABLE dbo.line_scores (line_code varchar(20), on_time_pct decimal(5,1), summary varchar(200));
