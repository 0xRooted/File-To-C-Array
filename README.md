# File-To-C-Array
Get files data in a unsigned char array. Similar to HxD export to c code.

Example:
![image](https://user-images.githubusercontent.com/102437829/197292016-4d47e29c-15cd-4dd2-b5a6-6d339d3bef9e.png)

test.py:
<hr>
<b>
import filetocarray

obj = filetocarray.image_to_c_array("ring0.jpg", "test.h", 12, "ring0_image", True, "TEST", True)
obj.save()
</b>
