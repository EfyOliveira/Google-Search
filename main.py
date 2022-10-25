from googlesearch import search
# pip install google

# Texto a ser pesquisado
query = "cyberpunk.rs"

# lang = linguagem da pesquisa "en - ingles ou pt - portugues".
# num = quantidade de resultado.
# stop = parar quando tiver 10 resultado.
# pause = tempo em segudos de intervalo entre resultados.
def googlesearch()
  for result in search(query, lang="en", num=10, stop=10, pause=2):
      print(result)
      
