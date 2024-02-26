from createdata import crialista
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


searchResult = crialista()

# Search Result Possui a Estrutura (id, titulo, descricao, link)
# Eu quero utilizando o LDA, selecionar a melhor pagina para dada pesquisa.

# Pre-processamento e extração de características com a nova estrutura
documents = [result['descricao'] for result in searchResult]  # Usando apenas a descrição

# Vectorização dos documentos usando Bag of Words com as descrições
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform(documents)

# Aplicação do LDA com a nova estrutura
lda = LatentDirichletAllocation(n_components=50, random_state=0)  # Ajustar n_components conforme necessário
lda.fit(X)

# Visualização dos tópicos com a nova estrutura
topics = lda.components_

# Exibindo as palavras associadas a cada tópico com a nova estrutura
words = vectorizer.get_feature_names_out()
topic_words = {}

for topic_idx, topic in enumerate(topics):
    top_words_idx = topic.argsort()[-10:][::-1]  # Pegar as 10 palavras mais relevantes para o tópico
    topic_words[topic_idx] = [words[i] for i in top_words_idx]

print(topic_words)

# Obtenção da distribuição de tópicos para os documentos
document_topics = lda.transform(X)

# Processamento da consulta de pesquisa
query = "ciencia"  # Substitua por sua consulta específica
query_vector = vectorizer.transform([query])

# Utilização do LDA para obter a distribuição de tópicos para a consulta
query_topic_distribution = lda.transform(query_vector)

# Identificando o tópico principal para a consulta
main_topic_for_query = np.argmax(query_topic_distribution)
print(query_topic_distribution)

print(f"O tópico principal para a consulta '{query}' é o Tópico {main_topic_for_query}.")
print(topic_words[main_topic_for_query])