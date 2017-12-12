from distutils.core import setup

setup(
    name='FaceReplace',
    version='0.1.0',
    description='Simple facial recognition and face replacement',
    author='Matt Lewis',
    author_email='domattthings@gmail.com',
    url='',
    packages=['face_replace'],
    python_requires='>=3',
    install_requires=[
        'numpy',
        'opencv-python',
        'pillow'
    ]
)
