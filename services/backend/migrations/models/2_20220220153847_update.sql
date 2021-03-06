-- upgrade --
CREATE TABLE IF NOT EXISTS "urls" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "url" VARCHAR(225) NOT NULL,
    "codigoUrl" VARCHAR(225) NOT NULL,
    "urlEncurtada" VARCHAR(225) NOT NULL,
    "dataExpiracao" TIMESTAMPTZ NOT NULL  DEFAULT '2022-02-27',
    "dataCriacao" TIMESTAMPTZ NOT NULL  DEFAULT CURRENT_TIMESTAMP
);;
DROP TABLE IF EXISTS "urlitem";
-- downgrade --
DROP TABLE IF EXISTS "urls";
