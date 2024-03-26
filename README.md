# Understanding Attention Mechanisms in Machine Learning

The attention mechanism stands out as one of the most effective tools in the field of AI and deep learning, bringing us closer to human-like thinking. In the book "[Thinking, Fast and slow](https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow)" humans are shown to think using two systems: System 1 for intuition and memorization, and System 2 for reasoning and focused attention. While the attention mechanism used in current machine learning models doesn't precisely replicate the human brain's functions, it significantly boosts model performance in specific situations by emulating a key aspect of System 2 thinking. Given the importance of this research direction and the significant impact of attention mechanisms, especially in transformer-based models, this tutorial aims to provide an educational resource.


* [Implicit attention](https://github.com/bezhvin/AttentionMechanism/blob/main/ImplicitAttention.ipynb):
This tutorial delves into the concept of attention in machine learning, emphasizing the necessity for every model to "attend" to achieve optimal performance, known as implicit attention. Through interactive demonstrations using images from the MNIST dataset and fitting simple models, participants will gain insights into quantifying and explaining implicit attention mechanisms within any model.

* Self-Attention:

  * [Concept and intuition](https://github.com/bezhvin/AttentionMechanism/blob/main/self-attention%20intuition.ipynb):
The idea is to grasp the concept of self-attention intuitively. Self-attention is explained as a method to represent each observation in a sample based on others via weighted averaging. Through a simple toy example and step-by-step explanations using interactive coding, you can develop a solid understanding of self-attention.

  * [Self-attention layer](https://github.com/bezhvin/AttentionMechanism/blob/main/self-attention_layer.ipynb):
This tutorial provides a practical exploration of the self-attention layer, elucidating its learnable components and introducing multi-head attention. Leveraging the MNIST dataset once more, it is explained how to implement self-attention for image data. While the focus is on image data, the tutorial highlights the versatility of self-attention for other types of data as well.
