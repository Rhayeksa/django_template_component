def sql_to_json(cursor):
    result, key = [], []

    for i in (name[0] for name in cursor.description or ()):
        key.append(i)
    for value in cursor.fetchall():
        result.append(dict(zip(key, value)))
    return result
