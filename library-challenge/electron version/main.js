const {app, BrowserWindow } = require('electron')

function makeWindow () {
    const win = new BrowserWindow({
        width: 400,
        height: 400,
        resizable: false,
        preload:'./preload.js'
    })

    win.loadFile('index.html')
}

app.whenReady().then(() => {
    makeWindow()
})