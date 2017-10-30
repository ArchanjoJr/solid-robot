# Solid Robot

A Simple Terminal Wrapper script for the [GwentApi](https://gwentapi.com/) to extract  a local **JSON**.

## INSTALLING

### Prerequisites

Just Make Sure you have `python3` and `pip3` instaled on the PC:

```BASH
$ sudo apt-get install python3.6
$ sudo apt-get -y install python3-pip

```

Just follow these easy step to step guide to Download the latest script:

1. Create a Folder:
	`mkdir Folder-Name`

2. Enter the Folder:
	`cd Folder-name`

3. Clone The repository:
	`git clone https://github.com/ArchanjoJr/solid-robot.git`

4. Then Install the Dependencies:
	`pip3 install -r requirements.txt`
####After That You're Good to Go

## Usage
Example:
`python3 app.py lang(DEFAULT=en-US)`

**Definitions:**
1. LANGUANGE:
Extract your JSON with Native Languanges, Available in 9 languages

Expression    | Languange
-----------| -------------
 en-Us   | English **(United States)**
 de-DE   | German **(Standard)**
 es-ES   | Spanish **(Spain)**
 es-MX   | Spanish **(Mexico)**
 fr-FR   | French **(France)**
 it-IT   | Italian **(Italy)**
 ja-JP   | Japanese **(Japan)**
 pl-PL   | Polish **(Polony)**
 pt-BR   | Portuguese **(Brazil)**
 ru-RU   | Russian **(Russia)**

### Example: `python3 app.py pl-PL`

## NOTES:
>This script will create 2 JSON_(JAVASCRIPT OBJECT NOTATION)_ files on the folder

>1. CARDS.JSON: contaning all the cards and it basic informations like color, Faction, quotes

>2. VARIATIONS.JSON: contaning informations like image link, mill.

## Built with


* [Requests](http://docs.python-requests.org/en/master/#). - HTTP for Humans.

## Authors

* **Matheus Archanjo** - *Initial work* - [ArchanjoJr](https://github.com/ArchanjoJr)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

