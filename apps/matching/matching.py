import Algorithmia
# from .models import User
import re
from random import random
import json 

# group1=[]
# group2=[]
# users = User.objects.all()
# for user in users:
#   if randint(1,2) == 1:
#     objects= {'name':user.username,'interests':re.split('; | , | \* | \n',user.hobbies)}
#     group1.append(user)
#   if randint(1,2) == 2:
#     group2.append(user)


data = {
  "scoring_weights": {
      "interests": 1.5,
      # "values": 7.5,
      "age": 0.65,
      "coordinates": 0.015
  },
  "group1": [
    {
          "name": "Beowulf the Conquerer",
          "interests": [
        "reading",
        "running",
        "chilling",
        "coding",
        "seattle",
        "coffee",
        "tea",
        "bilingual",
        "food",
        "arrested development",
        "the office",
        "parc and rec",
        "rick and morty"
      ],
      #     "values": [
      #   "humanism"
      # ],
          "age": "22",
          "coordinates": {
              "lat": 47.599088077746394,
              "long": -122.3339125374332
      }
    }
  ],
  "group2": [
    {
          "name": "Julia the Jukebox",
          "interests": [
        "music",
        "rock",
        "coffee",
        "guitar hero"
      ],
          "values": [
        "individuality"
      ],
          "age": "22",
          "coordinates": {
              "lat": 47.62446091996251,
              "long": -122.32016064226627
      }
    },
    {
          "name": "Chelsea the Bookworm",
          "interests": [
        "reading",
        "writing",
        "classics",
        "coffee",
        "walking"
      ],
          "values": [
        "family",
        "love"
      ],
          "age": "26",
          "coordinates": {
              "lat": 47.62446091996251,
              "long": -122.32016064226627
      }
    },
    {
          "name": "Ana the Artist",
          "interests": [
        "drawing",
        "art",
        "music",
        "classical music",
        "tea",
        "running"
      ],
          "values": [
        "post-modernism",
        "beauty"
      ],
          "age": "32",
          "coordinates": {
              "lat": 47.62446091996251,
              "long": -122.32016064226627
      }
    },
    {
          "name": "Laea the Space Pirate",
          "interests": [
        "coffee",
        "pirating",
        "traveling",
        "netflix"
      ],
          "values": [
        "vegetarianism",
        "individuality"
      ],
          "age": "39",
          "coordinates": {
              "lat": 47.62446091996251,
              "long": -122.32016064226627
      }
    },
    {
          "name": "Jules the Hipster",
          "interests": [
        "Scruffy Beards",
        "coffee",
        "tumblr",
        "postmodern art"
      ],
          "values": [
        "individuality",
        "relationships"
      ],
          "age": "21",
          "coordinates": {
              "lat": 47.62446091996251,
              "long": -122.32016064226627
      }
    },
    {
          "name": "Hale the Chef",
          "interests": [
        "food",
        "cooking",
        "tea",
        "microbrewery",
        "turkish cuisine"
      ],
          "values": [
        "family",
        "love"
      ],
          "age": "29",
          "coordinates": {
              "lat": 47.62446091996251,
              "long": -122.32016064226627
      }
    },
    {
          "name": "Natalie the Lawyer",
          "interests": [
        "law",
        "bird law",
        "coffee",
        "running"
      ],
          "values": [
        "love",
        "individuality"
      ],
          "age": "33",
          "coordinates": {
              "lat": 47.62446091996251,
              "long": -122.32016064226627
      }
    },
    {
          "name": "Kate the Teacher",
          "interests": [
        "education",
        "kids",
        "iced tea",
        "apple pie",
        "science"
      ],
          "values": [
        "individuality",
        "scepticism"
      ],
          "age": "32",
          "coordinates": {
              "lat": 47.62446091996251,
              "long": -122.32016064226627
      }
    },
    {
          "name": "Maria the Engineer",
          "interests": [
        "science",
        "tech",
        "engineering",
        "hackathons",
        "coffee",
        "running"
      ],
          "values": [
        "individuality",
        "free speech",
        "activism"
      ],
          "age": "22",
          "coordinates": {
              "lat": 47.62446091996251,
              "long": -122.32016064226627
      }
    },
    {
          "name": "Hannah the Model",
          "interests": [
        "fashion",
        "paris",
        "france",
        "tea",
        "traveling"
      ],
          "values": [
        "love",
        "art"
      ],
          "age": "24",
          "coordinates": {
              "lat": 47.62446091996251,
              "long": -122.32016064226627
      }
    }
  ]
}

client = Algorithmia.client('simWgOx7ABiLTOAxABjYTbiRrma1')
algo = client.algo('matching/DatingAlgorithm/0.1.3')
algo.set_options(timeout=300) # optional
print(algo.pipe(data).result['Beowulf the Conquerer'])
