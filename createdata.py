# Função para criar uma estrutura de dados com id, título, descrição e link
def criar_estrutura(id, titulo, descricao, link):
    """
    Cria e retorna uma estrutura de dados contendo um id, título, descrição e link.

    Parâmetros:
    - id (int): O identificador do item.
    - titulo (str): O título do item.
    - descricao (str): A descrição do item.
    - link (str): O link para mais informações sobre o item.

    Retorna:
    - dict: Um dicionário contendo as informações do item.
    """
    item = {
        "id": id,
        "titulo": titulo,
        "descricao": descricao,
        "link": link
    }
    return item

def adiciona_lista(lista_itens, id, titulo, descricao, link):
    """
    Adiciona um item a uma lista existente de itens, com cada item contendo um id, título, descrição e link.

    Parâmetros:
    - lista_itens (list): A lista de itens existente.
    - id (int): O identificador do item.
    - titulo (str): O título do item.
    - descricao (str): A descrição do item.
    - link (str): O link para mais informações sobre o item.
    """
    item = {
        "id": id,
        "titulo": titulo,
        "descricao": descricao,
        "link": link
    }
    lista_itens.append(item)
lista_itens = []  # Inicializa uma lista vazia
def createLista(lista_itens):
    adiciona_lista(lista_itens, 1, "Google", "pesquisar,google,interessante,descobrir", "http://google.com")
    adiciona_lista(lista_itens, 2, "TechNova", "tecnologia,inovação,notícias,avanços", "http://technova.com")
    adiciona_lista(lista_itens, 3, "Mundo dos Livros", "leitura,livros,aventura,conhecimento",
                   "http://mundodoslivros.com")
    adiciona_lista(lista_itens, 4, "Viagem Espacial", "espaço,viagem,planetas,exploração", "http://viagemespacial.com")
    adiciona_lista(lista_itens, 5, "Saúde Diária", "saúde,bem-estar,vida saudável,dicas", "http://saudediaria.com")
    adiciona_lista(lista_itens, 6, "A Arte da Culinária", "culinária,receitas,gastronomia,sabores",
                   "http://artedaculinaria.com")
    adiciona_lista(lista_itens, 7, "Cinema Mundial", "cinema,filmes,estreias,resenhas", "http://cinemamundial.com")
    adiciona_lista(lista_itens, 8, "Inovação Verde", "sustentabilidade,meio ambiente,verde,ecologia",
                   "http://inovacaoverde.com")
    adiciona_lista(lista_itens, 9, "História Global", "história,culturas,antiguidades,descobertas",
                   "http://historiaglobal.com")
    adiciona_lista(lista_itens, 10, "Mundo dos Games", "games,jogos,videogames,tecnologia", "http://mundodosgames.com")
    adiciona_lista(lista_itens, 11, "Planeta Tech", "tecnologia, inovação, futuro, gadgets", "http://planetatech.com")
    adiciona_lista(lista_itens, 12, "Viajante Anônimo", "viagens, culturas, aventuras, destinos",
                   "http://viajanteanonimo.com")
    adiciona_lista(lista_itens, 13, "Desenvolvedor Moderno", "desenvolvimento, programação, software, tecnologia",
                   "http://desenvolvedormoderno.com")
    adiciona_lista(lista_itens, 14, "Mestre do DIY", "faça você mesmo, projetos, artesanato, criatividade",
                   "http://mestredodiy.com")
    adiciona_lista(lista_itens, 15, "Mundo Fitness", "fitness, saúde, exercícios, bem-estar", "http://mundofitness.com")
    adiciona_lista(lista_itens, 16, "Zen Vida", "meditação, yoga, bem-estar, paz interior", "http://zenvida.com")
    adiciona_lista(lista_itens, 17, "Receitas do Mundo", "culinária, receitas, gastronomia, sabores do mundo",
                   "http://receitasdomundo.com")
    adiciona_lista(lista_itens, 18, "Aventuras Urbanas", "cidade, aventuras, cultura urbana, exploração",
                   "http://aventurasurbanas.com")
    adiciona_lista(lista_itens, 19, "Eco Sustentável", "sustentabilidade, ecologia, verde, meio ambiente",
                   "http://ecosustentavel.com")
    adiciona_lista(lista_itens, 20, "Mundo Pet", "animais de estimação, cuidados, dicas, saúde animal",
                   "http://mundopet.com")
    adiciona_lista(lista_itens, 21, "Astronomia em Foco", "astronomia, estrelas, planetas, exploração espacial",
                   "http://astronomiaemfoco.com")
    adiciona_lista(lista_itens, 22, "Negócios Inteligentes", "empreendedorismo, negócios, estratégias, inovação",
                   "http://negociosinteligentes.com")
    adiciona_lista(lista_itens, 23, "Arte Inspiradora", "arte, inspiração, criação, expressão",
                   "http://arteinspiradora.com")
    adiciona_lista(lista_itens, 24, "Jardim Secreto", "jardinagem, plantas, natureza, paisagismo",
                   "http://jardimsecreto.com")
    adiciona_lista(lista_itens, 25, "Cinema em Cena", "cinema, filmes, críticas, lançamentos",
                   "http://cinemaemcena.com")
    adiciona_lista(lista_itens, 26, "Negócios Verdes", "sustentabilidade, negócios, ecologia, responsabilidade social",
                   "http://negociosverdes.com")
    adiciona_lista(lista_itens, 27, "Aprendizado Online",
                   "educação, cursos online, aprendizado, desenvolvimento pessoal", "http://aprendizadoonline.com")
    adiciona_lista(lista_itens, 28, "Estilo de Vida Minimalista", "minimalismo, vida simples, organização, bem-estar",
                   "http://minimalista.com")
    adiciona_lista(lista_itens, 29, "Fotografia em Foco", "fotografia, técnicas, equipamentos, inspiração",
                   "http://fotografiaemfoco.com")
    adiciona_lista(lista_itens, 30, "Aventuras na Cozinha",
                   "culinária, gastronomia, experiências culinárias, descobertas", "http://aventurasnacozinha.com")
    adiciona_lista(lista_itens, 31, "Explorando Natureza", "natureza, aventura, ecoturismo, trilhas",
                   "http://explorandonatureza.com")
    adiciona_lista(lista_itens, 32, "Fashion Trends", "moda, tendências, estilo, dicas de moda",
                   "http://fashiontrends.com")
    adiciona_lista(lista_itens, 33, "Finanças Inteligentes",
                   "finanças pessoais, investimentos, economia, planejamento financeiro",
                   "http://financasinteligentes.com")
    adiciona_lista(lista_itens, 34, "Gamer's World", "jogos, videogames, análises, novidades", "http://gamersworld.com")
    adiciona_lista(lista_itens, 35, "Bem-Estar Natural",
                   "saúde natural, medicina alternativa, terapias holísticas, equilíbrio", "http://bemestarnatural.com")
    adiciona_lista(lista_itens, 36, "Leitura Ilimitada", "livros, resenhas, literatura, recomendações de leitura",
                   "http://leiturailimitada.com")
    adiciona_lista(lista_itens, 37, "Arte Culinária", "culinária, arte, chefes renomados, experiências gastronômicas",
                   "http://arteculinaria.com")
    adiciona_lista(lista_itens, 38, "Turismo Radical", "aventura, esportes radicais, adrenalina, destinos extremos",
                   "http://turismoradical.com")
    adiciona_lista(lista_itens, 39, "Saúde Mental em Foco",
                   "saúde mental, psicologia, bem-estar emocional, autoconhecimento", "http://saudementalemfoco.com")
    adiciona_lista(lista_itens, 40, "Tecnologia do Futuro", "inovação, tecnologia de ponta, futurismo, tendências",
                   "http://tecnologiadofuturo.com")
    adiciona_lista(lista_itens, 41, "Música em Harmonia", "música, artistas, bandas, concertos",
                   "http://musicaemharmonia.com")
    adiciona_lista(lista_itens, 42, "Viagens Espaciais", "espaço, exploração espacial, astronautas, missões",
                   "http://viagensespaciais.com")
    adiciona_lista(lista_itens, 43, "Mindfulness Diário",
                   "mindfulness, atenção plena, práticas de meditação, relaxamento", "http://mindfulnessdiario.com")
    adiciona_lista(lista_itens, 44, "Educação Inovadora",
                   "educação, metodologias inovadoras, aprendizado ativo, tecnologia educacional",
                   "http://educacaoinovadora.com")
    adiciona_lista(lista_itens, 45, "Estilo de Vida Saudável", "saúde, bem-estar, nutrição, atividade física",
                   "http://estilodevidasaudavel.com")
    adiciona_lista(lista_itens, 46, "Arquitetura Inspiradora",
                   "arquitetura, design, construção sustentável, espaços urbanos", "http://arquiteturainspiradora.com")
    adiciona_lista(lista_itens, 47, "História em Foco",
                   "história, civilizações antigas, eventos históricos, curiosidades", "http://historiaemfoco.com")
    adiciona_lista(lista_itens, 48, "Crescimento Pessoal", "autoajuda, desenvolvimento pessoal, motivação, superação",
                   "http://crescimentopessoal.com")
    adiciona_lista(lista_itens, 49, "Gastronomia Internacional",
                   "culinária, pratos típicos, gastronomia mundial, viagem gastronômica",
                   "http://gastronomiainternacional.com")
    adiciona_lista(lista_itens, 50, "Ecoturismo Aventura",
                   "ecoturismo, natureza, aventura ao ar livre, preservação ambiental", "http://ecoturismoaventura.com")
    adiciona_lista(lista_itens, 51, "Tech Trends", "tecnologia, tendências, inovações, gadgets",
                   "http://techtrends.com")
    adiciona_lista(lista_itens, 52, "Mente Criativa", "criatividade, inspiração, arte, projetos DIY",
                   "http://mentecriativa.com")
    adiciona_lista(lista_itens, 53, "Aventuras Subaquáticas",
                   "mergulho, oceanografia, vida marinha, destinos submarinos", "http://aventurassubaquaticas.com")
    adiciona_lista(lista_itens, 54, "Astronomia Divertida",
                   "astronomia, curiosidades espaciais, eventos astronômicos, astronomia amadora",
                   "http://astronomiadivertida.com")
    adiciona_lista(lista_itens, 55, "Turismo Cultural", "cultura, viagens, patrimônio histórico, experiências locais",
                   "http://turismocultural.com")
    adiciona_lista(lista_itens, 56, "Vida Saudável em Família",
                   "saúde familiar, atividade física, alimentação saudável, bem-estar",
                   "http://vidasaudavelfamilia.com")
    adiciona_lista(lista_itens, 57, "Arte Urbana", "arte de rua, grafite, intervenções urbanas, cultura urbana",
                   "http://arteurbana.com")
    adiciona_lista(lista_itens, 58, "Consciência Ambiental",
                   "sustentabilidade, conservação, reciclagem, ativismo ambiental", "http://conscienciaambiental.com")
    adiciona_lista(lista_itens, 59, "Futuro do Trabalho",
                   "trabalho remoto, automação, mercado de trabalho, carreira profissional",
                   "http://futurodotrabalho.com")
    adiciona_lista(lista_itens, 60, "Pets Aventura",
                   "aventuras com animais de estimação, dicas de viagem pet-friendly, cuidados",
                   "http://petsaventura.com")
    adiciona_lista(lista_itens, 61, "Mundo da Robótica", "robótica, inteligência artificial, automação, drones",
                   "http://mundodarobotica.com")
    adiciona_lista(lista_itens, 62, "Bem-Estar Animal",
                   "cuidados com animais, comportamento animal, adoção responsável, veterinária",
                   "http://bemestaranimal.com")
    adiciona_lista(lista_itens, 63, "Turismo Ecológico",
                   "ecoturismo, preservação ambiental, destinos sustentáveis, trilhas", "http://turismoecologico.com")
    adiciona_lista(lista_itens, 64, "Gourmet Explorador",
                   "gastronomia, culinária gourmet, chefs renomados, experiências culinárias",
                   "http://gourmetexplorador.com")
    adiciona_lista(lista_itens, 65, "Saúde em Movimento", "fitness, exercícios, saúde preventiva, qualidade de vida",
                   "http://saudeemmovimento.com")
    adiciona_lista(lista_itens, 66, "Jornada Espiritual", "espiritualidade, autoconhecimento, meditação, reflexão",
                   "http://jornadaespiritual.com")
    adiciona_lista(lista_itens, 67, "Arte Digital", "arte digital, design gráfico, ilustração, animação",
                   "http://artedigital.com")
    adiciona_lista(lista_itens, 68, "Viagens Exóticas", "viagens, destinos exóticos, culturas milenares, aventura",
                   "http://viagemsexoticas.com")
    adiciona_lista(lista_itens, 69, "Aventuras na Natureza", "aventura ao ar livre, camping, trilhas, sobrevivência",
                   "http://aventurasnanatureza.com")
    adiciona_lista(lista_itens, 70, "Gastronomia Fusion",
                   "culinária, fusão de sabores, gastronomia internacional, inovação culinária",
                   "http://gastronomiafusion.com")
    adiciona_lista(lista_itens, 71, "Tecnologia Avançada",
                   "tecnologia de ponta, inovação, gadgets futuristas, inteligência artificial",
                   "http://tecnologiaavancada.com")
    adiciona_lista(lista_itens, 72, "Vida Sustentável",
                   "sustentabilidade, consumo consciente, energia renovável, permacultura",
                   "http://vidasustentavel.com")
    adiciona_lista(lista_itens, 73, "Universo Geek", "cultura geek, filmes, séries, jogos, quadrinhos",
                   "http://universogeek.com")
    adiciona_lista(lista_itens, 74, "Turismo Aventura", "aventura, ecoturismo, esportes radicais, adrenalina",
                   "http://turismoaventura.com")
    adiciona_lista(lista_itens, 75, "Bem-Estar Holístico",
                   "bem-estar, saúde integral, terapias alternativas, equilíbrio emocional",
                   "http://bemestarholistico.com")
    adiciona_lista(lista_itens, 76, "Construções Sustentáveis",
                   "arquitetura sustentável, construção ecológica, eficiência energética, reciclagem",
                   "http://construcoessustentaveis.com")
    adiciona_lista(lista_itens, 77, "Estilo de Vida Vegano",
                   "veganismo, alimentação saudável, moda ética, ativismo animal", "http://estilodevidavegano.com")
    adiciona_lista(lista_itens, 78, "Aventuras Selvagens", "aventura na selva, expedições, vida selvagem, descobertas",
                   "http://aventurasselvagens.com")
    adiciona_lista(lista_itens, 79, "Ciência em Pauta",
                   "ciência, descobertas, pesquisas científicas, inovações tecnológicas", "http://cienciaempauta.com")
    adiciona_lista(lista_itens, 80, "Dicas de Viagem", "viagens, turismo, destinos, roteiros, experiências",
                   "http://dicasdeviagem.com")
    adiciona_lista(lista_itens, 81, "Gastronomia Gourmet",
                   "culinária gourmet, chefs, receitas sofisticadas, degustações", "http://gastronomiagourmet.com")
    adiciona_lista(lista_itens, 82, "Vida Zen", "espiritualidade, mindfulness, meditação, harmonia interior",
                   "http://vidazen.com")
    adiciona_lista(lista_itens, 83, "Mundo da Dança", "dança, coreografias, eventos de dança, estilos de dança",
                   "http://mundodadanca.com")
    adiciona_lista(lista_itens, 84, "Desenvolvimento Pessoal",
                   "autoajuda, coaching, crescimento pessoal, realização de objetivos",
                   "http://desenvolvimentopessoal.com")
    adiciona_lista(lista_itens, 85, "Aventuras Aquáticas", "esportes aquáticos, mergulho, surf, vela, canoagem",
                   "http://aventurasaquaticas.com")
    adiciona_lista(lista_itens, 86, "Educação Ambiental",
                   "educação ambiental, sustentabilidade, preservação, conscientização", "http://educacaoambiental.com")
    adiciona_lista(lista_itens, 87, "Fotografia de Natureza", "fotografia de paisagens, vida selvagem, flora, fauna",
                   "http://fotografiadenatureza.com")
    adiciona_lista(lista_itens, 88, "Turismo Cultural", "turismo cultural, patrimônio histórico, tradições, festivais",
                   "http://turismocultural.com")
    adiciona_lista(lista_itens, 89, "Gastronomia Internacional",
                   "culinária mundial, pratos típicos, chefs internacionais, experiências gastronômicas",
                   "http://gastronomiainternacional.com")
    adiciona_lista(lista_itens, 90, "Bem-Estar na Terceira Idade",
                   "saúde na terceira idade, atividades físicas, cuidados com a mente, qualidade de vida",
                   "http://bemestarnaterceiraidade.com")
    adiciona_lista(lista_itens, 91, "Aventuras na Montanha", "alpinismo, escalada, trekking, acampamento",
                   "http://aventurasnamontanha.com")
    adiciona_lista(lista_itens, 92, "Ciência Cidadã",
                   "ciência participativa, contribuição científica, projetos de pesquisa comunitária",
                   "http://cienciacidada.com")
    adiciona_lista(lista_itens, 93, "Arte Contemporânea",
                   "arte moderna, exposições, artistas contemporâneos, crítica de arte", "http://artecontemporanea.com")
    adiciona_lista(lista_itens, 94, "Turismo Rural", "turismo em áreas rurais, agroturismo, experiências no campo",
                   "http://turismorural.com")
    adiciona_lista(lista_itens, 95, "Negócios Sustentáveis",
                   "empreendedorismo sustentável, negócios verdes, responsabilidade social corporativa",
                   "http://negociossustentaveis.com")
    adiciona_lista(lista_itens, 96, "Jardinagem Urbana",
                   "cultivo em espaços urbanos, hortas urbanas, paisagismo urbano", "http://jardinagemurbana.com")
    adiciona_lista(lista_itens, 97, "Culinária Saudável",
                   "receitas saudáveis, alimentação equilibrada, culinária funcional", "http://culinariasaudavel.com")
    adiciona_lista(lista_itens, 98, "Mundo dos Negócios", "economia, finanças, empreendedorismo, gestão empresarial",
                   "http://mundodosnegocios.com")
    adiciona_lista(lista_itens, 99, "Viagens Fotográficas",
                   "viagens para fotografia, workshops de fotografia, tours fotográficos",
                   "http://viagensfotograficas.com")
    adiciona_lista(lista_itens, 100, "Gastronomia Molecular",
                   "culinária molecular, técnicas de vanguarda, experimentação culinária",
                   "http://gastronomiamolecular.com")
    adiciona_lista(lista_itens, 101, "Bem-Estar na Gravidez",
                   "saúde materna, cuidados na gestação, preparação para o parto, nutrição",
                   "http://bemestarnagravidez.com")
    adiciona_lista(lista_itens, 102, "Ecologia Urbana",
                   "sustentabilidade urbana, planejamento urbano sustentável, mobilidade urbana",
                   "http://ecologiaurbana.com")
    adiciona_lista(lista_itens, 103, "Meditação Guiada",
                   "meditação, mindfulness, relaxamento, práticas de meditação guiada", "http://meditacaoguiada.com")
    adiciona_lista(lista_itens, 104, "Gastronomia Regional",
                   "culinária regional, pratos típicos, gastronomia local, tradições culinárias",
                   "http://gastronomiaregional.com")
    adiciona_lista(lista_itens, 105, "Desenvolvimento de Jogos",
                   "desenvolvimento de videogames, programação de jogos, game design",
                   "http://desenvolvimentodejogos.com")
    adiciona_lista(lista_itens, 106, "Turismo de Aventura",
                   "aventura ao ar livre, esportes radicais, ecoturismo, experiências emocionantes",
                   "http://turismodeaventura.com")
    adiciona_lista(lista_itens, 107, "Astronomia Amadora",
                   "astronomia para iniciantes, observação do céu, telescópios, eventos astronômicos",
                   "http://astronomiaamadora.com")
    adiciona_lista(lista_itens, 108, "Bem-Estar Corporativo",
                   "saúde no trabalho, qualidade de vida no ambiente corporativo, programas de bem-estar",
                   "http://bemestarcorporativo.com")
    adiciona_lista(lista_itens, 109, "Gastronomia Tradicional",
                   "culinária tradicional, receitas ancestrais, comida de conforto, gastronomia familiar",
                   "http://gastronomiatradicional.com")
    adiciona_lista(lista_itens, 110, "Aventuras de Inverno",
                   "esportes de inverno, esqui, snowboard, viagens para destinos gelados",
                   "http://aventurasdeinverno.com")

def crialista():
    lista_itens = []
    createLista(lista_itens)
    return lista_itens

createLista(lista_itens)
# Imprimindo a lista para verificar
for item in lista_itens:
    print(item)
