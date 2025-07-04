from setuptools import setup, Extension, find_packages
from pathlib import Path

BSEC_ROOT = Path('bsec2-6-1-0_generic_release_22102024')
BSEC_ALGO_ROOT = BSEC_ROOT / 'algo/bsec_IAQ_Sel'
BSEC_LIB_DIR = BSEC_ALGO_ROOT / 'bin/RaspberryPi/PiFour_Armv8'
BSEC_INC_DIR = BSEC_ALGO_ROOT / 'inc'
BSEC_SENSOR_API_ROOT = BSEC_ROOT / 'examples/BSEC_Integration_Examples/src/bme68x'

ext_comp_args = ['-D BSEC']
libs = ['pthread', 'm', 'rt', 'algobsec']
lib_dirs = ['/usr/local/lib',
            str(BSEC_LIB_DIR)]

LIBDIR = Path(__file__).parent

README = (LIBDIR / "README.md").read_text()

bme68x = Extension('bme68x',
                   extra_compile_args=ext_comp_args,
                   include_dirs=['/usr/local/include',
                                  str(BSEC_SENSOR_API_ROOT),
                                  str(BSEC_INC_DIR)],
                   libraries=libs,
                   library_dirs=lib_dirs,
                   depends=[str(BSEC_SENSOR_API_ROOT / 'bme68x.h'),
                            str(BSEC_SENSOR_API_ROOT / 'bme68x.c'),
                            str(BSEC_SENSOR_API_ROOT / 'bme68x_defs.h'),
                            'internal_functions.h',
                            'internal_functions.c'],
                   sources=['bme68xmodule.c', str(BSEC_SENSOR_API_ROOT / 'bme68x.c'), 'internal_functions.c'])

setup(name='bme68x',
      version='1.3.0',
      description='Python interface for BME68X sensor and BSEC',
      long_description=README,
      long_description_content_type='text/markdown',
      url='https://github.com/pi3g/bme68x-python-library',
      author='Nathan',
      author_email='nathan@pi3g.com',
      license='MIT',
      classifiers=[
           'Development Status :: 3 - Alpha',
           'Intended Audience :: Developers',
           'License :: OSI Approved :: MIT License',
          'Natural Language :: English',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: Implementation :: CPython',
          'Topic :: Scientific/Engineering :: Atmospheric Science',
      ],
      keywords='bme68x bme680 bme688 BME68X BME680 BME688 bsec BSEC sensor environment temperature pressure humidity air pollution',
      packages=find_packages(),
      py_modules=['bme68xConstants', 'bsecConstants'],
      headers=[str(BSEC_SENSOR_API_ROOT / 'bme68x.h'),
               str(BSEC_SENSOR_API_ROOT / 'bme68x_defs.h'),
               'internal_functions.h'],
      ext_modules=[bme68x])
