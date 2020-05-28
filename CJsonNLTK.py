"""
파이썬 라이브러리인 nltk를 json 형식으로 리턴해주기 위한 파일입니다.
"""
import nltk
import json


class CJsonNLTK:
    def __init__(self, target: str):
        self.target = target
        self.dictionary = {'Target': self.target}

    def setDefinition(self) -> None:
        """
        정의, 단어의 성분, 예제를 추가합니다.
        :return:
        """
        self.dictionary['Synsets'] = {}
        i = 0
        for synset in nltk.corpus.wordnet.synsets(self.target):
            i += 1
            self.dictionary['Synsets'][i] = {}
            self.dictionary['Synsets'][i]['definition'] = synset.definition()
            self.dictionary['Synsets'][i]['pos'] = synset.pos()
            self.dictionary['Synsets'][i]['examples'] = []
            examples = []
            for e in synset.examples():
                examples.append(e)
            self.dictionary['Synsets'][i]['examples'] = list(set(examples))

    def setSynonymsAntonyms(self) -> None:
        """
        비슷한 의미를 가진 단어, 반대의 비슷한 의미를 가진 단어를 리턴합니다.
        :return:
        """
        synonyms = []
        antonyms = []
        for syn in nltk.corpus.wordnet.synsets(self.target):
            for lemma in syn.lemmas():
                synonyms.append(lemma.name())
                if lemma.antonyms():
                    antonyms.append(lemma.antonyms()[0].name())

        # 중복 제거
        self.dictionary['Synonyms'] = list(set(synonyms))
        self.dictionary['Antonyms'] = list(set(antonyms))

    def getDictionary(self) -> dict:
        """
        현재 딕셔너리를 반환합니다.
        :return: self.dictionary
        """
        return self.dictionary

    def save2Json(self, file_name: str) -> None:
        """
        dictionary 형식을 json 파일로 저장합니다.
        :param file_name: 저장할 파일 이름
        :return: none
        """
        with open(f'./{file_name}.json', 'w') as f:
            json.dump(self.dictionary, f)

    def pprint2Json(self) -> None:
        """
        dictionary 형식을 json 형식으로 출력합니다. (개행 있음)
        :return: none
        """
        print(json.dumps(self.dictionary, sort_keys=True, indent=4, separators=(',', ': ')))

    def print2Json(self) -> None:
        """
        dictionary 형식을 json 형식으로 출력합니다. (개행 없음)
        :return:
        """
        print(json.dumps(self.dictionary))
