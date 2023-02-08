# TDD

It's better to put media files generated during test runs in a temp directory.

```python
@pytest.fixture(autouse=True)
def tmp_upload_dir(tmpdir, settings):
    settings.UPLOADS_DEFAULT_DEST = tmpdir.mkdir("tmp")
```