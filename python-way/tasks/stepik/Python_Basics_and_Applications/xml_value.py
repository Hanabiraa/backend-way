"""
task link -> https://stepik.org/lesson/24474/step/4?unit=6779
"""
import xml.etree.ElementTree as ET

colors = dict(
    red=0,
    green=0,
    blue=0,
)


def get_children(root, level):
    # print(root.attrib)
    colors[root.attrib['color']] += level
    for child in root.getchildren():
        get_children(child, level+1)


raw = '<cube color="blue"><cube color="red"><cube color="green"></cube></cube><cube color="red"></cube></cube>'

parser = ET.fromstring(raw)

get_children(parser, 1)

print('{} {} {}'.format(colors['red'], colors['green'], colors['blue']))
