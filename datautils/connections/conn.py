import re

def expandMacros(query) :
    """
    This function is a query preprocessor.  It looks for date 
    macros and substitutes the appropriate values
    """
    pattern = re.compile("${}")

class Connection(object) :
    def __init__(self, auth) :
        self.auth = auth
        self.authenticate() 
        
    def authenticate(self) :
        pass

    def query(self, query) :
        pass

    def getData(self, query) :
        pass

    def insert(self, data) :
        pass

    def commit(self) :
        pass
