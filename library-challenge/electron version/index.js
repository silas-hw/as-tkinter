const { BrowserWindow } = require('@electron/remote');

document.getElementById('close').addEventListener('click', close_window)

function close_window() {
    var window = BrowserWindow.getFocusedWindow();
    window.close();
}