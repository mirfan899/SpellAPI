### Install packages.
You need to install packages from requirements.txt
```shell
pip install -r requierments.txt
```

### Wikipedia Dump
Download the latest Wikipedia English xml dump file. 
```shell
wget  https://dumps.wikimedia.org/enwiki/20220820/enwiki-20220820-pages-articles-multistream.xml.bz2
```
Takes around 20GB space.


### Generate bigram dictionary.
Now run following script to generate bigram dictionary.
```shell
python wiki_corpus.py -d enwiki-20220820-pages-articles-multistream.xml.bz2 -o en_wiki.txt
```
It will clean up the wikipedia and generates a text file.

Now run `bigram_dictionary.py` script to generate the bigram dictionary.


### Installation
Use docker file to deploy the api.

### API
These are the endpoints for spell correction and sentence splitter.

```text
http://127.0.0.1:5000/api/v1/spell
http://127.0.0.1:5000/api/v1/split
```

Test the spell eapi with the following command:
```shell
curl --location --request POST '127.0.0.1:5000/api/v1/spell' --form 'sentence="sodium attraction dorce"'
```

Sentence splitter, api take text parameter and split it into sentences.
```shell
curl --location --request POST '127.0.0.1:5000/api/v1/split' \
--form 'text="James Smith was born on November 20, 1972 at St. Mary'\''s Keller Memorial Hospital in Scranton, Pennsylvania.
James studied engineering and mathematics at Harvard university in 1990.
James bought 2 dogs, 3 computers, fur jacket, multiple diamonds while shopping in Seattle.
John Travolta bought 13 goldfish, 2 eels, 200 apples, and 4 parrots."'
```

or run test.py to check the api is working.
```shell
python test.py
```


### helpful
https://www.markhneedham.com/blog/2015/02/12/pythongensim-creating-bigrams-over-how-i-met-your-mother-transcripts/

### datasets
https://www.kaggle.com/datasets/sergejnuss/united-states-cities-database
https://www.kaggle.com/datasets/kaggle/us-baby-names

### Sort and unique names and cities
```shell
sort dictionary/cities.txt | uniq > dictionary/sorted_cities.txt
sort dictionary/names.txt | uniq > dictionary/sorted_names.txt
cat dictionary/sorted_names.txt > dictionary/names.txt 
cat dictionary/sorted_cities.txt > dictionary/cities.txt 
```