import pandas as pd
import nltk
nltk.download('stopwords')
nltk.download('rslp')
stopwords = nltk.corpus.stopwords.words('portuguese')
import pandas as pd
dados=pd.read_csv(r'H:\2-UESC\MeusSemestresUESC\semestre6\redes1\Socket\Train500.csv', on_bad_lines='skip',sep=';')
dados= dados.loc[:,['tweet_text','sentiment']]
replace_values = { 0 : 'Negativo', 1 : 'Positivo' } 
dados=dados.replace({"sentiment":replace_values})
BASE = []
for index ,row in dados.iterrows():
  BASE.append((row['tweet_text'],row['sentiment']))
BASE

def aplicastemmer(texto):
  stemmer=nltk.stem.RSLPStemmer()
  frasessteming=[]
  for (palavras,emocao) in texto:
    comstemming=[stemmer.stem(p) for p in palavras.split() if p not in stopwords]
    frasessteming.append((comstemming,emocao))
    
    
    
  return frasessteming

def buscapalavras(frases):
  todaspalavras=[]
  for palavras,emocao in frases:
    todaspalavras.extend(palavras)
  return todaspalavras
listaTotalPalavras=buscapalavras(aplicastemmer(BASE))
len(listaTotalPalavras)
def busca_fraquencia(palavras):
  frequencias=nltk.FreqDist(palavras)
  return frequencias
frequencia=busca_fraquencia(listaTotalPalavras)
frequencia.most_common(8)

def palavras_unicas(frequencias):
  unicas = frequencias.keys()
  return unicas

PU=palavras_unicas(frequencia)

def extratorPalavras(documento):
  saida={}
  doc=set(documento)
  for pu in PU:
    if pu in doc:
      saida['%s' % pu]=True
    else:
      saida['%s' % pu]=False
  return saida


frasescomstem=aplicastemmer(BASE)
basecompleta=nltk.classify.apply_features(extratorPalavras,frasescomstem)
classificador = nltk.NaiveBayesClassifier.train(basecompleta)
saidastem=[]
stemm=nltk.RSLPStemmer()
teste ='Triste'
for p in teste.split():
    if p not in stopwords:
        saidastem.append(stemm.stem(p))
saidastem
extraido=extratorPalavras(saidastem)
print(classificador.classify(extraido))
