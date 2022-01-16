from Bio import Entrez, Medline


class PubmedImpl:
    """ Vorlagen Klasse zur Anfrage an Pubmed """
    def getPapers(self, myQuery, maxPapers=10, myEmail="xxx.xxx@mailbox.tu-dresden.de") -> list:
        # Get articles from PubMed
        Entrez.email = myEmail
        record = Entrez.read(Entrez.esearch(db="pubmed", term=myQuery, retmax=maxPapers))
        idlist = record["IdList"]
        print("\nThere are %d records for %s." % (len(idlist), myQuery.strip()))
        records = Medline.parse(Entrez.efetch(db="pubmed", id=idlist, rettype="medline", retmode="text"))
        # records is iterable, which means that it can be consumed only once.
        # Converting it to a list, makes it permanently accessible.

        return list(records)
