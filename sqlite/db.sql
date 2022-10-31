PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS 'Users'  (
                                    'uid' VARCHAR(36) DEFAULT 'abcdef00-1234-5678-90ab-1234567890af',
                                    'name' VARCHAR(1024) DEFAULT NULL,
                                    'birth' VARCHAR(10) DEFAULT NULL,
                                    'login' VARCHAR(1024) DEFAULT NULL,
                                    'password' VARCHAR(1024) DEFAULT NULL,
                                    'phone' VARCHAR(12) DEFAULT '+70955005050',
                                    'email' VARCHAR(1024) DEFAULT NULL,
                                    'tg' VARCHAR(1024) DEFAULT NULL,
                                    PRIMARYKEY 'uid'
                                    );
INSERT INTO 'Users' VALUES(1,'00000000-1111-1111-1111-000000000000','Грин','1934-08-22','greg','qawsedrf','+70123456789',NULL,NULL);
INSERT INTO 'Users' VALUES(2,'00000000-2222-2222-2222-000000000000','Коха','1971-05-16','koka','!Q@W#E$R','+70987654321','kkk@mail.ru','@teleg');
INSERT INTO 'Users' VALUES(3,'00000000-3333-3333-3333-000000000000','Вано','1970-12-15','ivan','AzSxDcFv','+74560789123','iv@mail.ru',NULL);

CREATE TABLE 'Errors'   (
                        'code' INT(4) NOT NULL,
                        'text' VARCHAR(1024) DEFAULT NULL,
                        PRIMARYKEY 'code'
                        );
INSERT INTO 'Errors' VALUES(1,200,'OK');
INSERT INTO 'Errors' VALUES(2,300,NULL);
INSERT INTO 'Errors' VALUES(3,400,'Bad Request');
INSERT INTO 'Errors' VALUES(4,500,'Internal Server Error');
COMMIT;
