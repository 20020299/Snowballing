def floodFill(image, sr, sc, newColor):
    color = image[sr][sc]
    if color != newColor:
        image = fill(image, sr, sc, newColor, color)
    return image


def fill(image, sr, sc, newColor, color):
    if 0 <= sr < len(image) and 0 <= sc < len(image[0]):
        if image[sr][sc] == color:
            image[sr][sc] = newColor

            image = fill(image, sr - 1, sc, newColor, color)
            image = fill(image, sr, sc + 1, newColor, color)
            image = fill(image, sr + 1, sc, newColor, color)
            image = fill(image, sr, sc - 1, newColor, color)

    return image


def main():
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    color = 2
    print(floodFill(image, sr, sc, color))


if __name__ == "__main__":
    main()
