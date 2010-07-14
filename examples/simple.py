import pyssed

basic_margin = 24
notification_border_color = "#012233"

sig_background = pyssed.style('background-color: #ede5a8')


def size(width, height):
    return {'width': width,
            'height': height}

css = {
    '.notification': sig_background + {
        'margin-bottom': basic_margin,
        'border': '1px solid %s' % notification_border_color,
        'padding': 6,

        'ul': {
            'margin': 0,
            'padding': 0,
            'list-style-type': 'none',
        }
    },
    '.signature': sig_background + size(200, 54),
}

print '\n'.join(pyssed.generate(css=css))
