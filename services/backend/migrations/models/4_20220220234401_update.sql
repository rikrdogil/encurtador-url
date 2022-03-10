-- upgrade --
ALTER TABLE "users" RENAME COLUMN "username" TO "login";
ALTER TABLE "users" RENAME COLUMN "full_name" TO "nome";
ALTER TABLE "users" RENAME COLUMN "password" TO "senha";
DROP TABLE IF EXISTS "notes";
-- downgrade --
ALTER TABLE "users" RENAME COLUMN "login" TO "username";
ALTER TABLE "users" RENAME COLUMN "nome" TO "full_name";
ALTER TABLE "users" RENAME COLUMN "senha" TO "password";
