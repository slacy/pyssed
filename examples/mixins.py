import pyssed

background = pyssed.style('background: #123456')
italic = pyssed.style('font-style: italic')
bold = pyssed.style('font-weight: bold')
blue = pyssed.style('color: blue')

blue_ul = pyssed.style({'ul': {'background': 'blue'}})

css = {
    'a:hover': background + italic,
    'a:visited': background + bold + blue,
    '.someclass': blue_ul + {
        'a:visited': italic,
    },
    '.anotherclass': blue_ul + {
        'a:visited': bold,
    },
}

print "\n".join(pyssed.generate(css))
