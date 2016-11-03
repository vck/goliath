#!/usr/bin/env python
# coding=utf-8

import re


html = {"header1":"<h1>{}</h1>",
        "header2":"<h2>{}</h2>",
        "header3":"<h3>{}</h3>",
        "header4":"<h4>{}</h4>",
        "header5":"<h5>{}</h5>",
        "header6":"<h6>{}</h6>",
        "bold":"<strong>{}</strong>"
}


md_re = {"header1":u"[\#]",
         "header2":u"[\##]",
         "header3":u"[\###]",
         "header4":u"[\####]",
         "header5":u"[\#####]",
         "header6":u"[\######]"
}


def symbol_feeder(content):
    """bruteforce for each regex in known
    markdown tags
    """
    for reg in md_re.values():
        result = re.findall(reg, content)
        if result > 0:
            parsed_symbol =  {result[0]: content.strip(result[0])}
            break
    return parsed_symbol

def markpreter(symbol):
    if symbol_feeder(symbol):
        symbol_target = symbol_feeder(symbol)
        if symbol_target.keys()[0] is "#":
            html_tag = html["header1"]

        return html_tag.format(symbol_target.values()[0])




if __name__ == '__main__':
    print symbol_feeder("#test #test #test")
    print markpreter("#test #test #test")

