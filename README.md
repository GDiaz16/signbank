# FinSL-signbank

![coverage](https://rawgit.com/Signbank/FinSL-signbank/master/coverage.svg)

**Manage your sign language lexicons.**

FinSL-signbank is a web based database for **sign language** lexicons and corpuses.
Sign language annotation will be easier, faster, and more accurate.

**Technical documentation** for developers can be found at https://finsl-signbank.readthedocs.io/

**User documentation** is available at our [https://github.com/Signbank/FinSL-signbank/wiki][wiki]

# Overview

FinSL-signbank is being developed based on the needs of Finnish sign language researchers. It can be used for any sign language(s) that share similar requirements.
Signbank was originally developed by Steve Cassidy [https://github.com/Signbank/Auslan-signbank][auslan-signbank]. FinSL-Signbank is based on NGT Signbank [https://github.com/Signbank/NGT-signbank][ngt-signbank], NGT Signbank is a branch of Auslan Signbank.

Main features:
* Manage and organize sign language lexicons and corpuses.
* Store multiple lexicons of different sign languages.
* Use your Glosses in [ELAN][elan-link] with ECV (externally controlled dictionary).
    * ECV's are available for all lexicons automatically.
* Record videos with a webcam on the website, making the annotation process faster.
* Upload videos and connect them to glosses.
* Add comments on glosses and tag them.
* Store relationships between glosses, view a network graph of these relationships.
* Interface easily translatable to multiple languages.
* Control access to lexicons per user/group.
* Publish lexicons and their glosses.
    * Separate interface for published glosses, detailed interface for researchers/annotators.
* Add translation equivalents to your glosses in any language.

# Requirements

* Python 3 (3.4+ recommended)
* Django (1.11)

Dependencies can be found in [requirements.txt][requirements.txt] and they can be installed using pip.

# Documentation

**Technical documentation** for developers can be found at https://finsl-signbank.readthedocs.io/

**User documentation** is available at our [https://github.com/Signbank/FinSL-signbank/wiki][wiki]

# Installation

To install FinSL-signbank on linux with all the dependencies:

    $ git clone https://github.com/Signbank/FinSL-signbank.git

    $ pip install -r /path/to/finsl-signbank/requirements.txt

For detailed information see https://finsl-signbank.readthedocs.io/en/latest/installation.html

# Contribution

If you want to contribute to the project, contact the repository administrator [@henrinie][admin] or [University of Jyväskylä's Sign language centre][vkk-english].

[requirements.txt]: https://github.com/Signbank/FinSL-signbank/blob/master/requirements.txt
[vkk-english]: http://viittomakielenkeskus.jyu.fi/inenglish.html
[wiki]: https://github.com/Signbank/FinSL-signbank/wiki
[wiki-install]: https://github.com/Signbank/FinSL-signbank/wiki/Install
[auslan-signbank]: https://github.com/Signbank/Auslan-signbank
[ngt-signbank]: https://github.com/Signbank/NGT-signbank
[elan-link]: https://tla.mpi.nl/tools/tla-tools/elan/
[sqlite-link]: https://www.sqlite.org/
[admin]: https://github.com/henrinie
