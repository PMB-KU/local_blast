#!/usr/local/bin/python

import argparse
import pandas as pd


def read_fasta(path):
    id_seq = {}
    with open(path) as f:
        for line in f:
            if line.startswith(">"):
                id = line.rstrip("\n").split(" ")[0]
                id_seq.setdefault(id, "")
            else:
                id_seq[id] += line.rstrip("\n") 
    return id_seq

def write_fasta(path, id_seq):
    with open(path, "w") as f:
        for k, v in id_seq.items():
            f.write(k + "\n" + v + "\n")

def read_blast_tabler_fmt(path):
    with open(path) as f:
        fields = []
        for line in f:
            if line.startswith("# Fields:"):
                fields = line.rstrip("\n").lstrip("# Fields: ").split(",")
                fields = list(map(lambda x: x.lstrip(" "), fields))
                break
    df = pd.read_csv(path, comment="#", sep="\t")
    df.columns = fields
    return df


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=str, required=True)
    parser.add_argument("-f", "--fasta", type=str, required=True)
    parser.add_argument("-o", "--output", type=str, default=None)
    parser.add_argument("--evalue", type=float, default=1e-2)
    args = parser.parse_args()

    df = read_blast_tabler_fmt(args.input)
    seq_names = list(df[df['evalue'] < args.evalue]["subject acc.ver"])
    
    id_seq = read_fasta(args.fasta)
    id_seq_for_write = {}
    for seq_name in seq_names:
        idx = ">"+seq_name
        if idx in id_seq.keys():
            id_seq_for_write[idx] = id_seq[idx]
    if args.output is None:
        output_path = args.input.split('.')[0] + ".fa"
    else:
        output_path = args.output
    
    write_fasta(output_path, id_seq_for_write)

if __name__ == "__main__":
    main()