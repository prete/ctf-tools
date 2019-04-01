import string

alphabet = string.ascii_letters + "".join([str(x) for x in range(10)]) + " "+ "."
dna = dict()
idx = 0
for a in "ACGT":
    for b in "ACGT":
        for c in "ACGT":
            dna[a+b+c] = alphabet[idx]            
            idx = idx + 1

def decode(s):
    if len(s)%3 != 0:
        raise Exception("String not multiple of 3")
    
    clear_text = ""
    for i in range(0,len(s), 3):
        clear_text  += dna[s[i:i+3]]
    print(clear_text)

if __name__ == "__main__":
    TEXT = "CTAGTCCTTTTGGTCATGATGAGT"
    #with open("dna.txt") as f:
    #    TEXT = "".join([l.strip() for l in f.readlines()])
    decode(TEXT)