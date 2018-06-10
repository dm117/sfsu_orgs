from greekalphabet import *

myfile = open("orgs.txt", "r")
orglist = []

for i in myfile:
    orglist.append(i)

myfile.close()

outfile1 = open("greekorgs.txt", "w")

# only write Greek orgs to file
for name in orglist[:]:
    for word in alphabet:
        if word in name:
            outfile1.write(name)
            orglist.remove(name)
            break

# for name in orglist:
#     for letter in alphabet:
#         if letter in name:
#             orglist.remove(name)
#             break

outfile1.close()

# only write orgs that aren't Greek to file
outfile2 = open("orgsresults.txt", "w")
for values in orglist:
    outfile2.write(values)

outfile2.close()
