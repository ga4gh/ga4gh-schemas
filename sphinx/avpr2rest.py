
import sys, json, os, re

def typename(typeobject):
  if isinstance(typeobject, list):
    return 'union{' + ','.join(field['type']) + '}'
  elif isinstance(typeobject, dict):
    if typeobject['type'] == 'array':
      return 'array<' + typename(typeobject['items']) + '>'
    elif typeobject['type'] == 'map':
      return 'map<' + typename(typeobject['values']) + '>'
  elif isinstance(typeobject, basestring):
    return typeobject
  raise ValueError

def cleanup_doc(doc,indent=0):
  return '\n'.join([' '*indent + line.strip() for line in doc.replace('`','').split('\n')])
  
if __name__ == '__main__':
  
  in_filename = sys.argv[1]
  out_filename = sys.argv[2]
  
  with open(in_filename,'r') as f:
    data = json.loads(f.read())
  
  title = re.search(r'/(\w+?)\.',in_filename).group(1).capitalize()
  
  output = title + '\n' + '*'*len(title) + '\n'
  for item in data['types']:
    output += '.. avro:' + item['type'] + ':: ' + item['name'] + '\n\n'
    
    if item['type'] == 'record':
      for field in item['fields']:
        output += '  :field ' + field['name'] + ':\n'
        output += cleanup_doc(field['doc'],indent=4) + '\n'
        output += '  :type ' + field['name'] + ': ' + typename(field['type']) + '\n'
      output += '\n'
    
    if 'doc' in item:  
      output += cleanup_doc(item['doc'],indent=2) + '\n\n'
  
  with open(out_filename,'w') as f:
    f.write(output)
