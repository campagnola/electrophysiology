#!/usr/bin/python
import os, glob
order = glob.glob('*.svg')
order.remove('patch_examples.svg')
order.sort()

images = []
for svg in order:
    png = os.path.splitext(svg)[0] + '.png'
    images.append(png)
    if os.path.exists(png) and os.stat(png).st_mtime >= os.stat(svg).st_mtime:
        print "Skipping:", png
    else:
        print "Rendering:", png
        os.system('inkscape --export-area-drawing --export-png="%s" --export-dpi=90 --export-background=ffffffff "%s"' % (png, svg))
    
