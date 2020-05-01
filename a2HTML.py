
# Ahmed, Mohamed Khedr
#
# HTML table extraction program
# v1.0.3 - 2018-11-11
# compatible with Python versions 3.4 - 3.7
# source file: a2HTML.py

import sys
import requests
import re

header_text = ""
table = []

def get_HTML_lines(url):
    """
    str ->  str
    This function gets the HTML lines from an url provided,extracts the data
    from the webiste source and then imports it in the python file.
    url= http://qsand.com/1340/example1.html
    get_HTML_lines(url):
            <html>
        <body>
        <h3>Table of Important Fires</h3>
        <table>
         <tr>
          <td>1666</td>
          <td>London</td>
         </tr>
         <tr>
          <td>1871</td>
          <td>Chicago</td>
         </tr>
         <tr>
          <td>1904</td>
          <td>Toronto</td>
         </tr>
        </table>
        </body>
        </html>
    
    """
    http_object = requests.get(url)
    raw_html = http_object.content
    raw_string = raw_html.decode('utf-8')

    return raw_string


def extract_heading(htmlstr):
    """
    str ->  str
    This function extractd the heading from the website provided,
    it uses regular experessions to clean up the data and only select the
    heading (words) between <((H|h)\d> and /(H|h)\d> in the HTML formated
    website. It also uses regular experssion to exteract the Headers from the websites.
   >>> extract_heading(htmlstr):
     <html>
    <body>
    <h3>Table of Important Fires</h3>
    <table>
     <tr>
      <td>1666</td>
      <td>London</td>
     </tr>
     <tr>
      <td>1871</td>
      <td>Chicago</td>
     </tr>
     <tr>
      <td>1904</td>
      <td>Toronto</td>
     </tr>
    </table>
    </body>
    </html>

    Table of Important Fires
    """
    header = re.search(r"<(H|h)\d>(.*)</(H|h)\d>", htmlstr)
    return header.group(2)


def extract_table(htmlstr):
    """
    str ->  str
    This function is used to extract the table from the website,
    it uses regular experssions (re.search/ re.findall) to find any values between <td> and </td>
    line by line in the HTML formated website and extarcted them in the python file.
    After recalling the table we can extract the cells from the rows in
    the table using re expression by only extracting the values between
    <td> and </td> in the HTML formated file.
    >>> extract_table(htmlstr):
            <html>
        <body>
        <h3>Table of Important Fires</h3>
        <table>
         <tr>
          <td>1666</td>
          <td>London</td>
         </tr>
         <tr>
          <td>1871</td>
          <td>Chicago</td>
         </tr>
         <tr>
          <td>1904</td>
          <td>Toronto</td>
         </tr>
        </table>
        </body>
        </html>
    1666	London
    1871	Chicago
    1904	Toronto 
    """
    match = re.search(r'<table.*?/table>', htmlstr, re.DOTALL)
    tablehtml = match.group()
    tableList = re.findall(r'<tr>.*?</tr>', tablehtml, re.DOTALL)
    table = []
    for row in tableList:
        cell = re.findall('<td>(.*?)</td>', row, re.DOTALL)
        table.append(cell)
    return table

def write_output_py_file(filename, header_text, Str):
    """
    str,str,str -> file, NoneType, NoneType
    This function generate another Python program named example1 to example9,
    which get from sys.arv using command line. The output of this function includes
    assignments title, course code, section number, the assignment name, due date,
    name of partners, the name of program, v1.0.3 - 2018-11-11, Python version, and source file: a2HTML.py.
    The output also includes the tables heads extract, and the clean version of that table

    >>>def write_output_py_file(filename, header_text, Str)
    url= http://qsand.com/1340/example2.html
    file name created is example2.py
    in command line the output of the file created it:
    
        Programming Language Features
        language	not equal	comment
        B	!=	/* */
        Erlang	=/=	%
        FORTRAN	.ne.	c in col.1
        m4	eval( != )	#
        Pascal	<>	(* *)
    """
    py_file  =  open( filename, "w" )
    py_file.write("""#
# inf1340, section L102
# assignment 2 - due 2018-11-21
# Ahmed, Mohamed Khedr
# Enning, Zhang
#
# HTML table extraction program
# v1.0.3 - 2018-11-11
# compatible with Python versions 3.4 - 3.7
# source file: a2HTML.py
#
if __name__ == "__main__":
""")
    py_file.write("    print(\"" + header_text + "\")\n"
)
    py_file.write("    print(\"" + Str + "\")"
)
    py_file.close()


if __name__ == "__main__":
    url = sys.argv[1]                       # Getting the url from the command input
    match = re.search(r"/(\w+).html", url)  # Looking for the file name from url
    filename = match.group(1) + ".py"       # Making the python file with the file name

    htmlstr = get_HTML_lines(url)
    header_text = extract_heading(htmlstr)
    table = extract_table(htmlstr)
    Str = ""
    for List in table:
        Str += "\\n"
        for item in List:
            Str += item + " "
    write_output_py_file(filename, header_text, Str)
    




