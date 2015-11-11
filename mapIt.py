#! python3
# mapIt.py
# command line or clipboard

import webbrowser, sys
if len(sys.argv) > 1:
  # Get address from the command line
  address = ' '.join(sys.argv[1:])
