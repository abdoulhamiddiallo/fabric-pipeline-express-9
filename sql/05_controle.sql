-- Contrôle dans WH_Shinkansen : départs et pire retard de chaque ligne, lus dans le lakehouse
SELECT 'Tōkaidō' AS line, COUNT(*) AS departures, MAX(CAST(delay_s AS int)) AS max_delay_s FROM LH_Shinkansen.dbo.dep_tokaido
UNION ALL SELECT 'Sanyō', COUNT(*), MAX(CAST(delay_s AS int)) FROM LH_Shinkansen.dbo.dep_sanyo
UNION ALL SELECT 'Tōhoku', COUNT(*), MAX(CAST(delay_s AS int)) FROM LH_Shinkansen.dbo.dep_tohoku
UNION ALL SELECT 'Hokkaidō', COUNT(*), MAX(CAST(delay_s AS int)) FROM LH_Shinkansen.dbo.dep_hokkaido;
