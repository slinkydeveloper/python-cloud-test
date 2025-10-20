import restate

from app.greeter import greeter

app = restate.app(services=[greeter])
