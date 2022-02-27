from optimized import *

max_input = int(input("N operation loop? "))
f = open("C:/Users/mahtz/Documents/GitHub/ECS-129-/graphing_data_shit.txt", "w")
for i in range(1, max_input):
    volume_protein = main(i)
    f.write(str(i) + " " + str(volume_protein) + "\n")
f.close()
print("Done")