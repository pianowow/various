#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      CHRISTOPHER_IRWIN
#
# Created:     11/05/2015
# Copyright:   (c) CHRISTOPHER_IRWIN 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import json
import csv
import sqlite3

#read the file
with open('AllSets.enUS.json',encoding='utf-8') as f:
    c = json.load(f)

tot = 0
lst = [['Name','Count','Rarity','Type','Cost','Attack','Health/Durability','Text','Flavor']]

#append the given card to the list for the csv file
def appcard(card):
    c = []
    c.append(card['name'])
    c.append('2' if card['rarity'] != 'Legendary' else '1')
    c.append(card['rarity'])
    c.append(card['type'])
    c.append(card['cost'])
    c.append(card['attack'] if 'attack' in card else '')
    c.append(card['health'] if 'health' in card else card['durability'] if 'durability' in card else '')
    c.append(card['text'].replace('\n',' ') if 'text' in card else '')
    c.append(card['flavor'].replace('\n',' ') if 'flavor' in card else '')
    lst.append(tuple(c))

#loop over the cards
for st in c.keys():
    for card in c[st]:
        if 'collectible' in card and card['collectible'] and card['type'] != 'Hero':
            appcard(card)
            tot += 1

print(tot)

#write csv file
with open('cards.csv','w',newline='',encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerows(lst)

#write to database
with sqlite3.connect('cards.sqlite.db') as d:
    try:
        d.execute('drop table cards')
    except:
        None
    d.execute('create table cards (Name text,Rarity text,Count integer,Type text,Cost integer,Attack integer,Health_Durability integer,Text text,Flavor text)')
    for card in lst:
        d.execute('insert into cards values (?,?,?,?,?,?,?,?,?)', card)

