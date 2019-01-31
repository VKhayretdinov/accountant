import sqlite3


def search_by_inn(req):
    conn = sqlite3.connect('info.db')
    cursor = conn.cursor()

    req_number = "SELECT * FROM number WHERE ИННЮЛ = " + req
    res = cursor.execute(req_number).fetchone()

    req_nalog = "SELECT * FROM nalog WHERE ИННЮЛ = " + req
    res_tmp = cursor.execute(req_nalog).fetchone()

    req_gruppa = "SELECT * FROM gruppa WHERE ИННЮЛ = " + req
    res_tmp1 = cursor.execute(req_gruppa).fetchone()

    result = {}

    if res:
        result['name'] = res[0]
        result['INN'] = res[1]
    elif res_tmp:
        result['name'] = res_tmp[0]
        result['INN'] = res_tmp[1]
    elif res_tmp1:
        result['name'] = res_tmp1[0]
        result['INN'] = res_tmp1[1]
    else:
        return {}

    if res:
        result['sumWorker'] = res[2]
    if res_tmp:
        result['ESHN'] = res_tmp[2]
        result['USN'] = res_tmp[3]
        result['ENVD'] = res_tmp[4]
        result['SRP'] = res_tmp[5]
    if res_tmp1:
        result['UchKGN'] = res_tmp1[2]

    print(result)
    return result
