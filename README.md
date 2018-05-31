# Word Sense Disambiguation 

Word sense disambiguation (WSD) is the ability to identify the meaning of words in context. We address this problem using series of end-to-end neural architectures using bidirectional Long Short Term Memory (LSTM). We propose two variants for WSD: an end-to-end word specific neural model and all-words neural model. In the word specific models we have to train models for every disambiguation target word. We addressed this issue using the all-words model which rely on sequence learning. We also used POS tags to improve the performance. We tried different variants of attention mechanisms for the all-words model. Performance was boosted by using convolutional neural networks (CNN) which captures local features around the words that is normally what humans do for predicting the senses. We further improved the performance using hierarchical models. We used POS tags as hierarchy and used two variants as soft masking and hard masking.

## MODELS

* [Word Specific Model trained on One Million Dataset](https://github.com/Sshanu/Word-Sense-Disambiguation/tree/master/Four%20Word%20Model)
* [Word Specific Model trained on One Million Dataset](https://github.com/Sshanu/Word-Sense-Disambiguation/tree/master/one_million)
* [All-words Model](https://github.com/Sshanu/Word-Sense-Disambiguation/tree/master/one_million/all-word)
