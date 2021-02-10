#!/usr/bin/python3.5

import sys, os

msafile = sys.argv[1]

if msafile and os.path.isfile(msafile):
    with open(msafile, "r") as of:
        msaseqs = of.readlines()

    ## Rearrange of seq. name and nucleotide seq.
    seqnames=[]
    eachseqs=[]
    oseqname=''
    oseq=''
    for i in range(len(msaseqs)):
        if msaseqs[i][0] == '>':
            if len(oseqname) > 0 and len(oseq) > 0:
                seqnames.append(oseqname)
                eachseqs.append(oseq)

                oseqname=''
                oseq=''

            oseqname=msaseqs[i].strip()[1:]

        else:
            oseq+=msaseqs[i].strip()

    if len(oseqname) > 0 and len(oseq) > 0:
        seqnames.append(oseqname)
        eachseqs.append(oseq)

    ## Compare 1st seq (ref.) to other seqs.
    datasize=len(seqnames)
    seqlen=len(eachseqs[0])
    checkseq=''
    variatseqs=[]
    for i in range(seqlen):
        for j in range(1, datasize):
            if eachseqs[j][i] == "-" or eachseqs[0][i] != eachseqs[j][i]:
                checkseq+="\t"+eachseqs[j][i]

            else:
                checkseq+="\t."

        variatseqs.append(checkseq)
        checkseq=''

    ## Print title
    strsID='\t'
    for i in range(datasize):
        strsID+=seqnames[i]+"\t"

    print(strsID)

    ## Print all variated sites per strain
    dashCnt=0
    for i in range(seqlen):
        samecount=variatseqs[i].count(".")
        gapcount=variatseqs[i].count("-")
        if samecount < (datasize-1):
             if (samecount+gapcount)==(datasize-1) : continue
             if eachseqs[0][i] == "-": dashCnt+=1
             print(str(i+266-dashCnt)+"\t"+eachseqs[0][i]+variatseqs[i]+"\t"+str((datasize-1)-samecount-gapcount))
