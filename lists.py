# -*- coding: utf-8 -*-
"""
Created on Fri Mar 28 13:57:57 2025

@author: Professional
"""

# mevalar = ['olma', 'nok', "banan"]
# moshinla = ["bmw", "onix", 'kaptiva',"nexia"]
# narxlar = [1000,5000,9000,15000,3000]
# sonla = [1,-2,1.75,-8.5,"uch",'besh']
# bolla = []

# print("1 - meva ", mevalar[0])
# print(mevalar[-1])

# mevalar = ['olma', 'nok', "banan"]
# hayvonlar = ['it', 'mushuk', 'qo\'y', 'mol', 'it']

# zakaz_1 = ['sazan', 'non', 'choy', 'achichuk', 'shashlik']
# otmena = zakaz_1.pop(-1) #1chi listdan olb wu qiymatga ozlashtirb beradi
# print("men " + otmena + " otmen qildim")
# print("qogan zakazlar: ", zakaz_1)

#list_name.remove("product_name") nom boyicha ochiradi
#list_name.insert(index_product,'new_product') xoxlagan indexga yangi ma'lumot qoshish
#list_name.append('product_name') list oxiriga berilgan ma'lumotni qo'shadi
#del = list_name[index_number] index bo'yicha o'chirish
#list_name.sort() listni alfabit bo'yicha sartirovka qb beradi
#list_name.sort(reverse=True) listni alfabit bo'yicha teskari sartirovka qb beradi
#sorted(list_name) listni asl tartibini buzme sartirovka qb print qb beradi
#sorted(list_name,reverse=True) listni asl tartibini buzme alfabit bo'yicha teskari sartirovka qb print qb beradi
#list_name.reverse() listni teskari aylantirb chiqarb beradi
#len(list_name) ro'yxat uzunligini qaytaradi elementla soniniyam
#element_name = list(range(boshlangich_son,...gacha bo'lgan son)) ma'lum oraliqdagi sonlardan list yaratb beradi
#element_name = list(range(boshlangich_son,...gacha bo'lgan son, qadam)) ma'lum oraliqdagi sonlardan list yaratb beradi unga qadamni qo'shish orqali juft yoki toq sonlarni yoki hohlagancha qadamlarni oshirb borish mumkin
#

#-------------------Amaliyot---------------------

# davlatlar = ['Moxiko', 'Uzb', 'USA', 'UK', 'BAA', 'Russian']
# print(sorted(davlatlar,reverse=True))
# davlatlar.sort()
# davlatlar.sort(reverse=True)
# print(davlatlar)
# juft_sonlar = list(range(120,1200,2))
# print(juft_sonlar)
# summa_juft_sonlar = sum(juft_sonlar)
# print(max(juft_sonlar) - min(juft_sonlar))

# print(juft_sonlar[0:7]) 
# print(juft_sonlar[len(juft_sonlar)//2:len(juft_sonlar)//2+6])
# print(juft_sonlar[-6:-1])


taomlar = ['Sazan', 'mastava', 'kasha', 'tuxum', 'lagman']
nonushta = taomlar[:]
nonushta.remove("Sazan")
nonushta.remove("mastava")
nonushta.remove("lagman")
nonushta.append("Sasiska")
nonushta.append("Saryog")
nonushta = tuple(nonushta)
nonushta[0] = "qaymoq va non"






























