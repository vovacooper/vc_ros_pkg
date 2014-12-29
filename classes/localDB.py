import json

DB_FILE_DIR = "/var/www/vc_ros_pkg/static/admin/db/localDB.json"

class localDB:
    """Singleton
    _instance = None
    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance
    """

    @staticmethod
    def getData(path=DB_FILE_DIR):
        _json_data_file = open(path)
        _json_data = _json_data_file.read()
        data = json.loads(_json_data)
        _json_data_file.close()
        return data

    @staticmethod
    def saveData(object, path=DB_FILE_DIR):
        f = open(path, 'w')
        json.dump(object, f)


"""##########################################################
                TEST
###########################################################"""
if __name__ == "__main__":
    a = {
        "a": "b",
        "c": "d"
    }
    localDB.saveData(a)
    b = localDB.getData()
    print a
    print b
    print "end"
