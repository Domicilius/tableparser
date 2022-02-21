# tableparser
Simple Python script to roll on expanding random tables.

# USAGE
## Writing table files
Write table files with one entry per line. If you want to
expand a table to another file, put the name of the table
that you're expanding with the relative path from the original
file in brackets "[]". Example:

exampletable.txt
entry 1
entry 2
entry 3
[imported-tables/exampletable2.txt]
[imported-tables/exampletable2.txt]
entry 6

## Parsing tables
To generate an entry from this table, enclose the name of the file
in brackets the same way you would expand a table and pass that 
text into the program via standard input. Example using the above 
table:

echo "[exampletable.txt]" | parser.py

# EXTRAS
## Parsing dice formatting
Tableparser also supports the expansion of dice text, such as 
might be seen in the entry "3d6 orcs" or "2d4+2 mountain lions."
The entry would get expanded into "12 orcs" or "4 mountain
lions," respectively. To format these types of entries, use
the following formatting:

exampletable.txt
{3d6} orcs
{2d4+2} mountain lions
{2d6} [exampletable3.txt]
{1d4} [imported-tables/exampletable2.txt]
