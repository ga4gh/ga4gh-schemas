
import json

filename = '../target/schemas/reads.avpr'

text = open(filename,'r').read()
decoded = json.loads(text)

open('test.py','w').write(repr(decoded))
