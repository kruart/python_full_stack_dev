# Otus web 01 Word Counter

## Description
This simple library counts words (verbs by default) in different folders and shows simple stats.

## Getting Started

### Prerequisites
- Python 3
- Venv
- Pip

## Installing
Make a new virtualenv (you may as well not if you know what you're doing)

```
$ python -m venv <your_path>/myenv
```

Install requirements
```
$ pip install -r requirements.txt
```

Add an nltk perception tagger:
```
$ python3
>>> import nltk; nltk.download('averaged_perceptron_tagger')
```

## How to use
Change the directory and run program with arguments(if there are no arguments, the current directory is meant):
```
cd 01_word_counter
python3 count_verbs.py <directory_path>
```

For example:
```
python3 count_verbs.py /usr/lib/python3/dist-packages/
```

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details