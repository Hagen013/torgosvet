from elasticsearch import Elasticsearch, RequestsHttpConnection

es_client = Elasticsearch(
    hosts=['elasticsearch:9200/'],
    connection_class=RequestsHttpConnection
)
