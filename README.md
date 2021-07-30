# Fake News Detector
This is the submission for Pravega'21, hackathon conducted by IISc bengalore.

## A Brief Overview
<p align="justify" >After the covid 19 outbreak we have seen a huge amount of information
dissemination. With the current usage of social media platforms, consumers
are creating and sharing more information than ever before, some of which
are misleading with no relevance to reality. Automated classification of a text
article as misinformation or disinformation is the target of this project. In this
presentation, we’ll describe our approach to reach the solution.</p>

## Why us?
<p align = "justify" > We see that most of the related works focus on improving
the prediction quality by adding additional features. The
fact is that these features are not always available, for
instance some article may not contain images. There is also
the fact that using social media information is problematic
because it is easy to create a new account on these media
and fool the detection system. That’s why we chose to focus
on the article body. </p>

## Developer Instructions

You need to have the following things installed
* Node 12 LTS
* Python 3.7 or higher

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

Now go to your browser and browse to http://localhost:3000
## Notebooks created during the project
* [LSTM using Tensorflow](https://colab.research.google.com/drive/1ODOflRAd-huvu5X-oAv7v24jXIrngCPC?usp=sharing)
* [LSTM using Pytorch](https://colab.research.google.com/drive/1V-9tIgrjVIduPIrX71hbcDAjeGw6Tevq?authuser=1)


## Team Hackers
* [Archish S](https://github.com/Xerefic)
* [Kartik Ruikar](https://github.com/Kartik2605)
* [Sudip Mondal](https://github.com/sudip-mondal-2002)
