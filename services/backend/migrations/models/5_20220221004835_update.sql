-- upgrade --
ALTER TABLE "urls" ALTER COLUMN "dataExpiracao" SET DEFAULT '2022-02-28';
ALTER TABLE "users" RENAME COLUMN "nome" TO "full_name";
ALTER TABLE "users" RENAME COLUMN "login" TO "username";
ALTER TABLE "users" RENAME COLUMN "senha" TO "password";
-- downgrade --
ALTER TABLE "urls" ALTER COLUMN "dataExpiracao" SET DEFAULT '2022-02-27';
ALTER TABLE "users" RENAME COLUMN "full_name" TO "nome";
ALTER TABLE "users" RENAME COLUMN "password" TO "senha";
ALTER TABLE "users" RENAME COLUMN "username" TO "login";
