import pyssed

red = pyssed.style('color: red')
green = pyssed.style('color: green')
bold = pyssed.style('font-weight: bold')

css = {
    'a:hover': red + bold,
    'a:visited': green + bold,
    'a:link': bold + {
        'color': 'purple',
    },
}

print '\n'.join(pyssed.generate(css))
