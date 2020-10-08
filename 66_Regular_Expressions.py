import re

mystr = '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
'''

# findall, search, split, sub, finditer #ya sb functions hain
# patt = re.compile(r'fass') #simple search this word fass

#Meta Characters
# patt = re.compile(r'.adm') #any character search symbol .
# patt = re.compile(r'^Tata') #search word that start with symbol ^
# patt = re.compile(r'iin$') #end word with iin symbol $
# patt = re.compile(r'ai*') #kitny bi ai hoon phly a aay phr i symbol *
# patt = re.compile(r'ai+') #sirf ak a ho or agay jitny mrzi i ho symbol +
# patt = re.compile(r'ai{2}') #ak a kaa baad sirf 2 i hoon  symbol {}
# patt = re.compile(r'(ai){2}') #group ma as sth hoon symbol ()
# patt = re.compile(r'ai{1}|Fax') #ya tw ain chahiya ya Fax symbol |


# Special Sequences
# patt = re.compile(r'\AFax') #Match if the specified character at the start of the string symbol \A
# patt = re.compile(r'\bFax') #match if the word is started with Fax symbol \b at start
# patt = re.compile(r'27\b')  #match if the word is ended with Fax symbol \b at end

patt = re.compile(r'\d{5}-\d{4}') #match if specified pattern found for digits symbol \d
# \D Returns a match where the string DOES NOT contain digits
# \s Returns a match where the string contains a white space character
# \S Returns a match where the string DOES NOT contain a white space character
# \w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
# \W Returns a match where the string DOES NOT contain any word characters
# \Z Returns a match if the specified characters are at the end of the string

matches = patt.finditer(mystr)
for match in matches:
    print(match)
