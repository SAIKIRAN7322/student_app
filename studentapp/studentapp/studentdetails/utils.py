import enum

class gradesenumtypes(enum.Enum):

    A = "A"
    B = "B"
    C = "C"
    D = "D"



    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)
