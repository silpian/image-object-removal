# image-object-removal

**Note:** Use PNG or other lossless image formats, otherwise pixel matrix will be corrupted

Main library: Pillow (python image library), PIL is deprecated

repeatedly calculate n derivatives of rgb of pixels
like with maclaurin series and prioritized by distance to current pixel

calculate error rate, against actual background


## stage 1 (square overlayed onto solid color background)
1. bounds for square
2. iteratively calculate expected rgb from surrounding pixels

## stage 2 (square on gradient background)
1.
2.
3. average with calculated rgb from other side

## stage 3 (square on "floor" image background)
1.
2.
3.

##stage 4 (square on "flower pattern" image background)
1
2.
3.
