# noweb.py

A python script that extracts code from a literate programming document in "noweb" format.

# Usage

The end goal is to produce a Python script that will take a literate program as input (noweb format) and extract code from it as output.

`noweb.py -Rhello.php hello.noweb > hello.php`

This will read in a file called hello.noweb and extract the code labelled "hello.php". We redirect the output into a hello.php file.
