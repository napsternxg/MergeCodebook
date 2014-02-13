MergeCodeBooks
==============

Create Merged Codebooks from Entity and Corpus statistics files generated using [ConText](http://context.lis.illinois.edu/)

Usage
-----

usage: `main.py [-h] [-c C] [-t T] [-f F]`

optional arguments:
  -h, --help  show this help message and exit
  -c C Type of files e for entity and c for corpus
  -t T Threshold frequency. Minimum cumulative frequency to consider in final codebook
  -f F List of files. Should be comma separated without spaces. Or can be within quotes and comma separated if file contains spaces. 


For entity files merging with threshold frequency of 100 minimum results will be saved in `EntityCodebook.csv`
```
python main.py -c e -t 100 -f Entity1.csv,Entity.csv
```

For corpus statistics files merging with threshold frequency of 100 minimum results will be saved in `CorpusCodebook.csv`
```
python main.py -c c -t 100 -f Corpus1.csv,Corpus.csv
```