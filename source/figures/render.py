#!/usr/bin/python
import os, glob
path = os.path.dirname(__file__)
export_path = os.path.join(path, 'rendered')
if not os.path.isdir(export_path):
    os.mkdir(export_path)

order = glob.glob(os.path.join(path, '*.svg'))
order.sort()

images = []
for svg in order:
    png = os.path.splitext(svg)[0] + '.png'
    png = os.path.join(export_path, os.path.split(png)[1]) 
    png_lg = os.path.splitext(svg)[0] + '_lg.png'
    png_lg = os.path.join(export_path, os.path.split(png_lg)[1]) 
    images.append(png)
    if os.path.exists(png) and os.stat(png).st_mtime >= os.stat(svg).st_mtime:
        print "Skipping:", png
    else:
        print "Rendering:", png
        os.system('inkscape --export-area-drawing --export-png="%s" --export-dpi=150 --export-background=ffffffff "%s"' % (png, svg))
        os.system('inkscape --export-area-drawing --export-png="%s" --export-dpi=300 --export-background=ffffffff "%s"' % (png_lg, svg))
    
