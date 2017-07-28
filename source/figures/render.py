#!/usr/bin/python
import os, glob
path = os.path.dirname(__file__)
lowres_export_path = os.path.join(path, 'rendered')

# the long path here is to compensate for sphinx html_extra_path behavior
hires_export_path = os.path.join(path, 'hires', 'figures', 'rendered')

for p in (hires_export_path, lowres_export_path):
    if not os.path.isdir(p):
        os.makedirs(p)

order = glob.glob(os.path.join(path, '*.svg'))
order.sort()

for svg in order:
    png = os.path.splitext(svg)[0] + '.png'
    png = os.path.join(lowres_export_path, os.path.split(png)[1]) 
    
    png_lg = os.path.splitext(svg)[0] + '_lg.png'
    png_lg = os.path.join(hires_export_path, os.path.split(png_lg)[1])
    
    if os.path.exists(png) and os.stat(png).st_mtime >= os.stat(svg).st_mtime:
        print "Skipping:", png
    else:
        print "Rendering:", png
        os.system('inkscape --export-area-drawing --export-png="%s" --export-dpi=150 --export-background=ffffffff "%s"' % (png, svg))
        os.system('inkscape --export-area-drawing --export-png="%s" --export-dpi=300 --export-background=ffffffff "%s"' % (png_lg, svg))
    
