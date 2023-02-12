import sys
import tarfile
import io


proxytar = io.BytesIO(bytes.fromhex(sys.stdin.read()))
with tarfile.open(fileobj=proxytar) as tar:
    info = [member for member in tar.getmembers() if member.isfile()]
    print(sum(map(lambda x: x.size, info)), len(info))
