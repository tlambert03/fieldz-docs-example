"""Example repo showing griffe-fieldz with mkdocs"""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("fieldz-docs-example")
except PackageNotFoundError:
    __version__ = "uninstalled"
__author__ = "Talley Lambert"
__email__ = "talley.lambert@gmail.com"
