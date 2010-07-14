import pyssed

# You can use a variety of syntaxes to specify your styles.  The middle dict
# form is preferred, because CSS uses dash-separated names for things like
# font-weight, which can only be expressed via the dict form.
red = pyssed.style('color: red;')
green = pyssed.style({'color': 'green'})
blue = pyssed.style(color='blue')

# You can even mix & match them, but this isn't really recommended.
aqua_bold = pyssed.style('color: aqua;', {
        'font-weight': 'bold'},
                         background='blue')

css = {
    '.red': red,
    '.green': green,
    '.blue': blue,
    '.aquabold': aqua_bold,
    '.bluebold': blue + {
        'font-weight': 'bold',
    }
}

print "\n".join(pyssed.generate(css))
