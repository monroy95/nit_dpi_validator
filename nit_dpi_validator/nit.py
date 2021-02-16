import re


def nit_validador(nit):
    """
    Validador de NIT Guatemala

    Args:
        nit (str): NIT

    Returns:
        bool: True/False
    """    
    try:
        nit = str(nit)
        if not nit:
            return False
        
        # Expresion regular, para validar si aplica el patron
        nit_reg_exp = re.compile('^[0-9]+(-?[0-9kK])?$')
        if not nit_reg_exp.match(nit):
            return False
        
        # Elimacion guiones
        nit = nit.replace('-', '')
        # Digito verificador
        last_position = nit[-1]
        # Digitos excluyendo el ultimo
        dig_nit = nit[0:-1]
        # Conversion digito verificados a str y minuscula (en caso aplique)
        checker = str(last_position).lower()
        
        factor_nit = len(dig_nit) + 1
        total = 0

        for i in range(0, len(dig_nit)):
            digit_nit = int(dig_nit[i])
            total += digit_nit * factor_nit
            factor_nit = factor_nit - 1

        modulus = (11 - (total % 11)) % 11
        computed_checker = "k" if modulus == 10 else str(modulus)
        
        if checker == computed_checker:
            return True
        else:
            return False

    except:
        return False
