from pcinput import getInteger

def triangleArea( bottom, height ):
    while True:
        side = getInteger( bottom )
        if side <= 0:
            print( "A side cannot have a negative value!" )
            continue
        break
    while True:
        height_value = getInteger( height )
        if height_value <= 0:
            print( "A triangle cannot have a negative height!." )
            continue
        break
    area = 0.5 * side * height_value
    return area

def main():
    prompt1 = "Enter the value for the bottom side: "
    prompt2 = "Enter the value for the triangle height: "
    print( "The area for the triangle is:", triangleArea( prompt1, prompt2 ) )

if __name__ == '__main__':
    main()
