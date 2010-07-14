import pyssed

site_background = "#123450"
red = pyssed.style('color: red;')
blue = pyssed.style(color='blue')
green = {'color': 'green'}
bold = pyssed.style('font-weight: bold;')
red_bold = red + bold


def rounded(radius):
    return pyssed.style({
        'border-radius': radius,
        '-moz-border-radius': int(round(radius * 1.5)),
        '-webkit-border-radius': int(round(radius * 2.0)),
        })

css = {
    '.blue': blue,
    '.green': green,
    'ul li': rounded(3) + blue + {
        'font-style': 'italic',
        'background': site_background,
    },
    'div.ground': rounded(7) + red_bold + {
        'p': {
            'text-align': 'left',
            'em': {
                'font-size': '14pt',
                'background': site_background,
            }
        },
    }
}

print '\n'.join(pyssed.generate(css))
