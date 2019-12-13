#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  total_batches=float("inf")#of complete recipe
  for key in  recipe.keys():
    if key not in ingredients:
      return 0
    batches= ingredients[key]//recipe[key]#per ingredient how many batches

    if batches==0:
       return 0

    total_batches=min(batches,total_batches)
  return total_batches


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 732, 'butter': 158, 'flour': 51 }
  recipe_batches(recipe, ingredients)
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))