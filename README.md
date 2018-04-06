# image-object-removal

**Note:** Use PNG or other lossless image formats, otherwise pixel matrix will be corrupted

Main library: Pillow (python image library), PIL is deprecated

~~## stage 1 (square overlayed onto solid color background)~~
~~1. bounds for square~~
~~2. iteratively calculate expected Red from surrounding pixels~~

~~## stage 2 (square on gradient background)~~
~~1. same as stage 1~~
~~2. same as stage 2~~
~~3. average with calculated rgb from other side~~

To circumvent the issue of RGB int colors, and needing floating pt precision, the image was first loaded into a floating point numpy array where calculations where done. Then, this array was converted to an array of ints, which was then loaded back into a PIL image.

While an error rate check has not been completed, from first glance, the calculated image is indistinguishable from the original. Thus, any image could be put in the bounded square that was "removed," and it could be removed as if it were never there.

## stage 3 (square on "floor" image background)
1. raw image

![alt text](https://raw.githubusercontent.com/silpian/image-object-removal/master/image_01.png)

2. determine bounds for removing object (my water bottle)

![alt text](https://raw.githubusercontent.com/silpian/image-object-removal/master/image_01_hole.png)

3. calculate appropriate background

![alt text](https://raw.githubusercontent.com/silpian/image-object-removal/master/image_01_hole_removed.png)

As you can see, unfortunately simple images are not easy to "fill in." I had to tweak the algorithm with a random element to add the fuzziness that is needed for it to blend in. Additionally, I also need to blur the edges into the image.

Another example with kitchen floor and my retainer box

Raw from camera | Bounds marked | Background calculated

<img src="https://raw.githubusercontent.com/silpian/image-object-removal/master/data/img/raw/floor_4.png" width="250" height = "250"/> <img src="https://raw.githubusercontent.com/silpian/image-object-removal/master/data/img/intermediate/floor_4_hole.png" width="250" height = "250"/> <img src="https://raw.githubusercontent.com/silpian/image-object-removal/master/data/img/calculated/floor_4_hole_removed_one_side.png" width="250" height = "250"/>

## stage 4 (square on "flower pattern" image background)
1
2.
3.

## stage 5 (with background and foreground (3D))
