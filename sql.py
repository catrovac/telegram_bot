import sqlite3
import time

a = """ AAAAAA       AAA     AAAAAAAAAAAA   AAAAAAAA     AAAAAAAA  AA           AA     AAA       AAAAAAA  AAAAAAAAA  AAAAAAAA       """
b = """AA     A     AA AA    A    AA    A   AA     AA   AA      AA  AA         AA     AA AA      AA    A  AA      A  AA     AA      """
c = """AA          AA   AA        AA        AA    AA    AA      AA   AA       AA     AA   AA     AA       AA         AA    AA       """
d = """AA         AA     AA       AA        AAAAAAA     AA      AA    AA     AA     AA     AA    AA       AAAAAAA    AAAAAAA        """
e = """AA        AAAAAAAAAAA      AA        AA     AA   AA      AA     AA   AA     AAAAAAAAAAA   AA       AA         AA     AA      """
f = """AA     A  AA       AA      AA        AA      AA  AA      AA      AA AA      AA       AA   AA    A  AA      A  AA      AA     """
j = """ AAAAAA   AA       AA      AA        AA       AA  AAAAAAAA        AAA       AA       AA   AAAAAAA  AAAAAAAAA  AA       AA    """

print("BOT by C.A.T.R.O.V.A.C.E.R")
time.sleep(0.6)

print(
    "---------------------------------------------------------------------------------------------------------------------------------------------")
print()
print(a)
time.sleep(0.2)
print(b)
time.sleep(0.2)
print(c)
time.sleep(0.2)
print(d)
time.sleep(0.2)
print(e)
time.sleep(0.2)
print(f)
time.sleep(0.2)
print(j)
time.sleep(0.2)
print('\n')
print(
    "---------------------------------------------------------------------------------------------------------------------------------------------")

db = sqlite3.connect('account.db')
cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS user(name_session TEXT,
                                                  api_id INTEGER,
                                                  api_hash TEXT)""")
z = input('Добавить нового клиента Y/N :')
if z == 'y' or z == 'Y' or z == 'н' or z == 'Н':
    db = sqlite3.connect('account.db')
    cursor = db.cursor()
    k = int(input('Сколько пользователей Вы хотите добавить?  '))
    for q in range(k + 1):
        name = input('Введите имя сессии :')
        api_id = int(input('Введите api :'))
        api_hash = input('Введите hash :')
        cursor.execute("""INSERT INTO user VALUES(?,?,?)""", (name, api_id, api_hash))
        db.commit()
        print(f'Пользователь {name} {api_id} {api_hash} успешно добавлен!')
        q += 1
    print(q, 'Новых пользователей добавлено')
else:
    data = cursor.execute("""SELECT * FROM user """)
    content = data.fetchall()
p = input('Добавить кошелек крипты?  Y/N :')
if p == 'Y' or p == 'y' or p == 'н' or p == 'Н':
    db = sqlite3.connect('account.db')
    db = sqlite3.connect('account.db')
    cursor = db.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS cript(name TEXT,
                                                       val_case TEXT)""")
    n = int(input(f'Введите количество кошельков  :'))
    for m in range(n):
        name = input('Введите имя кошелька :')
        val_case = input('Введите номер кошелька :')
        cursor.execute("""INSERT INTO cript VALUES (?,?)""", (name, val_case))# name BTC,LTC,DOGE,BCH
        db.commit()
        print(f'кошелек {name} {val_case} успешно добавлен')


datac = cursor.execute("""SELECT * FROM cript""")
val_c = datac.fetchall()
vallet = {}
for name in val_c:
    vallet[name[0]] = name[1]
#print(vallet)
db.close()

