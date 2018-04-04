# image-object-removal

**Note:** Use PNG or other lossless image formats, otherwise pixel matrix will be corrupted

Main library: Pillow (python image library), PIL is deprecated

~~## stage 1 (square overlayed onto solid color background)
1. bounds for square
2. iteratively calculate expected Red from surrounding pixels~~

~~## stage 2 (square on gradient background)
1.
2.
3. average with calculated rgb from other side~~

To circumvent the issue of RGB int colors, and needing floating pt precision, the image was first loaded into a floating point numpy array where calculations where done. Then, this array was converted to an array of ints, which was then loaded back into a PIL image.

While an error rate check has not been completed, from first glance, the calculated image is indistinguishable from the original. Thus, any image could be put in the bounded square that was "removed," and it could be removed as if it were never there.



## stage 3 (square on "floor" image background)
1.
2.
3.

## stage 4 (square on "flower pattern" image background)
1
2.
3.
