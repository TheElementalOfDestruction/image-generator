import io

import PIL.Image
import PIL.ImageDraw
import PTS


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

def topTextBottomText(topText, bottomText, color = (0, 0, 0), topColor = None, bottomColor = None, font = 'consolas', topFont = None, bottomFont = None, basePath = None, topTextCorner = None, topTextSize = None, bottomTextCorner = None, bottomTextSize = None):
    """
    Function used for creating a meme in the "top text, bottom text" format.
    :param topText:          The text to put in the top of the Drake meme.
    :param bottomText:       The text to put in the bottom of the Drake meme.
    :param color:            A PIL compatible color code for the text color.
    :param topColor:         The color to use for the top text. If not
                             specified, this will default to the value of color.
    :param bottomColor:      The color to use for the bottom text. If not
                             specified, this will default to the value of color.
    :param font:             A font name that has been loaded into the PTS
                             module.
    :param topFont:          The name of the font to use for the top text.
    :param font:             A font name that has been loaded into the PTS
                             module.
    :param basePath:         The path to the base image to be used.
    :param topTextCorner:    The top left corner of the top text box.
    :param topTextSize:      The size (a width, height tuple) of the top text
                             box.
    :param bottomTextCorner: The top left corner of the bottom text box.
    :param bottomTextSize:   The size (a width, height tuple) of the bottom text
                             box.
    """
    # Check that top text and bottom text are not empty
    if not topText:
        raise ValueError(':param topText: must not be empty.')
    if not bottomText:
        raise ValueError(':param bottomText: must not be empty.')

    # Set the colors.
    topColor = topColor or color
    bottomColor = bottomColor or color

    # Set the fonts.
    topFont = topFont or font
    bottomFont = bottomFont or font

    # Prepare the text.
    topTextFinal = PTS.fitText(topText, topTextSize[0], topTextSize[1], topFont, fast = True)
    if topTextFinal is None:
        raise OverflowError('Top text is too long to fit in the specified space')

    bottomTextFinal = PTS.fitText(bottomText, bottomTextSize[0], bottomTextSize[1], bottomFont, fast = True)
    if bottomTextFinal is None:
        raise OverflowError('Top text is too long to fit in the specified space')

    # Determine exactly where to put the text.
    posTop = calculatePositionVerticalCenter(topTextCorner[0], topTextCorner[1], topTextSize[1], topTextFinal[1].getsize_multiline(topTextFinal[0])[1])
    posBottom = calculatePositionVerticalCenter(bottomTextCorner[0], bottomTextCorner[1], bottomTextSize[1], bottomTextFinal[1].getsize_multiline(bottomTextFinal[0])[1])

    # Load the template image.
    with PIL.Image.open(basePath) as im:
        draw = PIL.ImageDraw.ImageDraw(im)

        # Place the text in the image.
        draw.text(posTop, topTextFinal[0], topColor, topTextFinal[1])
        draw.text(posBottom, bottomTextFinal[0], bottomColor, bottomTextFinal[1])

        # Save the data and return it as a png image.
        return getPilData(im)
