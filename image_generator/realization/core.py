import PIL.Image
import PIL.ImageDraw
import PTS

from image_generator.utils import calculatePositionVerticalCenter, getPilData


DIRECTORY = '/'.join(__file__.replace('\\', '/').split('/')[:-1] + [''])
REALIZATION_BASE = DIRECTORY + 'realization_base.png'

def createRealization(topText, bottomText, color = (0, 0, 0), topColor = None, bottomColor = None, font = 'consolas', topFont = None, bottomFont = None):
    """
    Create a Realization meme.
    :param topText:     The text to put in the top of the Drake meme.
    :param bottomText:  The text to put in the bottom of the Drake meme.
    :param color:       A PIL compatible color code for the text color.
    :param topColor:    The color to use for the top text. If not specified,
                        this will default to the value of color.
    :param bottomColor: The color to use for the bottom text. If not specified,
                        this will default to the value of color.
    :param font:        A font name that has been loaded into the PTS module.
    :param topFont:     The name of the font to use for the top text.
    :param font:        A font name that has been loaded into the PTS module.
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
    topTextFinal = PTS.fitText(topText, 467, 242, topFont, fast = True)
    if topTextFinal is None:
        raise OverflowError('Top text is too long to fit in the specified space')

    bottomTextFinal = PTS.fitText(bottomText, 467, 242, bottomFont, fast = True)
    if bottomTextFinal is None:
        raise OverflowError('Top text is too long to fit in the specified space')

    # Determine exactly where to put the text.
    posTop = calculatePositionVerticalCenter(2, 2, 242, topTextFinal[1].getsize_multiline(topTextFinal[0])[1])
    posBottom = calculatePositionVerticalCenter(2, 250, 242, bottomTextFinal[1].getsize_multiline(bottomTextFinal[0])[1])

    # Load the template image.
    im = PIL.Image.open(REALIZATION_BASE)
    draw = PIL.ImageDraw.ImageDraw(im)

    # Place the text in the image.
    draw.text(posTop, topTextFinal[0], topColor, topTextFinal[1])
    draw.text(posBottom, bottomTextFinal[0], bottomColor, bottomTextFinal[1])

    # Save the data and return it as a png image.
    out = getPilData(im)
    im.close()
    return out
