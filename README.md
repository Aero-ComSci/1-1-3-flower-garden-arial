[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/CH30njZ-)
# 1.1.3FlowerGarden

Our code takes in a prompt from the reader.

We see how many flowers we need to print and which flower. If the flower is one of the 5 we draw we will the draw the flower(s).

To find the key words we use the process of tokenization by splitting the input by spaces and then from there we look for one of the flower names in the list, then from there we find the number closest to that flower by taking the index of the flower - 1 this allows us to bypass most errors with tokenization but still misses some wonky cases that the user may decide to throw upon us. 

The max flowers we allowed the user to print is 30
