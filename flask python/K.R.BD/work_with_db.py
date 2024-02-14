from DBcm import DBContextManager



def select_dict(config: dict, _sql: str):
    with DBContextManager(config) as cursor:
        if cursor is None:
            raise ValueError('Курсор не создан')
        else:
            cursor.execute(_sql)
            result = cursor.fetchall()
            if result:
                schema = [item[0] for item in cursor.description]
                result_dict = []
                for product in result:
                    result_dict.append(dict(zip(schema, product)))
                return result_dict
            else:
                return None