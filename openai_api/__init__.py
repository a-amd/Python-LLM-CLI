from os.path import dirname, basename, isfile
import glob

# Get all the modules in the current directory
modules = glob.glob(dirname(__file__) + "/*.py")
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and not f.endswith('__init__.py')]

from .GPT35 import GPT35Turbo