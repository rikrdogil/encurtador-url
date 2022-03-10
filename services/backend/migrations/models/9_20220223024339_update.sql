-- upgrade --
ALTER TABLE "urls" DROP COLUMN "dataCriacao";
-- downgrade --
ALTER TABLE "urls" ADD "dataCriacao" DATE NOT NULL;
