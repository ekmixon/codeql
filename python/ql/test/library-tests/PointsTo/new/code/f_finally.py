class Queue(object):

    def close(self):
        self._closed = True
        try:
            self._reader.close()
        finally:
            if close := self._close:
                self._close = None
                close() # FP was here: None on exceptional branch
