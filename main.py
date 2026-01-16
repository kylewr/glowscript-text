GlowScript 3.1 VPython
import random # For random color generation only

text = input("Enter text to generate: ")

# First element of list is the space after a letter
# Second element of list is space before a letter
# Spaces after a letter are to signify a letter space
# Spaces before are to make sure things dont overlap
# Everything else in the list defines shape
A = [4, 0, {'type': 'curve', 'xDiff': 0, "yPos": 0, "radius": "0.5", "curve": [[0, -2.5], [1.5, 2], [3, -2.5]]}, {'type': 'ellipsoid', "xDiff": 1.5, "yPos": -1, "axis": vec(0, 0, 0), "size": vec(2, 1, 1)}, {'type': 'sphere', "xDiff": 0, "yPos": -2.5, "radius": 0.5}]
B = [4, 0, {'type': 'curve', "xDiff": 0, "yPos": -2.5, "radius": 0.5, "curve":[[0, 0], [2.25, 0], [3, 0.625], [3, 1.875], [2.25, 2.5], [0, 2.5], [2.25, 2.5], [3, 3.125], [3, 4.375], [2.25, 5], [0, 5, 0], [0, 0]]}]
C = [1, 3.5, {'type': 'curve', "xDiff": 0, "yPos": -2.5, "radius": 0.5, "curve": [[0, 0], [-0.75, -0.5], [-1.5, -0.75], [-2.25, -0.5], [-3, 0], [-3.5, 1], [-3.5, 3.25], [-3, 4.25], [-2.25, 4.75], [-1.5, 5], [-0.75, 4.75], [0, 4.25]]}, {'type': 'sphere', "xDiff": 0, "yPos": -2.5, "radius": 0.5}]
D = [4, 0, {'type': 'curve', "xDiff": 0, "yPos": -2.5, "radius": 0.5, "curve": [[0, 0], [1.5, 0], [2.5, 0.5], [3, 1.5], [3, 3.5], [2.5, 4.5], [1.5, 5], [0, 5], [0, 0]]}]
E = [3.5, 0, {'type': 'box', "xDiff": 0, "yPos": 0, "length": 1, "height": 4}, {'type': 'arrow', "xDiff": -0.5, "yPos": 2, "axis": vec(4, 0, 0), "shaftwidth": 1, "headlength": 1.5, "headwidth": 1.5, "round": False}, {'type': 'box', "xDiff": 0.5, "yPos": 0, "length": 2, "height": 1}, {'type': 'box', "xDiff": 0.75, "yPos": -2, "length": 2.5, "height": 1}]
F = [4, 0, {'type': 'box', "xDiff": 0, "yPos": 0, "length": 1, "height": 4}, {'type': 'arrow', "xDiff": -0.5, "yPos": 2, "axis": vec(4, 0, 0), "shaftwidth": 1, "headlength": 1.5, "headwidth": 1.5, "round": False}, {'type': 'box', "xDiff": 0.5, "yPos": 0, "length": 2, "height": 1}]
G = [1, 3, {'type': 'curve', "xDiff": 0, "yPos": -2.5, "radius": 0.5, "curve": [[-1.5, 1.5], [0, 1.5], [0, 0], [-0.75, -0.5], [-1.5, -0.75], [-2.25, -0.5], [-3, 0], [-3.5, 1], [-3.5, 3.25], [-3, 4.25], [-2.25, 4.75], [-1.5, 5], [-0.75, 4.75], [0, 4.25]]}, {'type': 'sphere', "xDiff": -1.5, "yPos": -1, "radius": 0.5}]
H = [1, 2, {'type': 'box', "xDiff": 0, "yPos": -0.5, "length": 1, "height": 4}, {'type': 'pyramid', "xDiff": 0, "yPos": 1.5, "axis": vec(0, 1, 0)}, {'type': "arrow", 'xDiff': -2, 'yPos': 2.5, 'axis': vec(0, -7, 0), 'shaftwidth': 1, 'round': True}, {'type': 'box', "xDiff": -1, "yPos": 0, "length": 2, "height": 1}]
I = [1, 0, {'type': 'cylinder', "xDiff": 0, "yPos": -2.5, "axis": vec(0, 3, 0), "radius": 0.5}, {'type': 'sphere', "xDiff": 0, "yPos": 1.5, 'radius': 0.75}]
J = [4, 2, {'type': 'extrusion', "xDiff": 0, "yPos": 0, "shape": [[0, 1.5], [0, -2.5], [1, -2.5], [1, -1.5], [2, -1.5], [2, -3.5], [-1, -3.5], [-1, 1.5], [0, 1.5]]}, {'type': 'box', "xDiff": 0.5, "yPos": 2, "length": 6, "height": 1}]
K = [3, 0, {'type': 'arrow', "xDiff": 0, "yPos": -2.5, "axis": vec(0, 6, 0), "shaftwidth": 1, "headlength": 1.5, "headwidth": 1.5, "round": True}, {'type': 'pyramid', "xDiff": 2.5, "yPos": 2.5, "axis": vec(-2.75, -2.75, 0), "height": 1.75}, {'type': 'box', "xDiff": 1.25, "yPos": -1.25, "axis": vec(2.5, -2.5, 0), "width": 0.5}]
L = [4, 0, {'type': 'sphere', "xDiff": 0, "yPos": 2.5, "radius": 0.75}, {'type': 'sphere', "xDiff": 0, "yPos": -2.5, "radius": 0.75}, {'type': 'sphere', "xDiff":3, "yPos": -2.5, "radius": 0.75}, {'type': 'curve', "xDiff": 0, "yPos": -2.5, "radius": 0.5, "curve": [[0, 5], [0, 0], [3, 0]]}]
M = [6, 0, {'type': 'curve', "xDiff": 0, "yPos": -2.5, "radius": 0.5, "curve": [[0, 0], [0, 5], [2.5, 2.5], [5, 5], [5, 0]]}, {'type': 'sphere', "xDiff": 0, "yPos": -2.5, "radius": 0.5}]
N = [4, 0, {'type': 'curve', "xDiff": 0, "yPos": -2.5, "radius": 0.5, "curve": [[0, 0], [0, 5], [3, 0], [3, 5]]}, {'type': 'sphere', "xDiff": 0, "yPos": -2.5, "radius": 0.5}]
O = [3, 1, {'type': 'curve', "xDiff": 0, "yPos": -2.5, "radius": 0.5, "curve": [[0, 0], [-0.5, 0], [-1, 0.2], [-1.3, 0.7], [-1.5, 1.5], [-1.5, 3.5], [-1.3, 4.3], [-1, 4.8], [-0.5, 5], [0, 5], [0.5, 5], [1, 4.8], [1.3, 4.3], [1.5, 3.5], [1.5, 1.5], [1.3, 0.7], [1, 0.2], [0.5, 0], [0, 0]]}]
P = [4, 0, {'type': 'box', "xDiff": 0, "yPos": 0, "length": 1, "height": 5}, {'type': 'ring', "xDiff": 1.5, "yPos": 1, "axis": vec(0, 0, 1), "radius": 1.25, "thickness": 0.5}]
Q = [2.5, 1, {'type': 'curve', "xDiff": 0, "yPos": -2.5, "radius": 0.5, "curve": [[0, 0], [-0.5, 0], [-1, 0.2], [-1.3, 0.7], [-1.5, 1.5], [-1.5, 3.5], [-1.3, 4.3], [-1, 4.8], [-0.5, 5], [0, 5], [0.5, 5], [1, 4.8], [1.3, 4.3], [1.5, 3.5], [1.5, 1.5], [1.3, 0.7], [1, 0.2], [0.5, 0], [0, 0]]}, {'type': 'curve', "xDiff": 0, "yPos": -1, "radius": 0.5, "curve": [[0, 1.5], [2, 0]]}, {'type': 'sphere', "xDiff": 0, "yPos": 0.5, "radius": 0.5}]
R = [4, 0, {'type': 'box', "xDiff": 0, "yPos": 0, "length": 1, "height": 5}, {'type': 'ring', "xDiff": 1.5, "yPos": 1, "axis": vec(0, 0, 1), "radius": 1.25, "thickness": 0.5}, {'type': 'box', "xDiff": 2, "yPos": -1.25, "axis": vec(2, -2.5, 0), "width": 1}]
S = [1, 3, {'type': 'curve', "xDiff": 0, "yPos": 2, "radius": 0.5, "curve": [[0, 0], [-0.5, 0.5], [-1.5, 0.75], [-2.5, 0.5], [-3, 0], [-3, -1.25], [-2.25, -1.75], [-0.75, -2], [0, -2.5], [0, -3.75], [-0.5, -4.25], [-1.5, -4.5], [-2.5, -4.25], [-3, -3.75]]}, {'type': 'sphere', "xDiff": 0, "yPos": 2, "radius": 0.5}]
T = [4, 2, {'type': 'box', "xDiff": 0, "yPos": 0, "length": 1, "height": 5}, {'type': 'arrow', "xDiff": -2.5, "yPos": 2.5, "axis": None, "length": 6, "shaftwidth": 1, "headwidth": 1.5, "headlength": 2, "round": False}]
U = [2, 1, {'type': 'curve', "xDiff": 0, "yPos": -2.5, "radius": 0.5, "curve": [[1.5, 4.5], [1.5, 1.5], [1.3, 0.7], [1, 0.2], [0.5, 0], [0, 0], [-0.5, 0], [-1, 0.2], [-1.3, 0.7], [-1.5, 1.5], [-1.5, 4.5]]}, {'type': 'sphere', "xDiff": 1.5, "yPos": 2, "radius": 0.5}]
V = [2.5, 2, {'type': 'box', "xDiff": -1, "yPos": 0.25, "axis": vec(-2, 5, 0), "width": 1}, {'type': 'box', "xDiff": 1, "yPos": 0.25, "axis": vec(2, 5, 0), "width": 1}, {'type': 'cylinder', "xDiff": 0, "yPos": -2, "axis": vec(0, 0, 0.5), "radius": 1}, {'type': 'cylinder', "xDiff": 0, "yPos": -2, "axis": vec(0, 0, -0.5), "radius": 1}]
W = [5, 0, {'type': 'curve', "xDiff": 0, "yPos": 2.5, "radius": 0.5, "curve": [[0, 0], [1, -5], [2, -2.5], [3, -5], [4, 0]]}, {'type': 'sphere', "xDiff": 0, "yPos": 2.5, "radius": 0.5}]
X = [2, 1, {'type': 'box', "xDiff": 0, "yPos": 0, "axis": vec(-3, -5, 0), "width": 1}, {'type': 'box', "xDiff": 0, "yPos": 0, "axis": vec(3, -5, 0), "width": 1}]
Y = [3, 2, {'type': 'arrow', "xDiff": 0, "yPos": 0.5, "axis": vec(0, -3.5, 0), "shaftwidth": 0.75, "headwidth": 1.25, "headlength":1.5, "round": True}, {'type': 'box', "xDiff": -1, "yPos": 1, "axis": vec(-2, -2, 0), "length": 0.75, "height": 3.5}, {'type': 'box', "xDiff": 1, "yPos": 1, "axis": vec(2, -2, 0), "length": 0.75, "height": 3.5}]
Z = [3.5, 0, {'type': 'curve', "xDiff": 0, "yPos": 2, "radius": 0.5, "curve": [[0, 0], [3, 0], [0, -5], [3, -5]]}, {'type': 'sphere', "xDiff": 0, "yPos": 2, "radius": 0.5}]
COMMA = [1, 0, {'type': 'curve', "xDiff": 0, "yPos": -2.5, "radius": 0.5, "curve": [[0, 0], [0, -0.5], [-0.5, -1]]}, {'type': 'sphere', "xDiff": 0, "yPos": -2.5, "radius": 0.5}]
PERIOD = [1, 0, {'type': 'arrow', "xDiff": 0, "yPos": -2, "axis": vec(0, 0, 0.5), "round": True, "shaftwidth": 0.75, "headwidth": 1}]
APOSTROPHE = [1, 0, {'type': 'curve', "xDiff": 0, "yPos": 2.5, "radius": 0.5, "curve": [[0, 0], [0, -0.5], [-0.5, -1]]}, {'type': 'sphere', "xDiff": 0, "yPos": 2.5, "radius": 0.5}]
QUESTION_MARK = [4, 0, {'type': 'curve', "xDiff": 0, "yPos": 0, "radius": 0.5, "curve": [[0, 2],[0.5, 2.5], [1.5, 2.75], [2.5, 2.5], [3, 2], [3, 1.25], [2.25, 0.75], [1.5, 0], [1.5, -1]]}, {'type': 'sphere', "xDiff": 0, "yPos": 2, "radius": 0.5}, {'type': 'sphere', "xDiff": 1.5, "yPos": -2.5, "radius": 0.5}]
EXCLAMATION_MARK = [1, 0, {'type': 'cone', "xDiff": 0, "yPos": 4, "axis": vec(0, -5.75, 0), "radius": 1}, {'type': 'sphere', "xDiff": 0, "yPos": -2.5, "radius": 0.5}, {'type': 'sphere', "xDiff": 0, "yPos": 4.2, "radius": 1}]
SPACE = [3, 0] # Already complete, does not require any objects, only post-spaces
        
