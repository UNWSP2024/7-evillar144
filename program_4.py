import math

def distance(coord1, coord2):
    return math.sqrt((coord2[0] - coord1[0])**2 + (coord2[1] - coord1[1])**2 + (coord2[2] - coord1[2])**2)

def main():
    try:
        x1, y1, z1 = map(int, input("Enter the first 3D coordinate (x1, y1, z1): ").split(","))
        coord1 = (x1, y1, z1)

        x2, y2, z2 = map(int, input("Enter the second 3D coordinate (x2, y2, z2): ").split(","))
        coord2 = (x2, y2, z2)

        dist = distance(coord1, coord2)

        print(f"The distance between the two points is: {dist}")

    except ValueError:
        print("Invalid input! Please enter the coordinates in the correct format (x, y, z).")

if __name__ == "__main__":
    main()
