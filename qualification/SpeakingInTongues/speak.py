#!/usr/bin/python

def decode(line):
    """ Using a translation matrix, decode a line of text and return the
    decoded line.

    Translation matrix taken from sample input
    Crappy way of doing this... YES!
    Effective... YES!
    """

    translation_matrix = {
        'a': 'y',
        'b': 'h',
        'c': 'e',
        'd': 's',
        'e': 'o',
        'f': 'c',
        'g': 'v',
        'h': 'x',
        'i': 'd',
        'j': 'u',
        'k': 'i',
        'l': 'g',
        'm': 'l',
        'n': 'b',
        'o': 'k',
        'p': 'r',
        'q': 'z',
        'r': 't',
        's': 'n',
        't': 'w', 
        'u': 'j',
        'v': 'p',
        'w': 'f',
        'x': 'm',
        'y': 'a',
        'z': 'q'
    }

    decoded_line = ''
    for c in line:
        if c in translation_matrix:
            decoded_line += translation_matrix[c]
        else:
            decoded_line += c

    return decoded_line

if __name__ == "__main__":
    import sys
    f = sys.stdin
    T = int(f.readline())
    for i in xrange(T):
        line = f.readline().strip()
        decoded_string = decode(line)
        print "Case #%s: %s" % (i+1, decoded_string)