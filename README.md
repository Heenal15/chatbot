# Implementation of a FAQ Chatbot in PyTorch.  
Simple chatbot implementation with PyTorch.

# Source code credit
Online tutorial link: https://www.youtube.com/watch?v=RpWeNzfSUHw
Link to tutorial GitHub repository: https://github.com/patrickloeber/pytorch-chatbot
User Interface Tutorial Link: https://studygyaan.com/python/create-web-based-chatbot-in-python-django-flask
Link to GitHub repository: https://github.com/huzaifsayed/coronabot-chatterbot

# Inspired by
The approach is inspired by this article and ported to PyTorch: [https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077](https://chatbotsmagazine.com/contextual-chat-bots-with-tensorflow-4391749d0077).

## Tutorial link
[![Alt text](https://img.youtube.com/vi/RpWeNzfSUHw/hqdefault.jpg)](https://www.youtube.com/watch?v=RpWeNzfSUHw&list=PLqnslRFeH2UrFW4AUgn-eY37qOAWQpJyg)

## Deployed Version

The deployed version can be accessed at https://gpfaqchatbot.pythonanywhere.com/

## Installation
Installation instructions to build the chatbot in your local development environment from the
source code:

### Create an environment
To build the chatbot and use it in your local development environment, you must first set up
and activate a local development environment. From the root of the project:
```console
$ virtualenv venv
$ source venv/bin/activate
```

### Install all required packages
```console
$ pip3 install -r requirements.txt
$ pip install numpy
$ pip3 install Flask
$ pip3 install -f torch torchvision
$ pip install nltk
```
### Errors
If you get an error during the first run, you also need to install `nltk.tokenize.punkt`:
Run this once in your terminal:
 ```console
$ python
>>> import nltk
>>> nltk.download('punkt')
```

## Usage
Run
```console
python train.py
```
This will dump `data.pth` file. And then run
```console
python app.py
```
Open your browser and type in the URL
http://localhost:8080

## Chatbot Preview

![UI1](https://user-images.githubusercontent.com/78482808/230316772-3875c5af-2592-4b7e-8e8b-610e54aca0d2.png)

## Additions
Have a look at [intents.json](intents.json). You can add to it according to your own use case. Just define a new `tag`, possible `patterns`, and possible `responses` for the chat bot. You have to re-run the training whenever this file is modified.
```console
{
  "intents": [
    {
      "tag": "greeting",
      "patterns": [
        "Hi",
        "Hey",
        "How are you",
        "Is anyone there?",
        "Hello",
        "Good day"
      ],
      "responses": [
        "Hey :-)",
        "Hello, thanks for visiting",
        "Hi there, what can I do for you?",
        "Hi there, how can I help?"
      ]
    },
    ...
  ]
}
```
