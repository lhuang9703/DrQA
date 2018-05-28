#! usr/bin/python
# -*-coding:utf-8 -*-

import json
def astrcmp_1(str,li):
  mark = 0
  for i in range(len(li)):
    if str.lower() == li[i].lower():
      mark = 1
  if mark == 1:
    return 1
  else:
    return 0

def astrcmp_2(li,str):
  mark = 0
  for i in range(len(li)):
    if str.lower() == li[i].lower():
      mark = 1
  if mark == 1:
    return 1
  else:
    return 0
	
def astrcmp(str1,str2):
  return str1.lower() == str2.lower()
skip = 0
with open("/home/jiaosd/drqa/results/data01_5b_answer.json",'r',encoding = 'UTF-8') as f1:
  s1 = json.load(f1)
num = 0
num2 = 0
P_all = 0
R_all = 0
F1_all = 0
c1 = 0
c5 = 0
mrr = 0
mark = 0
mark2 = 0
mark3 = 0
p1 = open('right_factoid_c1.txt','w')
p2 = open('right_factoid_c5.txt','w')
p3 = open('right_list_total.txt','w')
p4 = open('right_list_part.txt','w')
with open("/home/jiaosd/drqa/data/BioASQ-trainingDataset6b.json",'r',encoding = 'UTF-8') as f2:
  s2 = json.load(f2)
questions_1 = s1["questions"]
questions_2 = s2["questions"]
print(len(questions_1))
print(len(questions_2))
for i in range(len(questions_1)):
  question_id = questions_1[i]["id"]
  question_type = questions_1[i]["type"]
  if question_type == "factoid":
    for j in range(len(questions_2)):
      question_id_2 = questions_2[j]["id"]
      if question_id_2 == question_id:
        exact_answer1 = questions_1[i]["exact_answer"]
        try:
          exact_answer2 = questions_2[j]["exact_answer"]
        except Exception as e:
          skip += 1
          continue
        for k in range(len(exact_answer1)):
          temp = exact_answer1[k][0]
          for r in range(len(exact_answer2)):
            if astrcmp(temp,exact_answer2[r]):
              c5 = c5+1
              mrr = mrr + 1/(k+1)
              if k == 0:
                c1 = c1+1
                p1.write(questions_1[i]["body"])
              else:
                p2.write(questions_1[i]["body"])
              mark = 1
              break
          if mark == 1:
            mark = 0
            break		  
    num = num+1
  if question_type == "list":
    TP = 0
    FP = 0
    FN = 0
    for j2 in range(len(questions_2)):
      question_id_22 = questions_2[j2]["id"]
      if question_id_22 == question_id:
        num2=num2+1
        exact_answer12 = questions_1[i]["exact_answer"]
        try:
          exact_answer22 = questions_2[j2]["exact_answer"]
        except Exception as e:
          skip += 1
          continue
        for k2 in range(len(exact_answer12)):
          temp2 = exact_answer12[k2][0]
          for r2 in range(len(exact_answer22)):
            if astrcmp_1(temp2,exact_answer22[r2]):
              TP = TP+1
              mark2 = 1
              break
          if mark2 == 0:
            FP = FP+1
          else:
            mark2 = 0
        for k3 in range(len(exact_answer22)):
          for r3 in range(len(exact_answer12)):
            if astrcmp_2(exact_answer22[k3],exact_answer12[r3][0]):
              mark3 = 1
              break
          if mark3 == 0:
            FN = FN+1
          else:
            mark3 = 0
        if TP != 0:
          p4.write('questions_2[j2]["body"]')
        if TP+FP == 0:
          a = 0
        else:
          a = TP/(TP+FP)
        b = TP/(TP+FN)
        if a==1 and b==1:
          p3.write('questions_2[j2]["body"]')
        if TP+FP != 0:
          P_all = P_all+TP/(TP+FP)
        R_all = R_all+TP/(TP+FN)
        if a+b != 0:
          F1_all = 2*a*b/(a+b)+F1_all
print("There are ",end="")
print(num2,end="")
print(" list questions. Here are evaluation index:")
print("mean precision = ",end="")	  
print(P_all/num2)
print("recall = ",end="")
print(R_all/num2)
print("F-measure = ",end="")
print(F1_all/num2)
print("There are ",end="")
print(num,end="")
print(" factoid questions. Here are evaluation index:")
print("LAcc = ",end="")
print(c5/num)
print("SAcc = ",end="")
print(c1/num)
print("MRR = ",end="")
print(mrr/num)
print('skip: '+str(skip))
