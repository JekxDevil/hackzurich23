import os
import hashlib


class CacheManager:
    def __init__(self, cache_dir):
        self.cache_dir = cache_dir
        os.makedirs(self.cache_dir, exist_ok=True)

    def _get_document_cache_path(self, document_path):
        # Generate a unique cache filename based on the document's path
        hash_obj = hashlib.sha256(document_path.encode('utf-8'))
        return os.path.join(self.cache_dir, hash_obj.hexdigest())

    def is_document_cached(self, document_path):
        # Check if the document is already cached
        cache_path = self._get_document_cache_path(document_path)
        return os.path.isfile(cache_path)

    def is_document_modified(self, document_path):
        # Check if the document has been modified since it was cached
        if not self.is_document_cached(document_path):
            return True  # Document is not cached, consider it modified

        cache_path = self._get_document_cache_path(document_path)

        # Calculate the hash of the current document content
        with open(document_path, 'rb') as doc_file:
            current_hash = hashlib.sha256(doc_file.read()).hexdigest()

        # Calculate the hash of the cached document content
        with open(cache_path, 'rb') as cache_file:
            cached_hash = cache_file.read().decode('utf-8')

        return current_hash != cached_hash

    def cache_document(self, document_path, content):
        # Cache the document content
        cache_path = self._get_document_cache_path(document_path)

        with open(cache_path, 'w', encoding='utf-8') as cache_file:
            cache_file.write(content)

    def get_cached_document(self, document_path):
        # Retrieve the cached document content
        cache_path = self._get_document_cache_path(document_path)
        with open(cache_path, 'r', encoding='utf-8') as cache_file:
            return cache_file.read()
