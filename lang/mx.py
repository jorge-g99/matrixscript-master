from lang.MXLang import MXLang


def start(args):
  lang    = MXLang()
  command = args[1] if len(args) > 1 else None

  if command == None:
    lang.shell()
  elif command == "help":
    print("\ndocumentation: https://github.com/cassiofb-dev\n")
  elif command == "license":
    print("\nThis software is under MIT license.\n")
  elif command == "copyright":
    print("\nMade in Brazil by Cassio Fernando.\n")
  else:
    lang.parseFile(command)