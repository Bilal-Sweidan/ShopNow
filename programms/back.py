import sqlite3
programms = sqlite3.connect("programms.db")
pr = programms.cursor()
pr.execute("create table if not exists programms (name text,img url,price integer,info text)")
pr.execute("insert into programms(name, img, price, info ) values('photoshop','img\photoshop.png',11,'programm for editing on any image')")
programms.commit()
programms.close()