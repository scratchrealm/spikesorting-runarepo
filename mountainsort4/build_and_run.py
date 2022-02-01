import os
import docker
from typing import cast
import tarfile
import shutil
import kachery_client as kc
from docker.models.images import Image
from docker.models.containers import Container
from docker.types import Mount

def main():
    thisdir = os.path.dirname(os.path.realpath(__file__))
    client = docker.from_env()
    image, _ = client.images.build(path='.')
    image = cast(Image, image)
    mounts = [
        Mount(target='/input', source=f'{thisdir}/input', type='bind', read_only=True)
    ]
    container = client.containers.create(
        image.id,
        mounts=mounts
    )
    container = cast(Container, container)
    print(container.id)
    print(image.id)
    try:
        container.start()
        logs = container.logs(stream=True)
        for a in logs:
            for b in a.split(b'\n'):
                if b:
                    print(b.decode())
        output_dir = f'{thisdir}/output'
        os.mkdir(output_dir)
        with kc.TemporaryDirectory() as tmpdir:
            strm, st = container.get_archive(path='/output/')
            output_tar_path = tmpdir + '/output.tar.gz'
            with open(output_tar_path, 'wb') as f:
                for d in strm:
                    f.write(d)
            with tarfile.open(output_tar_path) as tar:
                tar.extractall(tmpdir)
            for fname in os.listdir(tmpdir + '/output'):
                shutil.move(tmpdir + '/output/' + fname, output_dir + '/' + fname)
    finally:
        try:
            container.kill()
        except:
            pass
        container.remove()
    

if __name__ == '__main__':
    main()