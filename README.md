# [Fake News Detector](https://teamhackers-fakenewsdetector.herokuapp.com/)

This is the submission for Pravega'21, hackathon conducted by IISc bengalore.

## A Brief Overview

<p align="justify" >After the covid 19 outbreak we have seen a huge amount of information
dissemination. With the current usage of social media platforms, consumers
are creating and sharing more information than ever before, some of which
are misleading with no relevance to reality. Automated classification of a text
article as misinformation or disinformation is the target of this project. In this
presentation, we’ll describe our approach to reach the solution.</p>

## What is special in our approach?

<p align = "justify" > We see that most of the related works focus on improving
the prediction quality by adding additional features. The
fact is that these features are not always available, for
instance some article may not contain images. There is also
the fact that using social media information is problematic
because it is easy to create a new account on these media
and fool the detection system. That’s why we chose to focus
on the article body. </p>

## Brief overview of our work

### Web Development flow

<p align=justify> 
  The project has a express-node server, having a multipage application in the frontend created using ejs. The pages are styled through vanilla CSS and bootstrap. We have connected our node.js backend with the machine learning model with child process module using the command line utilities.
</p>

### Machine Learning Framework

![image](https://user-images.githubusercontent.com/74463091/127692674-66318eef-e17f-4d4e-81b7-de105e4db183.png)

#### Tokenizer

We used spaCy to segment the sentences into words, punctuation, etc. This is done according to rules specified by each language. The vocabulary is built according to the occurrence of the words in the corpus.

#### Embeddings

Glove Embeddings is used to convert the corpus into embeddings. The Glove embedding is trained on aggregated global word-word co-occurrence statistics from a corpus. The resulting representations showcase interesting linear substructures of the word vector space.

## Developer Instructions

You need to have the following things installed

* [Node 12 LTS](https://nodejs.org/en/blog/release/v12.22.4/)
* [Python 3.7 or higher](https://www.python.org/downloads/)

Once you are done with that follow the next instructions as stated

### Clone the repository

```cmd
> git clone https://github.com/sudip-mondal-2002/fake-news-detector.git
> cd fake-news-detector
```

### Install the node dependencies

```cmd
> yarn install
```

<p align="center"> OR </p>

```cmd
> npm install
```

### Install the python dependencies

```cmd
> pip install -r requirements.txt
```

### Start the server

```cmd
> yarn run start
```
<p align="center"> OR </p>

```cmd
> npm start
```

Now go to your browser and browse to (http://localhost:3000)

## Notebooks created during the project

* LSTM using Tensorflow [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ODOflRAd-huvu5X-oAv7v24jXIrngCPC?usp=sharing)
* LSTM using Pytorch [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1V-9tIgrjVIduPIrX71hbcDAjeGw6Tevq?usp=sharing)

## Bibliography

* Fakenews Dataset from [Kaggle](https://www.kaggle.com/c/fake-news)

* [GloVe Embeddings](https://nlp.stanford.edu/pubs/glove.pdf),  Stanford University (2014)

* [Recurrent Neural Networks](https://arxiv.org/pdf/1506.00019.pdf), Lipton et al. (2015)

* [Long Short-Term Memory](https://arxiv.org/pdf/1503.04069.pdf), Greff et al. (2015)

## Team Hackers

* [Archish S](https://github.com/Xerefic)
* [Kartik Ruikar](https://github.com/Kartik2605)
* [Sudip Mondal](https://github.com/sudip-mondal-2002)
