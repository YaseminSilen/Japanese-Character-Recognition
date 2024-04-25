# Japanese Character Recognition

## Introduction
In this project, I will implement neural networks to recognize handwritten Hiragana symbols using the Kuzushiji-MNIST (KMNIST) dataset. The aim is not only to achieve high accuracy but also to understand the impact of different architectural choices on the final accuracy.

The KMNIST dataset is based on old-style script (Kuzushiji) characters. While significant changes occurred in the Japanese language over time, this dataset preserves historical characters for analysis and recognition. The dataset contains 10 Hiragana characters, each with 7000 samples per class.

The dataset paper is available [here](https://arxiv.org/pdf/1812.01718.pdf), providing detailed insights into the dataset and its historical significance.

## Model Implementations

### NetLin
- **Description**: NetLin computes a linear function of the pixels in the image, followed by log softmax activation.
- **Architecture**:
  ![NetLin Architecture](https://github.com/YaseminSilen/Japanese-Character-Recognition/assets/100459878/3e0a5955-7a92-4711-8c5f-f04a6204b7f1)
- **Parameters**: 7850 independent parameters
- **Accuracy**: 70%

### NetFull
- **Description**: NetFull is a fully connected network with two layers. It uses tanh at the hidden nodes and log softmax at the output node.
- **Architecture**:
  ![NetFull Architecture](https://github.com/YaseminSilen/Japanese-Character-Recognition/assets/100459878/62f10b07-4eb1-404f-a0bd-88c3c2f02884)
- **Hidden Nodes**: 256
- **Parameters**: 200,960 independent parameters
- **Accuracy**: 85%

### NetConv
- **Description**: NetConv is a convolutional network with two convolutional layers and one fully connected layer, all using relu activation function.
- **Architecture**:
  ![NetConv Architecture](https://github.com/YaseminSilen/Japanese-Character-Recognition/assets/100459878/f1e34974-5090-48f6-8390-a89c59302f8c)
- **Parameters**: 214,803 independent parameters
- **Accuracy**: 94%

## Comparisons

### Accuracy
- NetConv achieves the highest accuracy (94%), followed by NetFull (85%) and NetLin (70%).
- Incorporating convolutional layers significantly improves accuracy, indicating the importance of capturing spatial information.
- NetFull, with hidden layers and non-linear transformations, outperforms NetLin, highlighting the significance of adding complexity to capture complex relationships.

### Independent Parameters
- NetConv has the highest number of parameters (214,803), followed by NetFull (200,960) and NetLin (7,850).
- More parameters generally imply higher capacity to capture intricate patterns but may lead to overfitting with smaller datasets.

## Confusion Analysis

### NetLin
- Character "ma" is most likely to be mistaken for "su" (146 instances).

### NetFull
- Character "ha" is most likely to be mistaken for "su" (75 instances).

### NetConv
- Character "ha" is most likely to be mistaken for "su" (31 instances).

Certain features are common between misclassified characters, leading to confusion.

## Conclusion
- NetConv offers the highest accuracy, indicating the effectiveness of convolutional layers for image recognition tasks.
- NetFull, with hidden layers, performs better than NetLin, showcasing the importance of architectural complexity.
- Understanding confusion patterns can guide model refinement for better performance.
