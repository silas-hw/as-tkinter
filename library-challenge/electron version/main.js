const {app, BrowserWindow } = require('electron')

function makeWindow () {
    const win = new BrowserWindow({
        width: 500,
        height: 500,
        preload:'./preload.js'
    })

    win.loadFile('index.html')
}

app.whenReady().then(() => {
    makeWindow()
})