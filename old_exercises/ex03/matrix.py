class MatrixException(Exception):
    def __init__(self, message):
        super().__init__(message)


class Matrix():
    def __init__(self, *args):
        if len(args) == 1:
            pass
        elif len(args) == 2:
            # if not isinstance(args[1], tuple):
            #     return
            self.data = [float(nbr) for nbr in [lst for lst in args[0]]]
            self.shape = args[1]
        else:
            raise MatrixException("You must provide one or two arguments")
