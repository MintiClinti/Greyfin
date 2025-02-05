import spacy
import srsly
from spacy.training import docs_to_json, offsets_to_biluo_tags, biluo_tags_to_spans

TRAIN_DATA = [
    ("I enjoy playing guitar.", {"entities": [(9, 15, "HOBBY")]}),
    ("Cooking is my passion.", {"entities": [(0, 7, "HOBBY")]}),
    ("I love hiking in the mountains.", {"entities": [(7, 13, "HOBBY")]}),
    ("Gardening helps me relax.", {"entities": [(0, 9, "HOBBY")]}),
    ("Photography is an art form.", {"entities": [(0, 12, "HOBBY")]}),
    ("Knitting is my favorite hobby.", {"entities": [(0, 8, "HOBBY")]}),
    ("Reading books is my hobby.", {"entities": [(0, 7, "HOBBY")]}),
    ("Watching movies is fun.", {"entities": [(0, 16, "HOBBY")]}),
    ("Playing chess is challenging.", {"entities": [(0, 13, "HOBBY")]}),
    ("I enjoy scuba diving.", {"entities": [(9, 20, "HOBBY")]}),
    ("I am interested in coding.", {"entities": [(16, 21, "INTEREST")]}),
    ("Astronomy fascinates me.", {"entities": [(0, 9, "INTEREST")]}),
    ("Fashion design is my passion.", {"entities": [(0, 13, "INTEREST")]}),
    ("I love learning languages.", {"entities": [(7, 23, "INTEREST")]}),
    ("Singing brings me joy.", {"entities": [(0, 7, "INTEREST")]}),
    ("Yoga helps me stay relaxed.", {"entities": [(0, 4, "INTEREST")]}),
    ("Bird watching is fascinating.", {"entities": [(0, 11, "INTEREST")]}),
    ("I am interested in meditation.", {"entities": [(16, 26, "INTEREST")]}),
    ("Playing chess is challenging.", {"entities": [(0, 13, "HOBBY")]}),
    ("I enjoy playing guitar.", {"entities": [(9, 15, "HOBBY")]}),
    ("Cooking is my passion.", {"entities": [(0, 7, "HOBBY")]}),
    ("I love hiking in the mountains.", {"entities": [(7, 13, "HOBBY")]}),
    ("Gardening helps me relax.", {"entities": [(0, 9, "HOBBY")]}),
    ("Photography is an art form.", {"entities": [(0, 12, "HOBBY")]}),
    ("Knitting is my favorite hobby.", {"entities": [(0, 8, "HOBBY")]}),
    ("Reading books is my hobby.", {"entities": [(0, 7, "HOBBY")]}),
    ("Watching movies is fun.", {"entities": [(0, 16, "HOBBY")]}),
    ("Playing chess is challenging.", {"entities": [(0, 13, "HOBBY")]}),
    ("I enjoy scuba diving.", {"entities": [(9, 20, "HOBBY")]}),
    ("I am interested in coding.", {"entities": [(16, 21, "INTEREST")]}),
    ("Astronomy fascinates me.", {"entities": [(0, 9, "INTEREST")]}),
    ("Fashion design is my passion.", {"entities": [(0, 13, "INTEREST")]}),
    ("I love learning languages.", {"entities": [(7, 23, "INTEREST")]}),
    ("Singing brings me joy.", {"entities": [(0, 7, "INTEREST")]}),
    ("Yoga helps me stay relaxed.", {"entities": [(0, 4, "INTEREST")]}),
    ("Bird watching is fascinating.", {"entities": [(0, 11, "INTEREST")]}),
    ("I am interested in meditation.", {"entities": [(16, 26, "INTEREST")]}),
    ("Playing chess is challenging.", {"entities": [(0, 13, "HOBBY")]}),
    ("I enjoy playing guitar.", {"entities": [(9, 15, "HOBBY")]}),
    ("Cooking is my passion.", {"entities": [(0, 7, "HOBBY")]}),
    ("I love hiking in the mountains.", {"entities": [(7, 13, "HOBBY")]}),
    ("Gardening helps me relax.", {"entities": [(0, 9, "HOBBY")]}),
    ("Photography is an art form.", {"entities": [(0, 12, "HOBBY")]}),
    ("Knitting is my favorite hobby.", {"entities": [(0, 8, "HOBBY")]}),
    ("Reading books is my hobby.", {"entities": [(0, 7, "HOBBY")]}),
    ("Watching movies is fun.", {"entities": [(0, 16, "HOBBY")]}),
    ("Playing chess is challenging.", {"entities": [(0, 13, "HOBBY")]}),
    ("I enjoy scuba diving.", {"entities": [(9, 20, "HOBBY")]}),
    ("I am interested in coding.", {"entities": [(16, 21, "INTEREST")]}),
    ("Astronomy fascinates me.", {"entities": [(0, 9, "INTEREST")]}),
    ("Fashion design is my passion.", {"entities": [(0, 13, "INTEREST")]}),
    ("I love learning languages.", {"entities": [(7, 23, "INTEREST")]}),
    ("Singing brings me joy.", {"entities": [(0, 7, "INTEREST")]}),
    ("Yoga helps me stay relaxed.", {"entities": [(0, 4, "INTEREST")]}),
    ("Bird watching is fascinating.", {"entities": [(0, 11, "INTEREST")]}),
    ("I am interested in meditation.", {"entities": [(16, 26, "INTEREST")]}),
    ("I spend my weekends hiking in the mountains.", {"entities": [(19, 25, "HOBBY")]}),
    ("I am passionate about playing the piano and painting landscapes.", {"entities": [(27, 39, "HOBBY"), (44, 57, "HOBBY")]}),
    ("My hobbies include gardening, cooking, and bird watching.", {"entities": [(14, 23, "HOBBY"), (25, 32, "HOBBY"), (38, 50, "HOBBY")]}),
    ("I love to travel and explore new cultures.", {"entities": [(7, 13, "HOBBY")]}),
    ("I spend my free time reading classic literature and practicing archery.", {"entities": [(27, 44, "HOBBY"), (50, 59, "HOBBY")]}),
    ("My interests range from scuba diving and astronomy to fashion design.", {"entities": [(21, 33, "HOBBY"), (38, 47, "HOBBY"), (52, 65, "HOBBY")]}),
    ("I enjoy coding and bird watching as my hobbies.", {"entities": [(9, 14, "HOBBY"), (19, 31, "HOBBY")]}),
    ("My favorite pastime is knitting and watching movies with my friends.", {"entities": [(21, 28, "HOBBY"), (33, 48, "HOBBY")]}),
    ("I have a passion for photography and yoga.", {"entities": [(18, 29, "HOBBY"), (34, 38, "HOBBY")]}),
    ("I like to spend my weekends hiking, reading books, and cooking.", {"entities": [(27, 33, "HOBBY"), (35, 47, "HOBBY"), (53, 60, "HOBBY")]}),
    ("Traveling and playing the guitar are my favorite hobbies.", {"entities": [(0, 9, "HOBBY"), (15, 28, "HOBBY")]}),
    ("I am interested in scuba diving, learning languages, and painting.", {"entities": [(19, 31, "HOBBY"), (33, 49, "HOBBY"), (54, 62, "HOBBY")]}),
    ("My hobbies are hiking, gardening, and playing chess.", {"entities": [(11, 17, "HOBBY"), (19, 28, "HOBBY"), (33, 46, "HOBBY")]}),
    ("I like to knit and watch movies in my free time.", {"entities": [(9, 13, "HOBBY"), (18, 32, "HOBBY")]}),
    ("I enjoy singing and meditation as my hobbies.", {"entities": [(9, 15, "HOBBY"), (20, 31, "HOBBY")]}),
    ("My interests include bird watching and playing tennis.", {"entities": [(13, 25, "HOBBY"), (30, 43, "HOBBY")]}),
    ("I am passionate about astronomy and scuba diving.", {"entities": [(18, 27, "HOBBY"), (32, 44, "HOBBY")]}),
    ("I love to cook and travel to new places.", {"entities": [(10, 14, "HOBBY"), (19, 32, "HOBBY")]}),
    ("My hobbies consist of painting, hiking, and playing the piano.", {"entities": [(16, 23, "HOBBY"), (25, 31, "HOBBY"), (36, 50, "HOBBY")]}),
    ("I enjoy gardening and bird watching in my free time.", {"entities": [(9, 18, "HOBBY"), (23, 35, "HOBBY")]}),
    ("I have a keen interest in learning new languages and playing chess.", {"entities": [(25, 38, "HOBBY"), (43, 55, "HOBBY")]}),
    ("Traveling and photography are my hobbies.", {"entities": [(0, 9, "HOBBY"), (14, 25, "HOBBY")]}),
    ("I like to read books and practice yoga.", {"entities": [(9, 19, "HOBBY"), (24, 32, "HOBBY")]}),
    ("My interests involve astronomy and bird watching.", {"entities": [(18, 28, "HOBBY"), (33, 45, "HOBBY")]}),
    ("I enjoy playing the guitar and cooking.", {"entities": [(9, 22, "HOBBY"), (27, 34, "HOBBY")]}),
    ("I like to hike and knit in my spare time.", {"entities": [(9, 13, "HOBBY"), (18, 22, "HOBBY")]}),
    ("I spend my weekends gardening and watching movies.", {"entities": [(20, 29, "HOBBY"), (34, 49, "HOBBY")]}),
    ("My hobbies include playing tennis and painting landscapes.", {"entities": [(20, 31, "HOBBY"), (36, 52, "HOBBY")]}),
    ("I am interested in astronomy and photography.", {"entities": [(19, 29, "HOBBY"), (34, 45, "HOBBY")]}),
    ("I enjoy bird watching and scuba diving as my hobbies.", {"entities": [(9, 21, "HOBBY"), (26, 38, "HOBBY")]}),
    ("I love to read books and travel to new destinations.", {"entities": [(10, 20, "HOBBY"), (25, 39, "HOBBY")]}),
    ("My interests include playing chess and learning new languages.", {"entities": [(18, 30, "HOBBY"), (35, 53, "HOBBY")]}),
    ("I am passionate about painting and hiking.", {"entities": [(18, 25, "HOBBY"), (30, 36, "HOBBY")]}),
    ("I enjoy knitting and watching movies with friends.", {"entities": [(9, 16, "HOBBY"), (21, 46, "HOBBY")]}),
    ("I like to play the piano and practice yoga.", {"entities": [(9, 21, "HOBBY"), (26, 34, "HOBBY")]}),
    ("I spend my weekends reading classic literature and painting.", {"entities": [(27, 45, "HOBBY"), (50, 57, "HOBBY")]}),
    ("My hobbies consist of scuba diving and bird watching.", {"entities": [(16, 28, "HOBBY"), (33, 45, "HOBBY")]})
]

nlp = spacy.load('en_core_web_sm')
docs = []
for text, annot in TRAIN_DATA[:70]:
    doc = nlp(text)
    tags = offsets_to_biluo_tags(doc, annot['entities'])
    entities = biluo_tags_to_spans(doc, tags)
    doc.ents = entities
    docs.append(doc)

srsly.write_json("./model/train.json", [docs_to_json(docs)])

docs = []
for text, annot in TRAIN_DATA[70:]:
    doc = nlp(text)
    tags = offsets_to_biluo_tags(doc, annot['entities'])
    entities = biluo_tags_to_spans(doc, tags)
    doc.ents = entities
    docs.append(doc)

srsly.write_json("./model/dev.json", [docs_to_json(docs)])

