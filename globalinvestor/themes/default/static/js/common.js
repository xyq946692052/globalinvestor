function toPage(value) {
    var url = document.location.href;
    url += (url.indexOf("?") == -1 ? "?" : "&");
    url += 'page' + "=" + value;
    window.location.href = url;
}