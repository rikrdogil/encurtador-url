-- upgrade --
ALTER TABLE "urls" ALTER COLUMN "dataExpiracao" DROP DEFAULT;
-- downgrade --
ALTER TABLE "urls" ALTER COLUMN "dataExpiracao" SET DEFAULT '2022-03-02';
