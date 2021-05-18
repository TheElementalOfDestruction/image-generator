import io


def calculatePositionFullCenter(textBoxCornerX, textBoxCornerY, textBoxWidth, textWidth, textBoxHeight, textHeight):
    return (textBoxCornerX + ((textBoxWidth - textWidth) / 2), textBoxCornerY + ((textBoxHeight - textHeight) / 2))

def calculatePositionHorizontalCenter(textBoxCornerX, textBoxCornerY, textBoxWidth, textWidth):
    return (textBoxCornerX + ((textBoxWidth - textWidth) / 2), textBoxCornerY)

def calculatePositionVerticalCenter(textBoxCornerX, textBoxCornerY, textBoxHeight, textHeight):
    return (textBoxCornerX, textBoxCornerY + (textBoxHeight/2) - (textHeight/2))

def getPilData(image):
    """
    Returns the png image data from a PIL image.
    """
    bio = io.BytesIO()
    image.save(bio, 'PNG')
    while bio.tell() != 0:
        bio.seek(0)
    return bio.read()
