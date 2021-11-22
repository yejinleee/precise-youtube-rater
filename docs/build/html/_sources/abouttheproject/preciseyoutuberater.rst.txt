##############################
precise youtube rater
##############################
precise-youtube-rater is an open-source project.

Crawling YouTube comments for reliable movie ratings.

There are so many indiscriminate fake reviews that it is difficult to recommend movies.

To this end, YouTube selects reliable comments and helps recommend movies

Using YouTube api, crawl comments from movie review videos.

Getting start
*************
Konlpy, Keras, Anaconda virtual environment, and Tensorflow systems must be established to be used.

Installation
============
dependencies:
  - _tflow_select=2.1.0=gpu
  - absl-py=0.12.0
  - aiohttp=3.7.4
  - astor=0.8.1
  - async-timeout=3.0.1
  - attrs=21.2.0
  - blas=1.0
  - blinker=1.4
  - brotlipy=0.7.0
  - ca-certificates=2021.5.25
  - cachetools=4.2.2
  - certifi=2021.5.30
  - cffi=1.14.5
  - click=8.0.1
  - coverage=5.5
  - cryptography=3.4.7
  - cudatoolkit=10.1.243
  - cudnn=7.6.5
  - cython=0.29.23
  - gast=0.2.2
  - google-auth=1.30.1
  - google-auth-oauthlib=0.4.4
  - google-pasta=0.2.0
  - grpcio=1.36.1
  - h5py=2.10.0
  - hdf5=1.10.4
  - icc_rt=2019.0.0
  - idna=2.10
  - idna_ssl=1.1.0
  - intel-openmp=2021.2.0
  - keras-applications=1.0.8
  - keras-preprocessing=1.1.2
  - libprotobuf=3.14.0
  - markdown=3.3.4
  - mkl=2020.2
  - mkl-service=2.3.0
  - mkl_fft=1.3.0
  - mkl_random=1.1.1
  - multidict=5.1.0
  - numpy=1.19.2
  - numpy-base=1.19.2
  - oauthlib=3.1.0
  - openssl=1.1.1k
  - opt_einsum=3.3.0
  - pandas=1.1.5
  - pip=21.1.1
  - protobuf=3.14.0
  - pyasn1=0.4.8
  - pyasn1-modules=0.2.8
  - pycparser=2.20
  - pyjwt=1.7.1
  - pyopenssl=20.0.1
  - pyreadline=2.1
  - pysocks=1.7.1
  - python=3.6.13
  - python-dateutil=2.8.1
  - pytz=2021.1
  - requests=2.25.1
  - requests-oauthlib=1.3.0
  - rsa=4.7.2
  - scipy=1.5.2
  - setuptools=52.0.0
  - six=1.15.0
  - sqlite=3.35.4
  - tensorboard=2.4.0
  - tensorboard-plugin-wit=1.6.0
  - tensorflow=2.1.0
  - tensorflow-base=2.1.0
  - tensorflow-estimator=2.5.0
  - tensorflow-gpu=2.1.0
  - termcolor=1.1.0
  - tqdm=4.59.0
  - typing-extensions=3.7.4.3
  - typing_extensions=3.7.4.3
  - vc=14.2
  - vs2015_runtime=14.27.29016
  - werkzeug
  - wheel=0.36.2
  - win_inet_pton=1.1.0
  - wincertstore=0.2
  - wrapt=1.12.1
  - yarl=1.6.3
  - zipp=3.4.1
  - zlib=1.2.11
pip:
  - jpype1==1.2.0
  - jsonschema==3.2.0
  - jupyter==1.0.0
  - jupyter-client==6.1.12
  - jupyter-console==6.4.0
  - jupyter-core==4.7.1
  - jupyterlab-pygments==0.1.2
  - jupyterlab-widgets==1.0.0
  - konlpy==0.5.2
  - lxml==4.6.3
  - markupsafe==2.0.1
  - mistune==0.8.4
  - nbclient==0.5.3
  - nbconvert==6.0.7
  - nbformat==5.1.3
  - nest-asyncio==1.5.1
  - notebook==6.4.0
  - packaging==20.9
  - pandocfilters==1.4.3
  - parso==0.8.2
  - pickleshare==0.7.5
  - prometheus-client==0.10.1
  - prompt-toolkit==3.0.18
  - pygments==2.9.0
  - pyparsing==2.4.7
  - pyrsistent==0.17.3
  - pywin32==301
  - pywinpty==1.1.1
  - pyzmq==22.1.0
  - qtconsole==5.1.0
  - qtpy==1.9.0
  - send2trash==1.5.0
  - terminado==0.10.0
  - testpath==0.5.0
  - tornado==6.1
  - traitlets==4.3.3
  - tweepy==3.10.0
  - urllib3==1.26.5
  - wcwidth==0.2.5
  - webencodings==0.5.1
  - widgetsnbextension==3.5.1

How to use
============
* It works at Main.py.
* Enter the desired movie accurately and enter additional information about the movie (optimal)  
* We select movie reviews and movie review comments with algorithms and preprocess review comments using Konlpy.
* Put the preprocessed comments into the model and predict the score.
* We average the ratings of all the review comments to derive the ratings of the movie ratings.
* Each comment is saved as a csv (classified as YouTube image id) file in the comment folder.

File information
  + Model_prediction.py: Bidirectional LSTM model for movie rating prediction  
  + YTVideoReviewManager.py: Movie Class File  
  + commentClass.py: Comments class file.  
  + Youtube_env.yaml: Anaconda Virtual Environment File  
  + DataPreprocessing.ipynb: Training data pre-processing file using Konlpy  