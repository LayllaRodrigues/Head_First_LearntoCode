#Avise o pythion que usaremos random 
#impotando modulo função random 

import random

#Fazendo 3 listas: uma de verbos, uma de adjetivos, uma de substantivos

verbs = ['Leverage', 'Sync', 'Target',
         'Gamify', 'Offline', 'Crowd-sourced',
         '24/7', 'Lean-in', '30,000 foot']

adjectives = ['A/B Tested', 'Freemium',
              'Hyperlocal', 'Siloed', 'B-to-B',
              'Oriented', 'Cloud-based', 
              'API-based']


nouns = ['Early Adopter', 'Low-hanging Fruit',
         'Pipeline', 'Splash Page', 'Productivity',
         'Process', 'Tipping Point', 'Paradigm']

#Escolhendo um verbo, adjetivo, substantivo

verbs = random.choice (verbs) 
adjectives = random.choice (adjectives) 
nouns = random.choice (nouns)


#Construindo uma frase, usando as palavras
phrase = verbs + ' ' + adjectives + ' ' + nouns

#Imprimindo a frase 
print(phrase)

