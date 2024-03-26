# Self-attention mechanism
The attention mechanism stands out as one of the most effective tools in the field of AI and deep learning, bringing us closer to human-like thinking. In the book "[Thinking, Fast and slow](https://en.wikipedia.org/wiki/Thinking,_Fast_and_Slow)" humans are shown to think using two systems: System 1 for intuition and memorization, and System 2 for reasoning and focused attention. While the attention mechanism used in current machine learning models doesn't precisely replicate the human brain's functions, it significantly boosts model performance in specific situations by emulating a key aspect of System 2 thinking. Given the importance of this research direction and the significant impact of attention mechanisms, especially in transformer-based models, this tutorial aims to provide an educational resource.

Here is the content of this tutorial:


* [Implicit attention](https://github.com/bezhvin/AttentionMechanism/blob/main/ImplicitAttention.ipynb): This notebook is a tutorial to underestand the concept of attention in machine learning and how actually every machine learning model needs to "attend" to gain reasonable performance, which is also called implicit attention. It is an interactive tutorial with images from MNIST dataset and fitting simple models trying to quantify and explain implicit attention mechanism in any model.

* Self-attention:
   * [Concept and intuition](https://github.com/bezhvin/AttentionMechanism/blob/main/self-attention%20intuition.ipynb): This tutorial provides a starting point to intuitively underestand self-attention as a way to represent each observarion in a sample based on the other observations via weighted averaging. A simple toy example is provided and the procedure is described step by step via simple itractive coding to get the concept of self attention.
   * [Self-attention layer](https://github.com/bezhvin/AttentionMechanism/blob/main/self-attention_layer.ipynb): In this tutorial the self-attention layer in a more practical way is explained by defining the learnable components and explaining multi-head attention. MNIST data set is used again as usecase example of how to use self-attention for image data while the concept is straight forward for other data too.


