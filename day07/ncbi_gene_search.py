import sys
from Bio import Entrez
from datetime import datetime
import os


def gene_search(term, count):
    Entrez.email = "Chendavidyan@gmail.com"
    handle = Entrez.esearch(db="Gene", term=term, idtype="acc", retmax=30)
    record = Entrez.read(handle)
    handle.close()
    requested_ids = record["IdList"][: int(count)]
    # print(record)
    total_count = record["Count"]

    return requested_ids, total_count


def download_gene_info(gene_id):
    handle = Entrez.efetch(db="gene", id=gene_id, rettype="gb", retmode="text")
    gene_info = handle.read()
    handle.close()
    with open(f"gene_{gene_id}.txt", "w") as file:
        file.write(gene_info)


def document_to_csv(term, count, total_count):
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_name = "search_documentation.csv"
    file_exists = os.path.isfile(file_name)
    with open(file_name, "a") as file:
        if not file_exists:
            file.write("date,term,count,total\n")
        file.write(f"{date}, {term}, {count}, {total_count}\n")


def main():

    if len(sys.argv) != 3:
        print("Usage: python ncbi_lgene_search.py TERM COUNT")
        sys.exit(1)

    
    term = sys.argv[1]
    count = sys.argv[2]
    ids, total_count = gene_search(term, count)
    for id in ids:
        download_gene_info(id)
    document_to_csv(term, count, total_count)


if __name__ == "__main__":
    main()
