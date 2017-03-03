import json

class Schema(object) :
    def __init__(self) :
        self.columns = []
        self.length = 0

    def appendCol(self, col) :
        """
        Add a column object to the schema
        """
        self.length += 1
        col.pos(self.length)
        self.columns.append(col)

    def appendSpec(self, spec) :
        """
        append a column from spec, see importSpec for format
        """
        self.length += 1
        self.columns.append(Column(spec['name'], spec['type'], self.length))

    def importSpec(self, spec) :
        """
        the format of the spec is a list of dictionaries that have name and datatype
        e.g. [{'name' : name, 'type' : type}, ...]
        """
        for i, col in enumerate(spec) :
            self.columns.append(Column(col['name'], col['type'], i))

        self.length = len(spec)

    def importFromMySQL(self, dbSchema) :
        pass

class Column(object) :
    def __init__(self, name, type, position=None) :
        self.name = name
        self.type = type
        self.position = position

    def pos(self, position) :
        self.position = position

    def spec(self) :
        return {"name" : self.name, "type" : self.type, "position" : self.position}

class Data(object) :
    """
    The data object is a common interchange format
    """
    def __init__(self, schema=None) :
        self.schema = schema
        self.data = []

    def loadRows(self, rows) :
        """
        Import from a row-list format.  This data is represented as a list of lists with the inner list representing fields, and outer list representing rows.
        """
        self.data = rows

    def exportRows(self) :
        return self.data

    def loadCols(self, cols) :
        """
        Import from columnar list format.  The outer list represents columns while the inner list represents rows.
        This requires that all columns have the same number of rows
        """
        
        if len(cols) > 0 :
            for i in range(len(cols[0])) :
                row = []
                for j in range(len(cols)) :
                    row.append(cols[j][i])
                self.data.append(row)

    def exportCols(self) :
        cols = []
        for j in range(len(self.data[0])) :
            cols.append([])
            for i in range(len(self.data)) :
                cols[j].append(self.data[i][j])

        return cols

