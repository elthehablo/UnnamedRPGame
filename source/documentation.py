import combat

class Documentation:
    @staticmethod
    def readDocumentation(entry):
        match(entry):
            case "Combat":
                print(help(combat))
            case _:
                print("Not a valid docstring")