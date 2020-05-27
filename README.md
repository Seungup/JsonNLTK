## NLTK Result -> json format

#### pip install nltk

TODO:
```bash
$ python
```
```python
>> import nltk
>> nltk.download()
```

### USE EXAMPLE 
```bash
$ python main.py {word} {argv}
```

### argv

      -p 
      Default: True
      Exp : Show the Json format in the consol line
      
      -s={json_file_name}
      Default: False
      Exp : Save to the Json format in main.py folder
      
      
      
### example 
```bash
$ python main.py hello

{
  "Target": "hello",
  "Synsets": {
      "1": {
          "definition": "an expression of greeting",
          "pos": "n",
          "examples": [
              "every morning they exchanged polite hellos"
          ]
        }
    },
    "Synonyms": [
        "hullo",
        "howdy",
        "hi",
        "how-do-you-do",
        "hello"
    ],
    "Antonyms": []
}
```

```bash
$ ls

  main.py
  CJsonNLTK.py
  
$ python main.py hello -s=json_file_name

$ ls
  
  main.py
  CJsonNLTK.py
  json_file_name.json
```
