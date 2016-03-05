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
    match_cpt = 0
    not_match_cpt = 0
    nb_inflected_detruit =  0
    i = 0
    lemma =""
    inflected = []
    for entry in root.findall('entry'):
        lemma = entry.find('lemma').text
        if (regexp_plus_plus(lemma)):
            match_cpt = match_cpt + 1
            inflected = entry.findall('inflected')
            for t in inflected:
                nb_inflected_detruit = nb_inflected_detruit + 1
                entry.remove(t)
        else:
            root.remove(entry)
            not_match_cpt = not_match_cpt + 1
        i = i+1
    for entry in root.findall('entry'):
        match_cpt   = match_cpt + 1
        pos      = entry.find('pos').attrib
        if pos['name'] == 'prefix':
            nb_prefix_detruit   = nb_inflected_detruit + 1
            root.remove(entry)
        if pos['name'] == 'X' :
            nb_X_detruit = nb_X_detruit + 1
            root.remove(entry)
        i = i+1

    tree.write('out.xml',encoding="UTF-8",xml_declaration=True)

    print("nb match : "+str(match_cpt)+"/"+str(i))
    print("nb d'inflected detruit : "+str(nb_inflected_detruit)+"/"+str(match_cpt))
    print("nb no match : "+str(not_match_cpt)+"/"+str(i))

