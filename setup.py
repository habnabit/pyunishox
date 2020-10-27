from setuptools import setup

setup(
    name="pyunishox",
    license="MIT",
    version="0.1",
    ext_modules=cythonize([Extension("pyunishox", ["pyunishox.pyx"])])
)
