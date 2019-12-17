from matplotlib import pyplot as plt
poverty_border_of_two = 15000
sum_people_Denver = 0
people_in_poverty_Denver_2018 = 0
people_in_poverty_Denver_2019 = 0
try:
  income_file1 = open("income of Denver County families.csv", "r")
  for line in income_file1:
      sum_people_Denver += len(line[0])
  print ("Amount of families in Denver County is "+ str(sum_people_Denver) + ".")
finally:
  income_file1.close()
try:
  income_file1 = open("income of Denver County families.csv", "r")
  for line in income_file1:
    line = list(line.split(","))
    if int(line[1]) < poverty_border_of_two:
       people_in_poverty_Denver_2018 += 1 
       a = (people_in_poverty_Denver_2018 * 100) / sum_people_Denver 
    if int(line[2]) < poverty_border_of_two:
       people_in_poverty_Denver_2019 += 1 
       a_1 = (people_in_poverty_Denver_2019 * 100) / sum_people_Denver       
  print ("Amount of families in poverty in 2018 is "+ str(people_in_poverty_Denver_2018) + ". It is " + str(round(a,2)) + "% of whole Denver County families of two.")
  print ("Amount of families in poverty in 2019 is "+ str(people_in_poverty_Denver_2019) + ". It is " + str(round(a_1,2)) + "% of whole Denver County families of two.")
finally:
  income_file1.close()
sum_people_Arapahoe = 0
people_in_poverty_Arapahoe_2018 = 0
people_in_poverty_Arapahoe_2019 = 0
try:
  income_file2 = open("income of Arapahoe County families.csv", "r")
  for line in income_file2:
      sum_people_Arapahoe += len(line[0])
  print ("Amount of families in Arapahoe County is "+ str(sum_people_Arapahoe) + ".")
finally:
  income_file2.close()
try:
  income_file2 = open("income of Arapahoe County families.csv", "r")
  for line in income_file2:
    line = list(line.split(","))
    if int(line[1]) < poverty_border_of_two:
       people_in_poverty_Arapahoe_2018 += 1
       b = (people_in_poverty_Arapahoe_2018 * 100) / sum_people_Arapahoe  
    if int(line[2]) < poverty_border_of_two:
       people_in_poverty_Arapahoe_2019 += 1
       b_1 = (people_in_poverty_Arapahoe_2019 * 100) / sum_people_Arapahoe      
  print ("Amount of families in poverty in 2018 is "+ str(people_in_poverty_Arapahoe_2018) + ". It is " + str(round(b,2)) + "% of whole Arapahoe County families of two.")
  print ("Amount of families in poverty in 2019 is "+ str(people_in_poverty_Arapahoe_2019) + ". It is " + str(round(b_1,2)) + "% of whole Arapahoe County families of two.")
finally:
  income_file2.close()
sum_people_Adams = 0
people_in_poverty_Adams_2018 = 0
people_in_poverty_Adams_2019 = 0
try:
  income_file3 = open("income of Adams County families.csv", "r")
  for line in income_file3:
      sum_people_Adams += len(line[0])
  print ("Amount of families in Adams County is "+ str(sum_people_Adams) + ".")
finally:
  income_file3.close()
try:
  income_file3 = open("income of Adams County families.csv", "r")
  for line in income_file3:
    line = list(line.split(","))
    if int(line[1]) < poverty_border_of_two:
       people_in_poverty_Adams_2018 += 1  
       c = (people_in_poverty_Adams_2018 * 100) / sum_people_Adams 
    if int(line[2]) < poverty_border_of_two:
       people_in_poverty_Adams_2019 += 1  
       c_1 = (people_in_poverty_Adams_2019 * 100) / sum_people_Adams 
  print ("Amount of families in poverty in 2018 is "+ str(people_in_poverty_Adams_2018) + ". It is " + str(round(c, 2)) + "% of whole Adams County families of two.")
  print ("Amount of families in poverty in 2019 is "+ str(people_in_poverty_Adams_2019) + ". It is " + str(round(c_1, 2)) + "% of whole Adams County families of two.")
finally:
  income_file3.close()
  print ("Totally in Denver City " + str(sum_people_Denver + sum_people_Arapahoe + sum_people_Adams) + " families of two.")
  print (str(people_in_poverty_Denver_2018 + people_in_poverty_Arapahoe_2018 + people_in_poverty_Adams_2018) + " families was in above of poverty line in 2018.")
  print ("In 2019 it is " + str(people_in_poverty_Denver_2019 + people_in_poverty_Arapahoe_2019 + people_in_poverty_Adams_2019))
  print ("It is " + str(round(((people_in_poverty_Denver_2018 + people_in_poverty_Arapahoe_2018 + people_in_poverty_Adams_2018) * 100) / (sum_people_Denver + sum_people_Arapahoe + sum_people_Adams),2)) + "% in 2018. And " +str(round(((people_in_poverty_Denver_2019 + people_in_poverty_Arapahoe_2019 + people_in_poverty_Adams_2019) * 100) / (sum_people_Denver + sum_people_Arapahoe + sum_people_Adams),2)) + "% in 2019.")
  x = ["2018", "2019"]
  y = [a, a_1]
  z = [b, b_1]
  w = [c, c_1]
  plt.plot(x,y)
  plt.plot(x,z)
  plt.plot(x,w)
  plt.title("Denver City Poverty Map")
  plt.xlabel("Year")
  plt.ylabel("People in poverty in %")
  plt.legend(["Denver County", "Arapahoe County", "Adams County"])
  plt.show()
'''try:
  income_file1 = open("income of Denver County families.csv", "r")
  income_file2 = open("income of Arapahoe County families.csv", "r")
  income_file3 = open("income of Adams County families.csv", "r")
  print("Denver County in 2018:")
  for line in income_file1:
    line = list(line.split(","))
    if int(line[1]) < poverty_border_of_two: 
       print(line)
  print("Denver County in 2018:")
   for line in income_file1:
    line = list(line.split(","))
    if int(line[2]) < poverty_border_of_two: 
       print(line)
  print("Arapahoe County:")
  for line in income_file2:
    line = list(line.split(","))
    if int(line[1]) < poverty_border_of_two: 
       print (line)
  print("Adams County:")
  for line in income_file3:
    line = list(line.split(","))
    if int(line[1]) < poverty_border_of_two: 
       print (line)
finally:
  income_file1.close()
  income_file2.close()
  income_file3.close()'''