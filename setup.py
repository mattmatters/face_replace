from distutils.core import setup

setup(
    name='face_replace',
    version='0.1.0',
    description='Simple facial recognition and face replacement',
    author='Matt Lewis',
    author_email='domattthings@gmail.com',
    url='https://github.com/mattmatters/face_replace',
    download_url = 'https://github.com/mattmatters/face_replace/archive/0.1.3.tar.gz',
    packages=['face_replace'],
    python_requires='>=3',
    install_requires=[
        'numpy',
        'opencv-python',
        'pillow'
    ]
)
