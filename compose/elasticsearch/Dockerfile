# https://github.com/elastic/elasticsearch-docker
FROM docker.elastic.co/elasticsearch/elasticsearch:5.5.2

# Add your elasticsearch plugins setup here
# Example: RUN elasticsearch-plugin install analysis-icu
COPY  index.sh /index.sh

RUN bin/elasticsearch-plugin install http://dl.bintray.com/content/imotov/elasticsearch-plugins/org/elasticsearch/elasticsearch-analysis-morphology/5.5.2/elasticsearch-analysis-morphology-5.5.2.zip
RUN bin/elasticsearch-plugin install analysis-phonetic

USER root
RUN sed -i 's/\r//' /index.sh
RUN chmod +x /index.sh

USER elasticsearch
