lines = [
    'abbreviatablevfiawhfqfqaq',
    'eddquspdpnmwfggrrgkailtoe',
    'rkawbzvrjapkuplmjpinwormi',
    'outwardsoutwarredvstpgjow',
    'buadpokyqotlromgjnuicedxu',
    'axvjomisunderstanderdseut',
    'cwiydyznrzwdkpggpgeagjznh',
    'tlsorhqghlferetapuvdhhtio',
    'extraembryonicomvndimaqvb',
    'rnimguumvurjjtbedrzaxihig',
    'iicfsyhcllmugictreatyiteu',
    'ogagmjaizkiluvrofboiwntdu',
    'lylcezmppfddbexpqepoyoyxr',
    'oplenfmoraalqnlhilhnrclpz',
    'guygeyahelbxwegytenrkufvs',
    'ixykpcdaialjqswtsxhjzltmy',
    'ccedyrajmqezlsmeysgdhaqce',
    'axpnmlnbpcnbkimcnufymrjvf',
    'ltnapsiloceratanzcddmhjsy',
    'lnquensuslsjvutlhcvtukgyk',
    'yojmnfmaepspaceshipjvknvf',
    'napolcradvmmmsumantdtdjlo',
    'tvbtofigdwifoutscornsjlom',
    'zuoapneicrbluhyvjlhgpubwi',
    'pmjikdytxxtqlhitoakpjftcf'
]

words = open('words.txt', 'rb').read().split("\n")

sorted_words = sorted(words, key=lambda w: len(w), reverse=True)

options = []
options.append('\n'.join(lines))
options.append(''.join(reversed(options[-1])))
v = []
for i in range(len(lines)):
    for j in range(len(lines)):
        v.append(lines[j][i])
    v.append('\n')
options.append(''.join(v[:-1]))
options.append(''.join(reversed(options[-1])))
v = []
for i in range(len(lines)):
    j = 0
    while True:
        try:
            if i < 0 or j < 0:
                raise IndexError
            v.append(lines[i][j])
        except IndexError:
            v.append('\n')
            break
        i -= 1
        j += 1
for j in range(1, len(lines)):
    i = len(lines) - 1
    while True:
        try:
            if i < 0 or j < 0:
                raise IndexError
            v.append(lines[i][j])
        except IndexError:
            v.append('\n')
            break
        i -= 1
        j += 1
options.append(''.join(v[:-1]))
options.append(''.join(reversed(options[-1])))
v = []
for i in reversed(range(len(lines))):
    j = 0
    while True:
        try:
            if i < 0 or j < 0:
                raise IndexError
            v.append(lines[i][j])
        except IndexError:
            v.append('\n')
            break
        i += 1
        j += 1
for j in range(1, len(lines)):
    i = 0
    while True:
        try:
            if i < 0 or j < 0:
                raise IndexError
            v.append(lines[i][j])
        except IndexError:
            v.append('\n')
            break
        i += 1
        j += 1
options.append(''.join(v[:-1]))
options.append(''.join(reversed(options[-1])))
haystack = '\n'.join(options)

for word in sorted_words:
    if word in haystack:
        print(word)
        break

