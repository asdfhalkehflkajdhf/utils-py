--
-- 由SQLiteStudio v3.2.1 产生的文件 周六 十二月 8 20:19:49 2018
--
-- 文本编码：UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- 表：table_businessInfo
DROP TABLE IF EXISTS table_businessInfo;
CREATE TABLE table_businessInfo (business_id BIGINT (20) PRIMARY KEY, review_all BIGINT (20), review_tg BIGINT (20));

-- 表：table_commentInfo
DROP TABLE IF EXISTS table_commentInfo;
CREATE TABLE table_commentInfo (comment_id INTEGER PRIMARY KEY AUTOINCREMENT, ctime DATETIME, context TEXT, type_id BIGINT, level INTEGER, business_id INT, font_id INTEGER, layout_id INTEGER);

-- 表：table_commentType
DROP TABLE IF EXISTS table_commentType;
CREATE TABLE table_commentType (type_id INTEGER PRIMARY KEY AUTOINCREMENT, "desc" TEXT);

-- 表：table_config
DROP TABLE IF EXISTS table_config;
CREATE TABLE table_config (crawlingInterval INTEGER);
INSERT INTO table_config (crawlingInterval) VALUES (60);

-- 表：table_coreStat
DROP TABLE IF EXISTS table_coreStat;
CREATE TABLE table_coreStat (state BOOLEAN, uptime DATETIME);
INSERT INTO table_coreStat (state, uptime) VALUES (0, NULL);

-- 表：table_fontLibrary
DROP TABLE IF EXISTS table_fontLibrary;
CREATE TABLE table_fontLibrary (font_id INT PRIMARY KEY, url CHAR (256), hash_key INT);

-- 表：table_layout
DROP TABLE IF EXISTS table_layout;
CREATE TABLE table_layout (layout_id INT PRIMARY KEY, url CHAR (256), hash_key INT);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
