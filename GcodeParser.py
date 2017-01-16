class parser:

    def __init__(self):
        self.Gcode = []
        self.filePath = None

    def loadGcode(self, Path):
        # Open file specified and read g code into list by line
        self.filePath = Path

        with open(self.filePath, 'r') as f
            self.Gcode = f.read().splitlines()

    def splitLine(self, Line):
        result = dict()

        for i in Line.split(' '):
            Code = i[0]
            Value = i[1:]
    
            if Code == 'X' or Code == 'Y':
                Value = float(Value)
            else:
                Value = int(Value)
        
            result[Code] = Value
        
        return(result)

