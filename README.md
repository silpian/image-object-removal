# image-object-removal

**Note:** Use PNG or other lossless image formats, otherwise pixel matrix will be corrupted

Main library: Pillow (python image library), PIL is deprecated

repeatedly calculate n derivatives of rgb of pixels
like with maclaurin series and prioritized by distance to current pixel

calculate error rate, against actual background

Precise derivative requires floating point colors, RGB of Pillow is series of ints.

Matplotlib colormap allows floating pt values, but then you need to find a suitable way to view the image

## stage 1 (square overlayed onto solid color background)
1. bounds for square
2. iteratively calculate expected Red from surrounding pixels

## stage 2 (square on gradient background)
1.
2.
3. average with calculated rgb from other side

At any pt, the derivative is constant, at 255/width

## stage 3 (square on "floor" image background)
1.
2.
3.

## stage 4 (square on "flower pattern" image background)
1
2.
3.
