#!/usr/bin/env python3
"""
This script processes SVG icon files by:
1. Reading each .svg file from input directory
2. Calculating the intrinsic height and width of all drawable content (which 
   may or may not be square)
3. Scaling content to fit 95% of a 512x512 canvas (maintains aspect ratio)
4. Centering the scaled content inside the canvas
5. Saving processed icons to output directory

Key features:
- Preserves vector quality (no rasterization)
- Maintains original aspect ratios
- Handles SVGs with metadata
"""

import os
from svgelements import SVG, Matrix

input_dir = "./icons"
output_dir = "./processed_icons"
size = 512
margin = 0.95

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for filename in os.listdir(input_dir):
    if filename.endswith(".svg"):
        try:
            path = os.path.join(input_dir, filename)
            svg = SVG.parse(path)
            
            # TODO
            
            print(f"Processed: {filename}")
        except Exception as e:
            print(f"Failed {filename}: {e}")
