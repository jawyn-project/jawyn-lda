import os

from gensim import corpora, models
import gensim

def encontrar_topicos_relevantes(ldamodel, termo):
    topicos_relevantes = []
    for topic_id, topic in ldamodel.show_topics(formatted=False, num_words=10):
        for word, weight in topic:
            if termo == word:
                topicos_relevantes.append((topic_id, topic))
                break
    return topicos_relevantes

def preprocessar_documentos(documentos):
    texts = [[word for word in document.lower().split()] for document in documentos]
    dictionary = corpora.Dictionary(texts)
    corpus = [dictionary.doc2bow(text) for text in texts]
    return dictionary, corpus

def criar_modelo_lda(corpus, dictionary, num_topics=2, passes=15):
    ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=num_topics, id2word=dictionary, passes=passes)
    return ldamodel


def analisar_topicos_e_relevancia(ldamodel, termo_pesquisa):
    topicos_relevantes = encontrar_topicos_relevantes(ldamodel, termo_pesquisa)
    topicos_formatados = [(topic_id, [(word, round(weight, 4)) for word, weight in topic]) for topic_id, topic in
                          topicos_relevantes]

    # Supondo que queremos retornar também os tópicos brutos juntamente com os formatados
    # Se 'topicos_relevantes' estiver vazio, garantimos que retornamos algo válido
    return topicos_relevantes, topicos_formatados


def modelSave(lda_model, dictionary, corpus, model_path, dictionary_path, corpus_path):
    # Cria o diretório para o modelo se não existir
    model_dir = os.path.dirname(model_path)
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
    # Salva o modelo LDA
    lda_model.save(model_path)
    # Salva o dicionário
    dictionary.save(dictionary_path)
    # Salva o corpus em formato Market Matrix
    corpora.MmCorpus.serialize(corpus_path, corpus)

def modelLoad(model_path, dictionary_path, corpus_path):
    loaded_lda_model = gensim.models.ldamodel.LdaModel.load(model_path)
    loaded_dictionary = corpora.Dictionary.load(dictionary_path)
    loaded_corpus = corpora.MmCorpus(corpus_path)
    return loaded_lda_model, loaded_dictionary, loaded_corpus

# Certifique-se de ajustar estes caminhos para um diretório onde você tenha permissão de escrita
model_path = 'model'

# Definindo os documentos
documentos = [
    "pesquisar google interessante descobrir conhecimento clarificar desvendar descobrir decifrar desenterrar desvelar desvendar decifrar discernir deslindar perscrutar esquadrinhar pesquisar esmiuçar escrutinar deslindar discernir entender investigar examinar explorar averiguar estudar aprender indagar",
    "tecnologia inovação notícias avanços online ",
    "leitura livros aventura filmes cinemas entretenimento"
]
dictionary, corpus = preprocessar_documentos(documentos)

# Executando a função principal com o termo de pesquisa "google"
termo_pesquisa = "cinemas"
num_topics = 3
passes = 15

# Ajuste os caminhos conforme necessário
model_path = 'C:\\Users\\jader\\Desktop\\estudos\\model\\lda_model.gensim'
dictionary_path = 'C:\\Users\\jader\\Desktop\\estudos\\model\\dictionary.gensim'
corpus_path = 'C:\\Users\\jader\\Desktop\\estudos\\model\\corpus.mm'

ldamodel = criar_modelo_lda(corpus, dictionary, num_topics=2, passes=15)
# Ajuste a chamada da função conforme a nova definição

# Depois do treinamento, chame modelSave para salvar o modelo, dicionário e corpus
modelSave(ldamodel, dictionary, corpus, model_path, dictionary_path, corpus_path)