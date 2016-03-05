import sys,os,xml.etree.ElementTree as ET
import re





condition = False

def regexp_plus_plus(lemma):
    # caractère alphabetique et les caractère fr , le tout entre un
    # ^ : devant la classe [] dit que on veut au debut de la chaine
    # + : au moins une fois un des char dans la classe
    # $ : et on finit avec ce qui il y a dans la classe
     p = re.compile("^[a-zA-Záàâäãåçéèêëíìîïñóòôöõúùûüýÿæœ�?ÀÂÄÃÅÇÉÈÊË�?ÌÎ�?ÑÓÒÔÖÕÚÙÛÜ�?ŸÆŒ]{4,12}$")
     #p = re.compile("\S")

     if re.match(p,lemma,flags=0):
         return True
     else :
         return False

if len(sys.argv) < 2 :
    exit();
else:
    nom_fichier = sys.argv[1];
    print("nom du fichier : "+nom_fichier)

    tree  = ET.parse(nom_fichier)
    root = tree.getroot()

    list_entry  = root.findall('entry')
    print(len(list_entry))


