def slice(text, a, b, c, d):
    return text[a:b+1] + ' ' + text[c:d+1]

text = 'Idr53M4hDPnrLDmgijbp8TLik5GOq5HN5iLCuNe0tmwVabVYj7pslorZEpZEMacrorhamphusVNeJMtWqjQvnx9j1mZPSKjzqPDcLS3xhlEM66tKizj32RKlOgscRl2ADFOjr47bmWQ5wq3FYVbonasusR4ltkUg9f4qoYgVo1i6Pa2mwB.'
print(slice(text, 60, 72, 146, 152))