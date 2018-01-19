import pytest
from snoop.data.tasks import shaorma
from snoop.data import models

pytestmark = [pytest.mark.django_db]


def test_dependent_task():
    @shaorma('test_one')
    def one():
        with models.Blob.create() as writer:
            writer.write(b'foo')

        return writer.blob

    @shaorma('test_two')
    def two(one_result):
        return one_result

    one_task = one.laterz()
    two_task = two.laterz(depends_on={'one_result': one_task})
    two_task.refresh_from_db()
    with two_task.result.open() as f:
        assert f.read() == b'foo'


def test_blob_arg():
    @shaorma('test_with_blob')
    def with_blob(blob, a):
        with blob.open(encoding='utf8') as src:
            data = src.read()

        with models.Blob.create() as output:
            output.write(f"{data} {a}".encode('utf8'))

        return output.blob

    with models.Blob.create() as writer:
        writer.write(b'hello')

    task = with_blob.laterz(writer.blob, 'world')
    assert task.blob_arg == writer.blob

    task.refresh_from_db()
    with task.result.open() as f:
        assert f.read() == b'hello world'
