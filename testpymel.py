import pymel.core as pmc
import inspect

xform, shape = pmc.polySphere()

def info(obj):
    '''Prints information anout the object.'''
    lines = ['Info for %s' % obj.name(),
                            'Attributes:']
    for a in obj.listAttr():
        lines.append(' ' + a.name())
    result = '\n'.join(lines)
    print (result)
