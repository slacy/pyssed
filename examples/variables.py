import pyssed

radius = 5

css = {
  'div.round': {
    'border-radius': radius,
    '-moz-border-radius': radius,
    '-webkit-border-radius': radius,
  }
}

print '\n'.join(pyssed.generate(css=css))

