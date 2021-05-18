import io

import numpy
import PIL.Image

DIRECTORY = '/'.join(__file__.replace('\\', '/').split('/')[:-1] + [''])
WOLVERINE_BASE = DIRECTORY + 'wolverine base.png'

def find_coeffs(pa, pb):
    matrix = []
    for p1, p2 in zip(pa, pb):
        matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0]*p1[0], -p2[0]*p1[1]])
        matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1]*p1[0], -p2[1]*p1[1]])
    A = numpy.matrix(matrix, dtype=numpy.float)
    B = numpy.array(pb).reshape(8)
    #res = numpy.dot(numpy.linalg.inv(A.T * A) * A.T, B)
    res = numpy.linalg.solve(A, B)
    return numpy.array(res).reshape(8)

def createWolverine(imagedata):
    im = PIL.Image.open(io.BytesIO(imagedata)).convert('RGBA').resize((390, 390), resample = 3).transform(size = (390, 390), method = PIL.Image.PERSPECTIVE, data = find_coeffs(((0, 12), (289, 0), (334, 351), (52, 389)), ((0, 0), (390, 0), (390, 390), (0, 390))), resample=3)
    ret = PIL.Image.new('RGBA', (600, 873), color = (0,  0, 0, 0))
    ret.paste(im, box = (160, 468))
    wolv = PIL.Image.open(WOLVERINE_BASE)
    ret.paste(wolv, mask = wolv)
    bio = io.BytesIO()
    ret.save(bio, 'PNG')
    while bio.tell() != 0:
        bio.seek(0)
    return bio.read()
