-- upgrade --
ALTER TABLE "urls" ALTER COLUMN "dataExpiracao" TYPE DATE USING "dataExpiracao"::DATE;
ALTER TABLE "urls" ALTER COLUMN "dataCriacao" TYPE DATE USING "dataCriacao"::DATE;
-- downgrade --
ALTER TABLE "urls" ALTER COLUMN "dataExpiracao" TYPE TIMESTAMPTZ USING "dataExpiracao"::TIMESTAMPTZ;
ALTER TABLE "urls" ALTER COLUMN "dataCriacao" TYPE TIMESTAMPTZ USING "dataCriacao"::TIMESTAMPTZ;
