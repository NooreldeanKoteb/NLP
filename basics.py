#!/usr/bin/env python
# coding: utf-8

import nltk, math, matplotlib
import matplotlib.pyplot as plt
#If not installed uncomment
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist

#==========================================#
#Part 1
#==========================================#
with open ("hamlet.txt") as inp:
    lines = inp.readlines()

lines = ''.join(lines)
lines = lines.split('\n')
for line in lines:
    if line == '\n':
        lines.remove(line)
    
lines = ''.join(lines)

sentances = sent_tokenize(lines)

print('(a) Number of Sentances: '+str(len(sentances))+'')


words = []
for sentance in sentances:
    words.extend(sentance.split(' '))
    
print('(b) words: '+str(len(words)))



words = []
for sentance in sentances:
    words.extend(word_tokenize(sentance))
    
print('(b) words: '+str(len(words)))



lowercase = []
for word in words:
    lowercase.append(word.lower())
    
types=set(lowercase)



len_types = len(types)
len_tokens = len(words)
print('(c) Tokens: '+str(len_tokens)+' | (d) Types: '+str(len_types)+'\n')

#==========================================#
#Part 2
#==========================================#

print("Herdan's Law value of k: "+str(len_types/math.pow(len_tokens,0.7))+'\n')


#==========================================#
#Part 3
#==========================================#
fdist = FreqDist(lowercase)

ranks = []
freqs = []
ranked_words = {}
rank = 1

# prev_freq = fdist.most_common()[0][1]

for word, freq in fdist.most_common():
#     if freq != prev_freq:
#         rank +=1
#         prev_freq = freq
    ranks.append(math.log(rank))
    freqs.append(math.log(freq))
    ranked_words[word] = rank
    rank +=1
    
def zipfunc(word):
    word_rank = ranked_words[word]
    word_freq = fdist[word]
    predicted = (1/word_rank)
    
    val = 0
    for i in range(1,len(types)+1):
        val += (1/i)
    
    predicted = predicted/val
    
    return str(word)+': Rank-' +str(word_rank)+' Observed-'+str(word_freq)+' Predicted-'+str('%.5f'%predicted)

print('\n'+zipfunc('the'))
print(zipfunc('hamlet'))
print(zipfunc('rose'))
print(zipfunc('honourable'))
print(zipfunc('royally')+'\n')


plt.plot(ranks, freqs)
plt.ylabel('log(frequency)')
plt.xlabel('log(rank)')
plt.show()



# #==========================================#
# #Part 4
# #==========================================#
# print('===========Part 4 Not Submitted with this submission===================')

# with open("gazetteer.eng-kin.txt", encoding="utf8") as inp:
#     lines = inp.readlines()

# eng = []
# kin = []
# for l in lines:
#     l = l.strip().split('|||')
#     eng.append(l[0].strip())
#     kin.append(l[1].strip())  


# In[23]:


# def editDistance(word1, word2, matrix=False):
#     len1 = len(word1) + 1
#     len2 = len(word2) + 1
    
#     mat = []
#     for i in range(len1):
#         mat.append([0] * (len2))  # make 2D array
#     for i in range(len1):
#         mat[i][0] = i  # column
#     for j in range(len2):
#         mat[0][j] = j  # row

#     for row in range(len1):
#         for col in range(len2):      
#             if row == 0:
#                 mat[row][col] = col
#             elif col == 0:
#                 mat[row][col] = row
#             elif word1[row - 1] == word2[col - 1]:
#                 mat[row][col] = mat[row - 1][col - 1]
#             else:
#                 mat[row][col] = 1 + min(mat[row - 1][col - 1], mat[row - 1][col], mat[row][col - 1])
#     if matrix != True:
#         return mat[len(word1)][len(word2)]
#     return mat


# In[24]:


# Test
# from nltk.metrics.distance import edit_distance

# for i in range(len(eng)):
#     val = editDistance(eng[i],kin[i]) == edit_distance(eng[i],kin[i])
#     dist = editDistance(eng[i],kin[i])
#     print(eng[i]+' | '+kin[i]+': '+str(val)+' ==> '+str(dist))


# In[25]:


# editDistance(eng[0],kin[0], True)


# In[26]:


# avg_dist = 0
# #[min/max, # of pairs]
# min_pair = [0,0]
# max_pair = [0,0]

# for i in range(len(eng)):
#     dist = editDistance(eng[i],kin[i])
    
#     if i == 0:
#         min_pair = [dist, 1]
#         max_pair = [dist, 1]
#     else:
#         if dist > max_pair[0]:
#             max_pair = [dist, 1]
#         elif dist == max_pair[0]:
#             max_pair[1] +=1
            
#         if dist < min_pair[0]:
#             min_pair = [dist, 1]
#         elif dist == min_pair[0]:
#             min_pair[1] +=1
        
#     avg_dist += dist
# print('Average edit distance: '+ str((avg_dist/len(eng))))
# print('Min distance: '+ str(min_pair[0])+ ' Pairs with minimum: ' +str(min_pair[1]))
# print('Max distance: '+ str(max_pair[0])+ ' Pairs with maximum: ' +str(max_pair[1]))


# In[27]:


# ank_ind = eng.index("Ankara")
# ank_prov_ind = eng.index("Ankara Province")
# print('Ankara edit distance: '+ str(editDistance(eng[ank_ind],kin[ank_ind])))
# print('Ankara Province edit distance: '+ str(editDistance(eng[ank_prov_ind],kin[ank_prov_ind])))

# print('How do you explain the second value? \n The word province and its affiliation with its owner are different in kinyarwanda,\n while the name will remain the same.')


# In[28]:


# import operator
# def editDistanceBacktrace(mat):
#     len1 = len(mat) - 1
#     len2 = len(mat[0]) - 1
    
#     alignment = [(len1, len2)]
    
#     while (len1, len2) != (0, 0):
#         directions = [
#             (len1 - 1, len2),  # skip s1
#             (len1, len2 - 1),  # skip s2
#             (len1 - 1, len2 - 1),  # substitution
#         ]

#         direction_costs = (
#             (mat[len1][len2] if (len1 >= 0 and len2 >= 0) else float("inf"), (len1, len2))
#             for len1, len2 in directions
#         )
#         _, (len1, len2) = min(direction_costs, key=operator.itemgetter(0))

#         alignment.append((len1, len2))
#     return list(reversed(alignment))

# dist_five_ind = 0
# dist_five_mat = []
# st = ()
# for i in range(len(eng)):
#     dist = editDistance(eng[i],kin[i])
#     if dist == 5:
#         dist_five_ind = i
#         dist_five_mat = editDistance(eng[i],kin[i], True)
#         st = (eng[i],kin[i])
#         break;

# print('Country at distance 5: '+eng[dist_five_ind]+' | '+kin[dist_five_ind])
# print('Country at distance 5 Matrix: \n'+str(dist_five_mat))
# print('backtraced: \n'+str(editDistanceBacktrace(dist_five_mat)))
# #Backtrace with NLTK Test
# # from nltk.metrics.distance import edit_distance_align
# # print('backtraced: \n'+str(edit_distance_align(st[0],st[1])))


# In[ ]:





# In[ ]:




