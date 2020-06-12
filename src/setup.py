from distutils.core import setup, Extension

# needs the 'stdc++' library in order to compile with python3 on Debian and Ubuntu
module_0 = Extension('randoms', include_dirs=['usr/bin/include'], libraries=[
                     'pthread', 'stdc++'], sources=['randoms.cc'], extra_compile_args=['-std=c++14'], language=['c++'])

setup(name='randoms', version='1.0', description='Generate randoms numbers using the Mersenne Twister',
      url='http://www.elk.nipne.ro', ext_modules=[module_0])
