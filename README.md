# Japanese-Character-Recognition
I will be implementing networks to recognize handwritten Hiragana symbols. The dataset to be used is Kuzushiji-MNIST or KMNIST for short. The paper describing the dataset is available [here](https://arxiv.org/pdf/1812.01718.pdf). It is worth reading, but in short: significant changes occurred to the language when Japan reformed their education system in 1868, and the majority of Japanese today cannot read texts published over 150 years ago. This paper presents a dataset of handwritten, labeled examples of this old-style script (Kuzushiji). Along with this dataset, however, they also provide a much simpler one, containing 10 Hiragana characters with 7000 samples per class. This is the dataset I will be using.

Implement a model NetLin which computes a linear function of the pixels in the image, followed by log softmax.

![netlin](https://github.com/YaseminSilen/Japanese-Character-Recognition/assets/100459878/3e0a5955-7a92-4711-8c5f-f04a6204b7f1)



Implement a fully connected 2-layer network NetFull, using tanh at the hidden nodes and log softmax at the output node.
![netfull](https://github.com/YaseminSilen/Japanese-Character-Recognition/assets/100459878/62f10b07-4eb1-404f-a0bd-88c3c2f02884)


Implement a convolutional network called NetConv, with two convolutional layers plus one fully connected layer, all using relu activation function.![conv](https://github.com/YaseminSilen/Japanese-Character-Recognition/assets/100459878/f1e34974-5090-48f6-8390-a89c59302f8c)
