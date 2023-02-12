import sys


codecs = ('cp037', 'cp1006', 'cp1250', 'cp1251', 'cp1253', 'cp1254', 'cp1255', 'cp1256', 'cp1257', 'cp1258', 'cp437',
          'cp720', 'cp737', 'cp775', 'cp850', 'cp852', 'cp855', 'cp864', 'cp866', 'cp869', 'cp874', 'cp875',
          'hp_roman8', 'iso8859_10', 'iso8859_16', 'iso8859_4', 'iso8859_5', 'koi8_r', 'latin_1', 'mac_croatian',
          'mac_greek', 'mac_iceland', 'mac_latin2')

rapier = sys.stdin.read().strip()
found = False
for codec1 in codecs:
    if found:
        break
    txt = rapier[:4] + rapier[-4:]
    try:
        txt1 = txt.encode(codec1)
    except (UnicodeEncodeError, UnicodeDecodeError):
        continue
    for codec2 in codecs:
        if found:
            break
        try:
            txt2 = txt1.decode(codec2)
        except (UnicodeEncodeError, UnicodeDecodeError):
            continue
        for codec3 in codecs:
            if found:
                break
            try:
                txt3 = txt2.encode(codec3)
            except (UnicodeEncodeError, UnicodeDecodeError):
                continue
            for codec4 in codecs:
                if found:
                    break
                try:
                    txt4 = txt3.decode(codec4)
                except (UnicodeEncodeError, UnicodeDecodeError):
                    continue
                for codec5 in codecs:
                    try:
                        txt5 = txt4.encode(codec5).decode('koi8-r')
                    except (UnicodeEncodeError, UnicodeDecodeError):
                        continue
                    else:
                        if txt5 == "ПРОЦКНЦ;":
                            try:
                                translate = rapier.encode(codec1).decode(codec2).encode(codec3).\
                                decode(codec4).encode(codec5).decode('koi8-r')
                            except (UnicodeEncodeError, UnicodeDecodeError):
                                continue
                            else:
                                if translate.isupper() and "ВЫВОД:" in translate:
                                    found = True
                                    sys.stdout.write(translate)
                                    break
