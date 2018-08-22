MORSE_CODE = {
	'A': '.-',     'B': '-...',   'C': '-.-.', 
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
 	'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',

    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',

    ' ':'/', '.':'.-.-.-', ',':'--..--',
    ':':'---...', '?':'..--..', "'":'.----.',
    '-':'-....-', '/':'-..-.', '@': '.--.-.',
    '=':'-...-', '(':'-.--.', ')':'-.--.-',
    '+':'.-.-.'
}
MORSE_CODE_REVERSED = {value:key for key,value in MORSE_CODE.items()}

s = open('umbar.txt', 'rb').read()
s = s.replace('nar', '0').replace('akh', '1')
decoded_s = ''.join([chr(int(s[i:i+8], 2)) for i in range(0, len(s), 8)])
coords_s = ''.join(MORSE_CODE_REVERSED.get(i) for i in decoded_s.split())
svg_coords = '<svg width="180" height"180" viewPort="0 0 180 180">'
minx, miny = 100000.0, 1000000.0
for letter in coords_s.split('@'):
    for line in letter.split('//'):
        e1, e2 = line.split('/')
        x1, y1 = e1.split(',')
        x2, y2 = e2.split(',')
        x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
        minx = min(minx, x1, x2)
        miny = min(miny, y1, y2)
for letter in coords_s.split('@'):
    for line in letter.split('//'):
        e1, e2 = line.split('/')
        x1, y1 = e1.split(',')
        x2, y2 = e2.split(',')
        x1, y1, x2, y2 = float(x1), float(y1), float(x2), float(y2)
        svg_coords += '<line x1="{}" y1="{}" x2="{}" y2="{}" stroke-width="2" stroke="black"/>'.format((x1 - minx) * 10000, (y1 - miny) * 10000, (x2 - minx) * 10000, (y2 - miny) * 10000)
svg_coords += '</svg>'
print svg_coords