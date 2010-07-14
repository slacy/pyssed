import pyssed

background = pyssed.style('background: #123456')
italic = pyssed.style('font-style: italic')
bold = pyssed.style('font-weight: bold')
blue = pyssed.style('color: blue')

css = {
    'a:hover': background + italic,
    'a:visited': background + bold + blue,
}

print "\n".join(pyssed.generate(css))
