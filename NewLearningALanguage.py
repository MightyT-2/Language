import json
import os

# Functions
# Greeting to the user
def salutations():
   print('This program is based on my "New Learning a Language" vocabulary list. It')
   print('will, following this list, take in a list of words in other languages to')
   print('create a base vocabulary list to start learning from.')
   return
# Give the user prompts on what to enter
def instructions(printOption):
   if printOption == 0:
      print('Would you like to continue (y/n)?')
   elif printOption == 1:
      print('Enter a language.')
   elif printOption == 2:
      print('Enter the translation.')
   elif printOption == 3:
      print('Enter the tag info.')
   elif printOption == 4:
      print('You have autosaved data, would you like to continue (y/n)')
   else:
      print('Instruction error.')
   return
# Load the dictionary data
def load_Data():
   data = json.load(open('Dictionaries\\New Learning a Language.json', encoding='utf-8'))
   return data
# Determine if the user wants to continue
def get_User_Response():
   answer = ''
   while answer not in ['y', 'n']:
      answer = input(' >> ')
   return answer
# Get a language to define
def get_Target_Language(dictionary):
   answer = 'English'
   while answer in dictionary:
      answer = input(' >> ').capitalize()
   return answer
# Define a new language
def define_language(language, tags, dictionary):
   words = []
   dictionary[language] = dictionary['English']
   for x in dictionary[language]:
      words = dictionary[language][x]
      dictionary[language][x] = {}
      for y in words:
         dictionary[language][x][y] = {}
         for z in tags:
            dictionary[language][x][y][z] = ''
   return
# Get a list of different features to know about the language
def get_Tags():
   answers = []
   add = 'definition'
   while add != '':
      answers.append(add)
      add = input(' >> ')
   return answers
# Define the words
def define_Words(language, category, word, dictionary):
   for tag in dictionary[language][category][word]:
      dictionary[language][category][word][tag] = input(tag + ' >> ')
   return
# Save the dictionary data
def save_Data(dictionary):
   json.dump(dictionary, open('Dictionaries\\New Learning a Language.json', 'w', encoding='utf-8'), indent=3)
   return
# Farewell to the user
def valedictions():
   print('Thank you for using this program, have a good day.')
   return

# Variables
dictionary = {}
language   = ''
tags       = []
vocab      = ''

# Main logic
salutations()
print('')
instructions(0)
dictionary = load_Data()
while get_User_Response() == 'y':

   instructions(1)
   language = get_Target_Language(dictionary)
   instructions(3)
   tags     = get_Tags()
   define_language(language, tags, dictionary)
   instructions(2)
   for categories in dictionary[language]:
      for words in dictionary[language][categories]:
         print('Define ' + words + ':')
         define_Words(language, categories, words, dictionary)
   save_Data(dictionary)
valedictions()