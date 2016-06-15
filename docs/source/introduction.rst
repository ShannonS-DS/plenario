==============
About Plenario
==============

Over the past few years, levels of government from the `federal administration <https://data.gov>`_ to individual municipalities like the `City of Chicago <https://data.cityofchicago.org/>`_ have begun embracing open data, releasing datasets publicly for free. This movement has vastly increased the amount of data available, but existing platforms and technologies are designed mainly to view and access individual datasets one at a time. This restriction contradicts decades of research contending that no aspect of the urban landscape is truly isolated; **in today's cities**, **everything is connected to everything else**.

Furthermore, researchers are often limited in the questions they can ask by the data available to answer them. It is not uncommon to spend 75% of one\’s time locating, downloading, cleaning, and standardizing the relevant datasets \— leaving precious little resources for the important work.


Mission
^^^^^^^



Plenario is a centralized hub for open datasets from around the world. It is designed to take us from "spreadsheets on the web" to truly smart open data. This rests on two fundamental breakthroughs:

1)  Allow users to assemble and download data from multiple, independent data sources, such as two different municipal data portals, or the federal government and a privately curated dataset.

2)  Unite all datasets along a single spatial and temporal index, making it possible to do complex aggregations with one query.

With these advances, Plenario allows users to study regions over specified time periods using all relevant data, regardless of original source, and represent the data as a single time series. By providing a single, centralized hub for open data, the Plenario platform enables urban scientists to ask the right questions with as few constraints as possible.


Features of the Plenario Platform
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Automatic Dataset Importation
*****************************

Plenario is more than just a tool or a website: it provides an infrastructure for working with open data. At its heart is an automated `ETL builder <https://en.wikipedia.org/wiki/Extract,_transform,_load>`_ to extract data from other sources, run custom transformations (to clean and standardize the data, and to align its field definitions with those of similar datasets), and load it into the database. Users can thus expand the universe of accessible data by importing open datasets from a variety of sources\-such as data portals that run using Socrata or CKAN, or datasets assembled by independent academics and organizations. Plenario then makes the datasets available to all users of the platform for download and analysis.

One Spatio-Temporal Index
*************************

If a dataset has spatial and temporal attributes, then it can be added to the platform and merged into the map and timeline along with all the other datasets. A single query can access all datasets in Plenario, and even perform joins and find relationships between them, by using these indices.

An Open Platform
****************

At its heart, Plenario is driven by the philosophy build it and they will come. Our API supports third-party apps and tools built on top of the Plenario infrastructure, which is a model that has been shown to work well for open data. Examples range from tracking crime to visualizing municipal budgets, and from adopting fire hydrants to alerting residents about sewage overflow.

Plenario is built as a collaborative project, and the entire platform is open source, extensible to all locations, and ready to deploy. The source code is actively maintained on `GitHub <https://github.com/UrbanCCD-UChicago/plenario>`_, and the entire project can be forked for private or customized use. Furthermore, the Plenario API can be used with multiple front-end frameworks, from custom mobile and web apps to a complex ESRI application.

Funding
^^^^^^^

Plenario is funded by the `National Science Foundation Computer and Information Science and Engineering directorate <http://www.nsf.gov/dir/index.jsp?org=CISE>`_ through a grant to the `Urban Center for Computation and Data <http://www.urbanccd.org/>`_ at the Computation Institute of the University of Chicago and Argonne National Laboratory.

Team
^^^^

The Plenario team brings together students and scientists from the Computation Institute and from the University of Chicago\’s Harris School for Public Policy, with funding from the John D. and Catherine T. MacArthur Foundation. It is being implemented by the Urban Center for Computation and Data and `DataMade <datamade.us>`_.

Get Involved
^^^^^^^^^^^^

Join our community to hear about platform updates, new features and discuss the potential uses of Plenario. We want to start a conversation with you, the users, about what Plenario can do for you \- whether you're a city manager, an app developer, a researcher, or a citizen interested in exploring open data. Join our Google Group `here <https://groups.google.com/forum/#!forum/plenariodataportal>`_.
