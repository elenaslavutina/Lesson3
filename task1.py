from sys import argv


script_name, virabotka, stavka, premia = argv
def zarplata (a,b,c):
    return  int(a)*int(b) + int(c)

print(zarplata(virabotka, stavka, premia))
