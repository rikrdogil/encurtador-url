-- upgrade --
ALTER TABLE "users" ADD "full_name" VARCHAR(50);
-- downgrade --
ALTER TABLE "users" DROP COLUMN "full_name";
