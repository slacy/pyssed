import pyssed

css = {
    'a:hover': {
        'font-weight': 'bold',
    }
}

print '\n'.join(pyssed.generate(css))
