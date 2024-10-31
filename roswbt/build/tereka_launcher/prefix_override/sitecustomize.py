import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/dhonan/Workspaces/tereka/roswbt/install/tereka_launcher'
