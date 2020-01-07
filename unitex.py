import os
os.system("rd /s corpus-medical_snt")
os.mkdir("corpus-medical_snt")
os.system("UnitexToolLogger Normalize corpus-medical.txt -r Norm.txt --output_offsets=corpus-medical_snt/normalize.out.offsets -qutf-8-no-bom")
os.system("UnitexToolLogger Tokenize corpus-medical.snt -a Alphabet.txt -qutf-8-no-bom")
os.system("UnitexToolLogger Compress subst.dic ")
os.system("UnitexToolLogger Dico -t corpus-medical.snt -a Alphabet.txt C:/Users/%username%/AppData/Local/Unitex-GramLab/French/Dela/Delaf.bin subst.bin")
os.system("UnitexToolLogger Grf2Fst2 posologie.grf")
os.system("UnitexToolLogger Locate -t corpus-medical.snt posologie.fst2 -a Alphabet.txt -L -I --all")
os.system("UnitexToolLogger Concord corpus-medical_snt/concord.ind -f \"Courrier new\" -s12 -l40 -r55")


