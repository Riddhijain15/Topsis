import pathlib
p=pathlib.Path('C:/Users/vikas/Downloads/topsis_web_app_ds/.env')
b=p.read_bytes()
print(repr(b))
print('---decoded---')
print(b.decode('utf-8', errors='replace'))
