import setuptools

setuptools.setup(
    name='lk-django-fcm',
    version='0.0.2',
    author='722C',
    description="LK's Django FCM Using Firebase Admin",
    license='MIT',
    url='https://github.com/lightningkite/lk-django-fcm',
    packages=[
        'fcm_notifications',
        'fcm_notifications.migrations',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Programming Language :: Python :: 3',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        'django',
        'firebase_admin',
        'django_rest_framework',
    ],
    python_requires='>=3.6',
)
