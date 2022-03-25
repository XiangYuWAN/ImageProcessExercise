IMAGE SEGMENTATION
The goal is to partition an image into its relevant regions.
A large number of methods.
The watershed is the fundamental method in morphological segmentation.
A gradient−based approach.
* Pure watershed approach
−−−−−−−−−−−−−−−−−−−−−−−−−
The gradient is partitioned into its catchment basins (regions).
 This can be computed very efficiently
 Waiting queues algorithms
 See, for example:
 L. Vincent, P. Soille. "Watersheds in Digital Spaces:
 An Efficient Algorithm Based on Immersion Simulations",
 IEEE Trans. Pattern Anal. Mach. Intell., 1991.
 DOI:10.1109/34.87344
A catchment basin (region) arises for each minimum of the gradient.
A problem is that, normally, an image gradient has an extremely
large number of minima.
 This produces an over−segmentation problem.
 A large number of non−relevant regions is obtained.
A solution to this over−segmentation problem is achieved by adding
markers.
* Watershed + markers approach
−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
Markers of relevant regions can be incorporated to modify the
gradient of the image, so that all minima that are not marked
are removed (or rather, 'filled').
Those markers can be computed by several techniques (v.g.,
by using contrast operators such as the 'top−hat', etc.), or
can be provided manually.
After modifying the gradient, a watershed algorithm can be
applied to compute its catchment regions.
Each marker will produce a catchment basin (region).
图像分段目标是将图像分区为其相关区域。
大量方法。
流域是形态细分中的基本方法。
基于梯度的方法。
*纯粹的流域方法-------------------------梯度被分割为其集水区盆地（地区）。
这可以非常有效地等待等待队列算法，例如：L. Vincent，P. Soille。  “数字空间中的流域：基于浸没模拟的高效算法”，
IEEE Trans。 模式肛门。 马赫。 智能。，1991年。
DOI：10.1109 / 34.87344集水盆（区域）为每个梯度的每个最小值产生。
问题是，通常，图像梯度具有极大数量的最小值。
这产生了过分分割问题。
获得了大量的非相关区域。
通过添加标记来实现对该过分分割问题的解决方案。
*流域+标记方法-----------------------------------------
中文可以纳入相关区域的梯度， 因此，未标记的所有最小值都被删除（或者相反，'填充'）。
这些标记可以通过若干技术（V.G.，通过使用诸如“顶帽”等）的对比度运算符来计算，或者可以手动提供。
在修改梯度之后，可以应用流域算法来计算其集水区区域。
每个标记将产生集水区盆地（区域）。
##################################################################









exercise: 实现以下功能以将图像ImageInmarkers施加到梯度图像Imagein in。 
输出将是修改后的渐变映像输出，其最小值是ImageInMarkers的标记。

imMinimaImpose (imageIn, imageInMarkers, connectivity, imageOut)
/* imageIn: input image (in principle, a gradient image) whose minima
must be modified; 
imageInMarkers: binary input image with markers
(markers have an intensity value of 255, and the rest of the image
has a 0 intensity value).

The output image imageOut is a modification
of imageIn that has as minima the markers at imageInMarkers.
输出图像ImageOut是对Imagein的修改，其具有ImageInMarkers的标记。
 */


为此，应使用以下简单的简单最小拼版算法。 这是一种简单而直接的算法，但不是非常有效：
/ **** /
- 让M成为标记图像。  M的标记将是“施加”的梯度最小值。 让我成为原始渐变。
- 计算minv，即标记图像反转（在Minv标记中具有0值，图像的其余部分具有255个值）。
- 计算我'= i inf minv。
-  minv_0是minv / * init * /  -  i = 0 / * init * /  -  do / *循环* / minv_i + 1 = erosion_1（minv_i）sup i'i = i + 1直到minv_i的幂等（即，minv_i 没变）

Erosion_1是尺寸1的基本侵蚀（具有8-Connectivity的尺寸3x3的结构化元件）。
minv_final是所需的结果。 它的最小值是M的标记。
这可以通过检查Minv的最小值来检查。
（注意：此操作是一个测地重建。）该算法简单但慢。  （存在更有效的算法。）/ **** /