import utils.db as db
import pandas as pd
import nltk
nltk.download('stopwords')
nltk.download('rslp')
stopWords = nltk.corpus.stopwords.words('portuguese')


def aplicaStemmer(texto):
    stemmer = nltk.stem.RSLPStemmer()
    frasesStemming = []
    for (palavras, emocao) in texto:
        comStemming = [stemmer.stem(p)
                       for p in palavras.split() if p not in stopWords]
        frasesStemming.append((comStemming, emocao))
    return frasesStemming


def buscaPalavras(frases):
    todasPalavras = []
    for palavras, emocao in frases:
        todasPalavras.extend(palavras)
    return todasPalavras


def buscaFrequencia(palavras):
    frequencias = nltk.FreqDist(palavras)
    return frequencias


def palavrasUnicas(frequencias):
    unicas = frequencias.keys()
    return unicas


def extratorPalavras(documento):
    saida = {}
    doc = set(documento)
    for pu in PU:
        if pu in doc:
            saida['%s' % pu] = True
        else:
            saida['%s' % pu] = False
    return saida


BASE = db.get_base()

listaTotalPalavras = buscaPalavras(aplicaStemmer(BASE))
len(listaTotalPalavras)

frequencia = buscaFrequencia(listaTotalPalavras)
frequencia.most_common(8)

PU = palavrasUnicas(frequencia)

frasesComStem = aplicaStemmer(BASE)
baseCompleta = nltk.classify.apply_features(extratorPalavras, frasesComStem)
classificador = nltk.NaiveBayesClassifier.train(baseCompleta)


def interpreta_frase(msg):
    saidaStem = []
    stem = nltk.RSLPStemmer()
    for p in msg.split():
        if p not in stopWords:
            saidaStem.append(stem.stem(p))
    saidaStem
    extraido = extratorPalavras(saidaStem)
    return (classificador.classify(extraido))
