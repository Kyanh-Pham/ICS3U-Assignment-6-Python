#!/usr/bin/env python3
# Created by: Kyanh Pham
# Created on: Nov 2022
# This program finds the area of a triangle


def calculate_triangle_area(base: int, height: int) -> float:
    # This function calculates volume

    if base <= 0 or height <= 0:
        area = float(-1)
        return area
    else:
        area = float(base * height) / 2
        return area


def main():
    # This function gets the volume

    # Input
    base_from_user = input("Enter the triangle's base length(cm):")
    height_from_user = input("Enter the triangle's height(cm): ")

    try:
        base_from_user = float(base_from_user)
        height_from_user = float(height_from_user)
        # call functions
        final_area = calculate_triangle_area(base_from_user, height_from_user)
        if final_area == -1:
            print("Invalid Input")
        else:
            print(
                "The area of this triangle with the base of {0} cm and height  of {1} cm is {2} cm².".format(
                    base_from_user, height_from_user, final_area
                )
            )
    except ValueError:
        print("Invalid Input")

    print("\nDone.")


if __name__ == "__main__":
    main()
