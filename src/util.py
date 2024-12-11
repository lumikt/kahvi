def reference_to_string(ref_dict: dict, html = True):
    """
    Takes a reference dictionary and returns it in bibtex format using html formatting.
    Args:
        ref_dict (dict): dictionary containing reference info
        HTML (True/False): boolean to check if it is to be converted to html or plaintext
    """
    to_html = html
    if to_html:
        space,linebreak = "&nbsp;","<br>"
    else:
        space,linebreak = " ","\n"
    i = 0
    ref_dict.pop("id")
    citation_key = ref_dict.pop("citation_key")
    ref_type = ref_dict.pop("ref_type")

    string_conversion = f'@{ref_type.upper()}' + "{" +  f'{citation_key},{linebreak}'
    for key,value in ref_dict.items():
        string_conversion  +=  f'{space}{space}{space}{key} = "{value}",'
        if i == len(ref_dict)-1:
            string_conversion = string_conversion[:-1]
        string_conversion += linebreak
        i+= 1

    string_conversion += "}"+linebreak
    return string_conversion
