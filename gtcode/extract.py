import ast

def get_python_code(content : str, debug=False) -> str:
    '''
    Get a string and returns the python code snipets inside that string

    PARAMETERS:
        content: str
            The input string
        debug: bool
            If True, it will print the details of the processing line
            by line
    RETURNS:
        The python code snipets
    '''

    article = content.split('\n')
    article.reverse()

    code_list = ['']
    candidate = ''
    first_line_found = False

    for line in article:
        
        if debug:
            print('LINE:', line)
            print('CANDIDATE:', candidate, sep='\n')
            print('FIRST LINE FOUND:', first_line_found)

        clean_line = line.lstrip()
        has_leading_sp = clean_line != line

        try:
            ast.parse(clean_line)
            first_line_found = len(line) > 0 or first_line_found
            
            if debug:
                print('VALID LINE')
                print('MEANING LINE?:', first_line_found)

            if not has_leading_sp:
                code_list.append(line)
                if debug:
                    print('NO LEADING SPACES')
            else:
                if debug:
                    print('LEADING SPACES')
                candidate = line + '\n' + candidate
        except:
            if debug:
                print('NO VALID LINE')
            if first_line_found:
                candidate = line + '\n' + candidate
                if not has_leading_sp:
                    try:
                        ast.parse(candidate)
                        code_list.append(candidate)
                        candidate = ''
                        first_line_found = False
                    except:
                        pass
        
        if debug:
            print('NEW CANDIDATE:', candidate, sep='\n')
            print('LAST CODE:', code_list[-1], sep='\n')
            print('==========================================================================')

    code_list.reverse()
    result = '\n'

    for line in code_list:
        if len(line.strip()) > 0:
            result += line + '\n'
    return result