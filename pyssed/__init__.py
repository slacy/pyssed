#!/usr/bin/python
import copy


class style(object):
    """A list of CSS styles, but stored as a dict.
    Can contain nested styles."""

    def __init__(self, *args, **kwargs):
        self._styles = {}
        for a in args:
            self.append(a)

        for name, value in kwargs.iteritems():
            self._styles[name] = value

    def iteritems(self):
        """Return iterable contents."""
        return self._styles.iteritems()

    def append(self, other):
        """Append syle 'other' to self."""
        self._styles = self.__add__(other)._styles

    def __add__(self, other):
        """Add self and other, and return a new style instance."""
        summed = copy.deepcopy(self)
        if isinstance(other, str):
            single = other.split(':')
            summed._styles[single[0]] = single[1]
        elif isinstance(other, dict):
            summed._styles.update(other)
        elif isinstance(other, style):
            summed._styles.update(other._styles)
        else:
            raise 'Bad type for style'
        return summed

    def __repr__(self):
        return str(self._styles)


def generate(css, parent='', indent=4):
    """Given a dict mapping CSS selectors to a dict of styles, generate a
    list of lines of CSS output."""
    subnodes = []
    stylenodes = []
    result = []

    for name, value in css.iteritems():
        # If the sub node is a sub-style...
        if isinstance(value, dict) or isinstance(value, style):
            subnodes.append((name, value))
        # Else, it's a string, and thus, a single style element
        elif (isinstance(value, str)
              or isinstance(value, int)
              or isinstance(value, float)):
            stylenodes.append((name, value))
        else:
            raise 'Bad error'

    if stylenodes:
        result.append(parent.strip() + ' {')
        for stylenode in stylenodes:
            attribute = stylenode[0].strip(' ;:')
            if isinstance(stylenode[1], str):
                # string
                value = stylenode[1].strip(' ;:')
            else:
                # everything else (int or float, likely)
                value = str(stylenode[1]) + 'px'

            result.append(' ' * indent + '%s: %s;' % (
                    attribute, value))

        result.append('}')
        result.append('') # a newline

    for subnode in subnodes:
        result += generate(subnode[1],
                           parent=(parent.strip() + ' ' + subnode[0]).strip())

    return result