def generate(text, rand=True): # Need to add support for spaces
    letterPos = [((-len(text)/2) - 4) + i for i in range(len(text))] # Splits letters in half and generates a tuple of all (base; will be manipulated by letter spacing) X points for each letter
    letter = {"a":A, "b":B, "c":C, "d":D, "e":E, "f":F, "g":G, "h":H, "i":I, "j":J, "k":K, "l":L, "m":M, "n":N, "o":O, "p":P, "q":Q, "r":R, "s":S, "t":T, "u":U, "v":V, "w":W, "x":X, "y":Y, "z":Z, ",":COMMA, "'":APOSTROPHE, ".":PERIOD, "?":QUESTION_MARK, "!":EXCLAMATION_MARK, " ":SPACE} # Dict for str -> tuple translations
    charIter = 0 # character loop iteration counter
    for char in text:
        nextChar = charIter + 1
        genLet = letter[char.lower()] # Fetch translation from dict
        x = letterPos[charIter] + genLet[1] # Determining X and adding any pre-spacing values
        letterPos = [lettr + genLet[0] + genLet[1] for lettr in letterPos] # Set letterPos to manipulate all X values for next letters based on the current pre/post spacing
        if rand: color = vec(random.random(), random.random(), random.random())
        else: color = color.blue
        for obj in genLet:
            # Check object type and create that object based on the parameters from the dict in the letters defined near the top of the file
            if obj['type'] == 'arrow':
                if obj['axis']:
                    arrow(pos=vec(x + obj['xDiff'], obj['yPos'], 0), axis=obj['axis'], color=color, shaftwidth=obj['shaftwidth'], round=obj['round'])
                else:
                    arrow(pos=vec(x + obj['xDiff'], obj['yPos'], 0), length=obj['length'], color=color, shaftwidth=obj['shaftwidth'], round=obj['round'])
                try:
                    arrow.headwidth = obj['headwidth']
                    arrow.headlength = obj['headlength']
                except: pass
            elif obj['type'] == 'box':
                try:
                    box(pos=vec(x + obj['xDiff'], obj['yPos'], 0), axis=obj['axis'], length=obj['length'], height=obj['height'], color=color)
                except:
                    try:
                        box(pos=vec(x + obj['xDiff'], obj['yPos'], 0), axis=obj['axis'], width=obj['width'], color=color)
                    except:
                        box(pos=vec(x + obj['xDiff'], obj['yPos'], 0), length=obj['length'], height=obj['height'], color=color)
            elif obj['type'] == 'pyramid':
                pyramid(pos=vec(x + obj['xDiff'], obj['yPos'], 0), axis=obj['axis'], color=color)
            elif obj['type'] == 'cylinder':
                cylinder(pos=vec(x + obj['xDiff'] , obj['yPos'], 0), axis=obj['axis'], color=color, radius=obj['radius'])
            elif obj['type'] == 'sphere':
                sphere(pos=vec(x + obj['xDiff'], obj['yPos'], 0), radius=obj['radius'], color=color)
            elif obj['type'] == 'curve':
                c = curve(radius=obj['radius'], color=color)
                for curvePoint in obj['curve']: c.append(vec(x + curvePoint[0] + obj['xDiff'], curvePoint[1] + obj['yPos'], 0))
            elif obj['type'] == 'ellipsoid':
                ellipsoid(pos=vec(x + obj['xDiff'], obj['yPos'], 0), axis=obj['axis'], color=color, size=obj['size'])
            elif obj['type'] == 'extrusion':
                shape = [[obj['shape'][i][0] - (x + obj['xDiff']), obj['shape'][i][1] + obj['yPos']] for i in range(len(obj['shape']))]
                extrusion(path=[vec(0, 0, -0.5), vec(0, 0, 0.5)], shape=shape, color=color)
            elif obj['type'] == 'cone':
                cone(pos=vec(x + obj['xDiff'], obj['yPos'], 0), axis=obj['axis'], color=color, radius=obj['radius'])
            elif obj['type'] == 'ring':
                ring(pos=vec(x + obj['xDiff'], obj['yPos'], 0), axis=obj['axis'], color=color, radius=obj['radius'], thickness=obj['thickness'])
        charIter += 1
    return [letter[c] for c in text]
    
generate(text)
