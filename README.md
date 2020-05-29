# README

## build & run

```bash
docker build -t blast:latest ./blast+
docker run --rm -it -v $(pwd):/local_volume blast:latest
```

## makeblastdb

### Nucleic Acid

```bash
makeblastdb -dbtype  -in target.fa -out target_db_name
```

### Protein

```bash
makeblastdb -dbtype prot -in target.fa -out target_db_name
```

## RUN blastp

```bash
blastp -db target_db_name -query query.fa -outfmt"7" -out output.tsv
```

## extract sequence 

extracting sequences with a ceratin evalue from fasta (default evalue is 0.01)

```bash
extract_sequence -i output.tsv -f target.fa --evalue 1e-5
```