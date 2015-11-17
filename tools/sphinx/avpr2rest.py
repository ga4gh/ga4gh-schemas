
import sys
import json
import os
import re
import argparse

def get_file_locations():
  parser = argparse.ArgumentParser()
  parser.add_argument('input', help='Input AVPR filename(s)', nargs='+')
  parser.add_argument('output', help='Output directory')
  args = parser.parse_args()
  return (args.input, args.output)

def typename(typeobject):
  if isinstance(typeobject, list):
    union_names = [typename(item) for item in typeobject]
    return '|'.join(union_names)

  elif isinstance(typeobject, dict):
    if typeobject['type'] == 'array':
      return 'array<%s>' % typename(typeobject['items'])
    elif typeobject['type'] == 'map':
      return 'map<%s>' % typename(typeobject['values'])

  elif isinstance(typeobject, basestring):
    return typeobject

  raise ValueError

def cleanup_doc(doc,indent=0):
  return '\n'.join([' '*indent + line for line in doc.split('\n')])

if __name__ == '__main__':

  avpr_filenames, rest_directory = get_file_locations()

  for avpr_filename in avpr_filenames:
    base_filename = os.path.basename(avpr_filename)
    name = os.path.splitext(base_filename)[0]

    rest_filename = os.path.join(rest_directory, name+'.rst')

    with open(avpr_filename,'r') as f:
      data = json.load(f)

    output = data['protocol'] + '\n'
    output += '*' * len(data['protocol']) + '\n\n'

    if 'doc' in data:
      output += cleanup_doc(data['doc']) + '\n\n'

    for message_name in data['messages']:
      message_def = data['messages'][message_name]
      doc = message_def['doc']
      # process formal parameters ('request')
      request = message_def['request']
      # collect the names
      param_names = []
      for param in request:
        param_names.append(param['name'])
      response = message_def['response']
      errors = message_def['errors']
      output += " .. function:: %s(%s)\n\n" % (message_name,
                                               ', '.join(param_names))
      for param in request:
        output += "  :param %s: %s: %s\n" % (param['name'], param['type'],
                                             param['doc'])
      output += "  :return type: %s\n" % response
      output += "  :throws: %s\n\n" % ', '.join(errors)
      output += cleanup_doc(doc)
      output += "\n\n"

    for item in data['types']:
      output += '.. avro:%s:: %s\n\n' % (item['type'], item['name'])

      if item['type'] == 'record':
        for field in item['fields']:
          output += '  :field %s:\n' % field['name']
          if 'doc' in field:
            output += cleanup_doc(field['doc'],indent=4) + '\n'
          output += '  :type %s: %s\n' % (field['name'], typename(field['type']))
        output += '\n'

      if item['type'] == 'enum':
        output += '  :symbols: %s\n' % '|'.join(item['symbols'])

      if item['type'] == 'fixed':
        output += '  :size: %s\n' % item['size']

      if 'doc' in item:
        output += cleanup_doc(item['doc'],indent=2) + '\n\n'

    with open(rest_filename,'w') as f:
      f.write(output)

def get_file_locations():
  parser = argparse.ArgumentParser()
  parser.add_argument('input', help='Input AVPR filename(s)', nargs='+')
  parser.add_argument('output', help='Output directory')
  args = parser.parse_args()
  return (args.input, args.output)

def typename(typeobject):
  if isinstance(typeobject, list):
    union_names = [typename(item) for item in typeobject]
    return '|'.join(union_names)

  elif isinstance(typeobject, dict):
    if typeobject['type'] == 'array':
      return 'array<%s>' % typename(typeobject['items'])
    elif typeobject['type'] == 'map':
      return 'map<%s>' % typename(typeobject['values'])

  elif isinstance(typeobject, basestring):
    return typeobject

  raise ValueError

if __name__ == '__main__':

  avpr_filenames, rest_directory = get_file_locations()

  for avpr_filename in avpr_filenames:
    base_filename = os.path.basename(avpr_filename)
    name = os.path.splitext(base_filename)[0]

    rest_filename = os.path.join(rest_directory, name+'.rst')

    with open(avpr_filename,'r') as f:
      data = json.load(f)

    output = data['protocol'] + '\n'
    output += '*' * len(data['protocol']) + '\n\n'

    if 'doc' in data:
      output += cleanup_doc(data['doc']) + '\n\n'

    for message_name in data['messages']:
      message_def = data['messages'][message_name]
      doc = message_def['doc']
      # process formal parameters ('request')
      request = message_def['request']
      # collect the names
      param_names = []
      for param in request:
        param_names.append(param['name'])
      response = message_def['response']
      errors = message_def['errors']
      output += " .. function:: %s(%s)\n\n" % (message_name,
                                               ', '.join(param_names))
      for param in request:
        output += "  :param %s: %s: %s\n" % (param['name'], param['type'],
                                             param['doc'])
      output += "  :return type: %s\n" % response
      output += "  :throws: %s\n\n" % ', '.join(errors)
      output += cleanup_doc(doc)
      output += "\n\n"

    for item in data['types']:
      output += '.. avro:%s:: %s\n\n' % (item['type'], item['name'])

      if item['type'] == 'record':
        for field in item['fields']:
          output += '  :field %s:\n' % field['name']
          if 'doc' in field:
            output += cleanup_doc(field['doc'],indent=4) + '\n'
          output += '  :type %s: %s\n' % (field['name'], typename(field['type']))
        output += '\n'

      if item['type'] == 'enum':
        output += '  :symbols: %s\n' % '|'.join(item['symbols'])

      if item['type'] == 'fixed':
        output += '  :size: %s\n' % item['size']

      if 'doc' in item:
        output += cleanup_doc(item['doc'],indent=2) + '\n\n'

    with open(rest_filename,'w') as f:
      f.write(output)
