import pyssed

radius = 5

css = {
  'div.round': {
    'border-radius': radius,
    '-moz-border-radius': int(round(radius * 2.0)),
    '-webkit-border-radius': int(round(radius * 1.5)),
  }
}

print '\n'.join(pyssed.generate(css))
