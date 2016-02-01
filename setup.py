from setuptools import setup, find_packages

setup(
    name = "hotdoc_gst_extension",
    version = "0.6.5",
    keywords = "gstreamer hotdoc",
    url='https://github.com/hotdoc/hotdoc_gst_extension',
    author_email = 'mathieu.duponchelle@opencreed.com',
    license = 'LGPL',
    description = "An extension for hotdoc that documents gstreamer plugins",
    author = "Mathieu Duponchelle",
    packages = find_packages(),

    package_data = {
        '': ['*.html'],
    },

    entry_points = {'hotdoc.extensions': 'get_extension_classes = hotdoc_gst_extension.gst_extension:get_extension_classes'},
    install_requires = [
    ],
)
