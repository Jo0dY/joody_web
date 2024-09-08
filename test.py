from flask import Blueprint, request, reder_template, flash, redirect, url_for
from flask import current_app as current_app

from app.module import dbModule

test=Blueprint('test',__name__, url_prefix='/test')
@test.route('/',methods=['GET'])
def index():
    return render_template('/test/test.html',
                            result=None,
                            resultDate=None,
                            resultUPDATE=None)


@test.route('/insert', methods=[GET])
def insert():
    db_class = dbModule.Database()

    sql      ="INSERT INTO testDB.testTable(test) \
               VALUES('%s')" % ('testData')
    
    db_class.execute(sql)
    db_class.commit()

    return reder_template('/test/test.html',
                          result='insert is done!',
                          resultDate=None,
                          resultUPDATE=None)




@test.route('/select', methods=[GET])
def select():
    db_class = dbModule.Database()

    sql      ="SELECT idx, test \
               FROM testDB.testTable"
    row      = db_class.executeAll(sql)

    print(row)
    
    return reder_template('/test/test.html',
                          result=None,
                          resultDate=row[0],
                          resultUPDATE=None)



@test.route('/update', methods=[GET])
def update():
    db_class = dbModule.Database()

    sql      ="UPDATE testDB.testTable \
               SET test='%s'\
               WHERE test='testDate'"%('update_Data')

    
    db_class.execute(sql)
    db_class.commit()

    sql      ="SELECT idx, test \
                FROM testDB.testTable"
    row      = db_class.executeAll(sql)

    return reder_template('/test/test.html',
                          result=None,
                          resultDate=None,
                          resultUPDATE=row[0])

