import combat
import dieroller
import drawmap
import importer

class Documentation:
    @staticmethod
    def readDocumentation(entry):
        match(entry):
            case "combat":
                print(help(combat))
            case "dieroller":
                print(help(dieroller))
            case "drawmap":
                print(help(drawmap))
            case "importer":
                print(help(importer))
            case "help":
                print("------------------------------------")
                print("Current classes with documentation: ")
                print("combat, dieroller, drawmap, importer")
                print("------------------------------------")
                print("input 'exit' to exit the game")
            case "exit":
                exit(0)
            case _:
                print("Not a valid docstring")