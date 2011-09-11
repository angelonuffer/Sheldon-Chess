var sock = new WebSocket("ws://localhost:8080/application_handler")

sock.onmessage = function(evt)
{
    eval(evt.data)
}
