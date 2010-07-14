import pyssed


def size(width=None, height=None):
    result = {}
    if width:
        result.update({'width': width})
    if height:
        result.update({'height': height})
    return result

css = {
    'div.square': size(100, 100),
    'div.rect': size(40, 30),
    'div.wide': size(1024),
    'div.tall': size(height=800),
}

print '\n'.join(pyssed.generate(css))
