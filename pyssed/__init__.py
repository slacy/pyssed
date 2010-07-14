#!/usr/bin/python


class style(object):
    """Represents an array of CSS styles."""

    def __init__(self, *args, **kwargs):
        self._styles = {}
        for a in args:
            self.__add__(a)

        for name, value in kwargs.iteritems():
            self._styles[name] = value

    def iteritems(self):
        return self._styles.iteritems()

    def __add__(self, other):
        if isinstance(other, str):
            single = other.split(':')
            self._styles[single[0]] = single[1]
        elif isinstance(other, dict):
            self._styles.update(other)
        elif isinstance(other, style):
            self._styles.update(other._styles)
        else:
            raise "Bad type for style"
        return self

    def __repr__(self):
        return str(self._styles)


def generate(parent='', css=None):
    indent = 4
    subnodes = []
    stylenodes = []
    result = []

    for name, value in css.iteritems():
        # If the sub node is a sub-style...
        if isinstance(value, dict) or isinstance(value, style):
            subnodes.append((name, value))
        # Else, it's a string, and thus, a single style element
        elif isinstance(value, str) or isinstance(value, int):
            stylenodes.append((name, value))
        else:
            raise "Bad error"

    if stylenodes:
        result.append(parent.strip() + " {")
        for stylenode in stylenodes:
            attribute = stylenode[0].strip(' ;:')
            if isinstance(stylenode[1], str):
                # string
                value = stylenode[1].strip(' ;:')
            else:
                # everything else (int or float, likely)
                value = str(stylenode[1]) + 'px'

            result.append(' ' * indent + "%s: %s;" % (
                    attribute, value))

        result.append("}\n")

    for subnode in subnodes:
        result += generate(parent=(parent.strip() + ' ' + subnode[0]).strip(),
                           css=subnode[1])

    return result
