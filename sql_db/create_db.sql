CREATE DATABASE kg_express;
CREATE USER express_user  WITH PASSWORD 'qwerty123';
ALTER ROLE express_user SET client_encoding TO 'utf-8';
ALTER ROLE express_user SET default_transaction_isolation TO 'read committed';
ALTER ROLE express_user SET timezone TO 'Asia/Bishkek';
GRANT ALL PRIVILEGES ON DATABASE kg_express TO express_user;
