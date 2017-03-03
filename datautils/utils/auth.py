from ..exceptions import *

MYSQL=1
HIVE=2

class Authorization(object) :
    def __init__(self, user=None, passwd=None, host=None, port=None, database=None, type=None) :
        self.user = user
        self.passwd = passwd
        self.host = host
        self.port = port
        self.database = database
        self.type = type

        self.validate()

    def validate(self) :
        if self.type is None :
            print "no type"
            raise NoTypeError("An Auth object must have a type specified")

        if self.type == MYSQL :
            print "mysql fail"
            if (self.user is None) or (self.passwd is None) or (self.host is None) :
                raise MissingCredentialsError("For a MySQL connection; user, passwd, and host are required fields")

        if self.type == HIVE :
            print "hive fail"
            if (self.host is None) or (self.port is None) :
                raise MissingCredentialsError("For a Hive connection; host and port are required fields")

    def __str__(self) :
        pass
