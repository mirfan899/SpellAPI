import os.path
import sys

import click
from gensim.corpora import WikiCorpus


@click.command()
@click.option("--dump", "-d", type=click.Path(), help="Path to XML dump file")
def main(dump, txt):
    """Convert Wikipedia xml dump file to text corpus"""
    if not dump:
        click.echo("Please provide a path to the XML dump file")
        sys.exit(1)
    if not os.path.exists(dump):
        click.echo("XML dump file does not exist")
        sys.exit(1)

    output = open("en_wiki.txt", 'w')
    wiki = WikiCorpus(dump)

    i = 0
    for text in wiki.get_texts():
        i = i + 1
        if i % 10000 == 0:
            print('Processed ' + str(i) + ' articles')
        output.write(bytes(' '.join(text), 'utf-8').decode('utf-8') + '\n')

    output.close()
    print('Processing complete!')


if __name__ == '__main__':
    main()
