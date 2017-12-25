# Word Sense Disambiguation - Winter Project 2017

## Team Members
* [Harshit Saini](https://github.com/harshits333)
* [Praphul Singh](https://github.com/spraphul)
* [Robin Singh](https://github.com/robsr)
* [Shanu Kumar](https://github.com/Sshanu)

## Introduction 

### WSD is one of the greatest problems in Natural Language Processing. It is widely used in machine translations, sequence tagging, information retrieval and many more areas. Despite of the amount of work already done in this field, the problem stills seeks for better and accurate ways of implementation.
### In this project, we have tried to explore the field under the supervision of Prof. Harish Karnick, IIT Kanpur.

## Work Done
* _We have used the Four Word dataset and One million dataset for the training._
* _We built a TensorFlow based model to predict the sense of a target word in a sentence.(Model-1)_
* _In addition to this, model-1 was modified to predict the POS-tags of each word in the sentence as well to have a better understanding of the grammmar before predicting the sense of the target word.(Model-2)_
* _To improve the accuracy of the POS-tags Linear Conditional Random Fields(CRF) classifier was used instead of Softmax Classifier.(Model-3)_
* _We propose a hierarchical model to predict the POS-tag of the target word first to reduce the classification problem to less number of senses and then predict the sense of the target word.(Model-4). Note that there is no pretraining involved separately for the POS-tag. Instead the model is trained both for POS-tag and sense in a single shot assigning more weight to the POS loss._


