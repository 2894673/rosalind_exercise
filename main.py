class DRNA:
    """[summary]
    various tools for DNA/RNA string maniplulation
    """
    def __init__(self, DRNA:str) -> str:
        self.DRNA = DRNA
        
    def print(self):
        print(self.DRNA)
        
    def count_nucleotides(self):
        A_count = 0
        C_count = 0
        T_count = 0
        G_count = 0
        for i in self.DRNA:
            if i == "A":
                A_count += 1
            if i == "C":
                C_count += 1
            if i == "T":    
                T_count += 1
            if i == "G":
                G_count += 1
        return "A: {}, C: {}, G: {}, T: {}".format(A_count, C_count, T_count, G_count)
    
    def DNA_to_RNA(self):
        return self.DRNA.replace("T", "U")
    
    def reverse_complement(self):
        rev = self.DRNA[::-1]
        rev_comp = rev.replace("A","t").replace("T","a").replace("G", "c").replace("C", "g").upper()
        return rev_comp
