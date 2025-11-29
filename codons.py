def create_codon_dict(file_path):
  codon_dict = {}
  with open(file_path, "r", encoding="utf-8") as f:
    for row in f:
      codon_line = row.split("\t")
      codon_dict[codon_line[0]] = codon_line[2]
  return codon_dict
