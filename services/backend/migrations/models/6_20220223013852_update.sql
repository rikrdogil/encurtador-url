-- upgrade --
ALTER TABLE "urls" ALTER COLUMN "dataExpiracao" SET DEFAULT '2022-03-02';
ALTER TABLE "urls" ALTER COLUMN "dataExpiracao" DROP NOT NULL;
-- downgrade --
ALTER TABLE "urls" ALTER COLUMN "dataExpiracao" SET NOT NULL;
ALTER TABLE "urls" ALTER COLUMN "dataExpiracao" SET DEFAULT '2022-02-28';
