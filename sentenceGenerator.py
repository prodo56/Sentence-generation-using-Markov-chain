import re
import random
import sys

temporaryMapping ={}
mapping={}
startWords = []

def getTuple(wordlist):
    return tuple(wordlist)

def words(filename):
    '''
    to read all the words in the file
    :param filename:
    :return:
    '''
    listOfWords = []
    try:
        with open(filename,"r") as f:
            for w in re.findall(r"[\w']+|[.,!?;]", f.read()):
                if w.isupper() and w!="I":
                    w=w.lower()
                elif w[0].isupper():
                    w=w.lower().capitalize()
                else:
                    w=w.lower()
                listOfWords.append(w)
    except Exception as e:
        print "Error while reading list of words/file with error "+ e.message
    return listOfWords

def getTempMapping(prefixwords,followingWords):
    '''
    initial word count before normalisation
    :param prefixwords:
    :param followingWords:
    :return:
    '''
    global temporaryMapping
    first = getTuple(prefixwords)
    if first in temporaryMapping:
        if followingWords in temporaryMapping[first]:
            temporaryMapping[first][followingWords] += 1.0
        else:
            temporaryMapping[first][followingWords] = 1.0
    else:
        temporaryMapping[first] = {}
        temporaryMapping[first][followingWords] = 1.0


def generateMapping(wordList,prefixLength):
    '''
    to generate normalised word counts
    :param wordList:
    :param prefixLength:
    :return:
    '''
    global temporaryMapping
    global startWords
    startWords.append(wordList[0])
    for i in xrange(1,len(wordList)-1):
        if i<=prefixLength:
            prefixWords = wordList[:i+1]
        else:
            prefixWords = wordList[i-prefixLength+1:i+1]
        followingWords = wordList[i+1]
        if prefixWords[-1] == "." and followingWords not in ".,!?;":
            startWords.append(followingWords)
        getTempMapping(prefixWords,followingWords)
    for prefix,following in temporaryMapping.iteritems():
        totalVal = sum(following.values())
        mapping[prefix]=dict([(k, v / totalVal) for k, v in following.iteritems()])

def getNextWord(prevWordList):
    '''
    to get next word given the prefix
    :param prevWordList:
    :return:
    '''
    flag = False
    while getTuple(prevWordList) not in mapping:
        if getTuple([prevWordList[-1]]) in mapping:
            flag =True
            break
        prevWordList.pop()
    if not flag:
        next = random.choice(mapping[getTuple(prevWordList)].keys())
    else:
        next = random.choice(mapping[getTuple([prevWordList[-1]])].keys())
    return next

def generateSentence(prefixlength):
    '''
    to generate the sentences
    :param prefixlength:
    :return:
    '''
    currentWord = random.choice(startWords)
    sentence = currentWord.capitalize()
    prevWordList = [currentWord]
    sentenceLength =1
    while True:
        currentWord = getNextWord(prevWordList)
        prevWordList.append(currentWord)
        if currentWord not in ".,!?;":
            sentence += " "
        sentence += currentWord
        sentenceLength += 1
        if sentenceLength>prefixlength and currentWord in ".":
            return sentence
        if sentenceLength >=100:
            return sentence
    return sentence

def main():
    if len(sys.argv) < 3:
        print "Incorrect number of parameters. Check Usage"
    filename = sys.argv[1]
    prefixLength = int(sys.argv[2])
    numberOfSentences = int(sys.argv[3])
    wordLists = words(filename)
    generateMapping(wordLists,1)

    for i in xrange(numberOfSentences):
        print generateSentence(prefixLength)

if __name__ == "__main__":
    main()