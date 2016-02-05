=========================
 Messager
=========================

This project is built using the `python project template`_. For now I will leave all the tools originally included in the template. They include:

* Paver_ for running miscellaneous tasks
* Setuptools_ for distribution (Setuptools and Distribute_ have merged_
* Sphinx_ for documentation
* flake8_ for source code checking
* pytest_ for unit testing
* mock_ for mocking (not required by the template, but included anyway)
* tox_ for testing on multiple Python versions

The sections of this README detailing the use of Paver_ and tox_ are also copied from `python project template`_

.. _Paver: http://paver.github.io/paver/
.. _Setuptools: http://pythonhosted.org/setuptools/merge.html
.. _Distribute: http://pythonhosted.org/distribute/
.. _merged: http://pythonhosted.org/setuptools/merge.html
.. _Sphinx: http://sphinx-doc.org/
.. _flake8: https://pypi.python.org/pypi/flake8
.. _pytest: http://pytest.org/latest/
.. _mock: http://www.voidspace.org.uk/python/mock/
.. _tox: http://testrun.org/tox/latest/
.. _python project template: https://github.com/seanfisk/python-project-template

Project Setup
=============

Instructions
------------

#. Clone the template project, replacing ``my-project`` with the name of the project you are creating::

        git clone https://github.com/jthompson18/COMP330.git my-project
        cd my-project

#. Create a new virtual environment for your project:

   With virtualenv_::

       virtualenv /path/to/my-project-venv
       source /path/to/my-project-venv/bin/activate

   If you are new to virtual environments, please see the `Virtual Environment section`_ of Kenneth Reitz's Python Guide.

#. Install the project's development and runtime requirements::

        pip install -r requirements-dev.txt

#. Run the tests::

        paver test

#. Generate docs::

        paver doc_html #just generates the documentation
        or
        paver doc_open #generates and opens the documentation

**Project setup is now complete!**

.. _virtualenv: http://www.virtualenv.org/en/latest/
.. _Virtual Environment section: http://docs.python-guide.org/en/latest/dev/virtualenvs/

Using Paver
-----------

The ``pavement.py`` file comes with a number of tasks already set up for you. You can see a full list by typing ``paver help`` in the project root directory. The following are included::

    Tasks from pavement:
    lint             - Perform PEP8 style check, run PyFlakes, and run McCabe complexity metrics on the code.
    doc_open         - Build the HTML docs and open them in a web browser.
    coverage         - Run tests and show test coverage report.
    doc_watch        - Watch for changes in the Sphinx documentation and rebuild when changed.
    test             - Run the unit tests.
    get_tasks        - Get all paver-defined tasks.
    commit           - Commit only if all the tests pass.
    test_all         - Perform a style check and run all unit tests.

For example, to run the both the unit tests and lint, run the following in the project root directory::

    paver test_all

To build the HTML documentation, then open it in a web browser::

    paver doc_open

Using Tox
---------

Tox is a tool for running your tests on all supported Python versions.
Running it via ``tox`` from the project root directory calls ``paver test_all`` behind the scenes for each Python version,
and does an additional test run to ensure documentation generation works flawlessly.
You can customize the list of supported and thus tested Python versions in the ``tox.ini`` file.

Opening Issues
--------------

### Templates
 - [New Issue](https://github.com/jthompson18/COMP330/issues/new?body=%23%23%23%20Description%20of%20issue%0A%0A%0A%23%23%23%20Reproduction%20Steps%0A%0A%0A%23%23%23%20Actual%20behavior%2Fresult%0A%0A%0A%23%23%23%20Expected%20behavior%2Fresult%0A%0A%0A%23%23%23%20Affected%20Org%2C%20Group%2C%20Account%0A%0A%0A%23%23%23%20Additional%20info%20(browser%20detail%2C%20etc)%0A%0A%0A)

- [Feature Request](https://github.com/jthompson18/COMP330/issues/new?body=%23%23%20Description%0A%0A%0A%23%23%20Reason%0A%0A%0A%23%23%20Background%0A%0A%0A)