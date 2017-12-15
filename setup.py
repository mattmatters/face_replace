from setuptools import setup

setup(
    name='face_replace',
    version='0.1.10',
    description='Simple facial recognition and face replacement',
    author='Matt Lewis',
    author_email='domattthings@gmail.com',
    license='MIT',
    url='https://github.com/mattmatters/face_replace',
    download_url='https://github.com/mattmatters/face_replace/archive/0.1.10.tar.gz',
    py_modules=['face_replace'],
    packages=['face_replace'],
    install_requires=[
        'numpy',
        'opencv-python',
        'pillow',
    ],
    include_package_data=True,
    package_data={
        'paths':[
            'paths/haarcascade_frontaface_alt.xml',
            'paths/haarcascade_profileface.xml'
        ]
    }
)
