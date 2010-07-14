import pyssed

red = pyssed.style('color: red')
blue = pyssed.style(color='blue')
green = {'color': 'green'}
bold = pyssed.style('font-weight: bold')
red_bold = red + bold


def rounded(radius):
    return pyssed.style({
        'border-radius': radius,
        '-moz-border-radius': radius,
        '-webkit-border-radius': radius,
        })

css = {
    '.blue': blue,
    '.green': green,
    'ul li': rounded(3) + blue + {
        'font-style': 'italic',
    },
    'div.ground': rounded(7) + green + {
        'p': {
            'text-align': 'left',
            'em' : {
                'font-size': '14pt'
            }
        },
    }
}

print '\n'.join(pyssed.generate(css=css))
