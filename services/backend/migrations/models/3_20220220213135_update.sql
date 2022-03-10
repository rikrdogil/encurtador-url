-- upgrade --
ALTER TABLE "urls" ALTER COLUMN "codigoUrl" DROP NOT NULL;
ALTER TABLE "urls" ALTER COLUMN "urlEncurtada" DROP NOT NULL;
-- downgrade --
ALTER TABLE "urls" ALTER COLUMN "codigoUrl" SET NOT NULL;
ALTER TABLE "urls" ALTER COLUMN "urlEncurtada" SET NOT NULL;
