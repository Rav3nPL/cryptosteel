# cryptosteel

Tool that change Etherum private key from hexadecimal form into only-letters form siutable to use in Cryptosteel.

Usage:

    ./encode.py [privkey in hexadecimal form]

returns all-upper letters cut in 4 chars batch


    ./decode.py [encoded privkey as one long string]

returns private key as hexadecimal string

Example:

    ~/cryptosteel$ sha256sum ./encode.py
    bed1aee2c2050facae101238bea7b11478a4c579818754de740a6acb972701fb  ./encode.py
    ~/cryptosteel$ ./encode.py bed1aee2c2050facae101238bea7b11478a4c579818754de740a6acb972701fb
    BEDH AEEI CIGL GFAC AEHG HIJO BEAN BHHK NOAK CLNP OHON LKDE NKGA MACB PNIN GHFB
    ~/cryptosteel$ ./decode.py BEDHAEEICIGLGFACAEHGHIJOBEANBHHKNOAKCLNPOHONLKDENKGAMACBPNINGHFB
    bed1aee2c2050facae101238bea7b11478a4c579818754de740a6acb972701fb

