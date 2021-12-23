const {app, BrowserWindow } = require('electron');

require('@electron/remote/main').initialize();
//require("@electron/remote/main").enable(webContents)

function makeWindow () {
    const win = new BrowserWindow({
        width: 400,
        height: 400,
        resizable: false,
        transparent: true,
        frame: false,
        webPreferences: {
            nodeIntegration: true,
            contextIsolation: false,
            enableRemoteModule: true,
        }
    })

    require("@electron/remote/main").enable(win.webContents)
    win.loadFile('index.html')
}

app.whenReady().then(() => {
    makeWindow();
})