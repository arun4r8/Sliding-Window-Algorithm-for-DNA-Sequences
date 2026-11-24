# Longest Common DNA Substring (Sliding Window)

Finds the longest stretch(es) of bases that two DNA strands have in common.

## How it works

The shorter strand is scanned with a window that starts at its full length and
shrinks by one base at a time. At each window size, every substring of the shorter
strand is checked against the longer one. The first size that produces any match
is the longest, and all distinct matches of that length are returned in sorted
order. Comparison is case-insensitive.

## Usage

```bash
python dna.py < dna.in
```

Input: a line with the number of pairs, then two lines (one strand each) per pair.

```
3
GAAGGTCGAA
CCTCGGGA
ATGATGGAC
GTGATAAGGACCC
AAATTT
GGGCCC
```

Output: each pair's longest common substrings, one per line, with a blank line
between pairs:

```
TCG

GGAC
TGAT

No Common Sequence Found
```
