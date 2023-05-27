import importer

def main():
    #TODO: code to execute main program
    pathing = importer.ImportHandler("resources/creatures.txt")
    newarray = pathing.ImportAllCreatures()
    value = pathing.ImportCreatureStat(0, 1)
    print(newarray)
    print("value is: "+value.decode('UTF-8'))
    return

if __name__ == "__main__":
    main()