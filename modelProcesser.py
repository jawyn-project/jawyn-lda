from trainModel import modelLoad, analisar_topicos_e_relevancia

# Executando a função principal com o termo de pesquisa "google"
termo_pesquisa = "cinemas"
num_topics = 3
passes = 15

# Ajuste os caminhos conforme necessário
model_path = 'C:\\Users\\jader\\Desktop\\estudos\\model\\lda_model.gensim'
dictionary_path = 'C:\\Users\\jader\\Desktop\\estudos\\model\\dictionary.gensim'
corpus_path = 'C:\\Users\\jader\\Desktop\\estudos\\model\\corpus.mm'

loaded_lda_model, loaded_dictionary, loaded_corpus = modelLoad(model_path, dictionary_path, corpus_path)

topicos_relevantes, topicos_relevantes_formatados = analisar_topicos_e_relevancia(loaded_lda_model, termo_pesquisa)

for idx, topic in loaded_lda_model.print_topics(-1):
    print(f"Tópico: {idx}\nPalavras: {topic}\n")

# Agora, mesmo que 'analisar_topicos_e_relevancia' retorne listas vazias, o código não resultará em erro
print(topicos_relevantes, topicos_relevantes_formatados)