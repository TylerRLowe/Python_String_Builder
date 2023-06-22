# Python_String_Builder
A string builder that can be imported and used with no dependencies. Based on the C and Java counterparts, providing Amortized 0(1) appending and removing from the end. As the average length of strings added increases, the efficiency of string builder surpasses using .join. When the average happened string length exceeds 8 characters, it outperforms .join by about 10%. string builder append is constant time no matter how long the input, while .join increases linearly.

<b>Use case</b>

I was translating an airline system that functions by constantly changing a current string of the path from Java to pytohn, and ran into the issue of decreasing performance of Python's built-in methods, and could not find a suitable replacement

![image](https://github.com/TylerRLowe/Python_String_Builder/assets/99204234/ffd45d4b-92e3-4470-8306-3f51199b6101)
