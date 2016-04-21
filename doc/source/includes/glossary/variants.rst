
------------------------
Genetic variants and VCF
------------------------

Genetic variants are differences in the genome sequence from one
individual to the next. Such variation can manifest at different
scales, from small changes affecting just one or a few DNA base pairs,
to copy number variations of whole exons or genes, to large structural
variations affecting megabases or more. The GA4GH Variants schema
focuses on small variants for now, because there's less consensus on
how to represent the larger kinds of variation.

Small genetic variants can be represented as edits to a Reference
sequence: typically a tuple of (1) Reference sequence name, (2)
starting position of the affected portion on the Reference
sequence, (3) DNA sequence of the affected portion of the Reference,
and (4) alternate DNA sequence found in place of the Reference
sequence. Both the reference and alternate sequences are provided in
order to represent sequence insertions and deletions (indels). A few
examples::

    CHROM  POS     REF  ALT  
    20     14370   G    A 
    20     17330   TA   T
    20     18302   TG   ACC

The first variant is a single-nucleotide substitution of G to A. The
second variant is a deletion of an A at position 17,331. The third
variant is a multi-nucleotide change to a lengthier sequence starting
at position 18,302.

Given a list of such variants, we can specify the genotype of one or
more individuals with respect to each variant. The genotype of a
diploid individual (for an autosomal variant) may take one of three
distinct values: homozygous reference (0,0), heterozygous (0,1), or
homozygous alternate (1,1). We can then present a matrix of genotypes,
where the rows are variants as shown above, the columns are the
individuals, and each entry is one of those three genotype *calls* (or
marked missing)::

    CHROM  POS     REF  ALT   Alice   Bob
    20     14370   G    A     (0,0)   (0,1)
    20     17330   TA   T     (0,0)   (1,1)
    20     18302   TG   ACC   (0,1)     -

(If the phase of an individual's genotypes across several variant
positions is known, then the heterozygous genotypes (0,1) and (1,0)
may be considered distinct, where the order specifies which homologous
chromosome possesses the alternate sequence.)

It's possible to observe multiple different alternate sequences, or
`alleles`, affecting the same portion of the reference. This can occur
even within one individual, if their two homologous chromosomes
contain different alternate sequences, and becomes somewhat common
when representing variants observed across a population. To handle
these cases, we allow a variant to specify multiple alternate
alleles. For example::

    CHROM  POS     REF  ALT  
    20     19254   G    A,C,T
    20     21672   AT   AC,TGA

And in this case the genotypes can take values such as (0,3) or
(1,2). This multi-allelic sites model was refined and popularized in
the 1000 Genomes Project's `Variant Call Format (VCF)
<https://samtools.github.io/hts-specs/VCFv4.2.pdf>`_, upon which the
Variants schema is based.

There remain some outstanding challenges with this model of small
variants. For example, the same edit to the reference sequence can be
represented in multiple ways. There are also different ways to
represent clusters of alleles that affect overlapping but non-equal
portions of the reference. The GA4GH doesn't yet prescribe resolutions
to these ambiguities, and different conventions are used in practice.

(TODO possible additional/advanced topics: homozygous ref vs. no-call;
phasing and phase sets; genotype likelihoods; INFO, FORMAT, QUAL,
FILTER)

