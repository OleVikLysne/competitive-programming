# To work with bytes:
import io, os
Ø = io.BytesIO(os.read(0, os.fstat(0).st_size))
input = lambda: next(Ø)


# To work with strings:
import io, os
Ø = io.BytesIO(os.read(0, os.fstat(0).st_size))
input = lambda: next(Ø).decode()